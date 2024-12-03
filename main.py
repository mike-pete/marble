import re
from pprint import pprint
from typing import Dict, List, Optional
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit

from pydantic import BaseModel, Field

from Page import Page
from utils import get_element_with_text


class WineItem(BaseModel):
    product_link: Optional[str] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    sku: Optional[str] = None
    origin: Optional[str] = None
    type_varietal: Optional[str] = Field(None, alias="type/varietal")
    alcohol_content: Optional[str] = Field(None, alias="alcohol content")
    price: Optional[str] = None
    image: Optional[str] = None

    def __init__(self, product_id: str) -> None:
        super().__init__()
        base_url = "https://shop.klwines.com"

        url = f"{base_url}/products/details/{product_id}"
        self.product_link = url

        soup = Page(url).soup
        sections = soup.select("main>section")

        if len(sections) == 3:
            image = sections[0].select_one("img")
            if image:
                srcset = image.get_attribute_list("srcset")
                if srcset:
                    src = srcset[0]
                    if src:
                        src_text = src.split(" ")[-2]
                        self.image = base_url + src_text

            title = sections[0].select_one("h1")
            if title:
                self.name = title.text.strip()

            for block in sections[1].select("div:has(>h2)"):
                h2 = block.select_one("h2")

                if h2:
                    label: str = h2.text.strip()

                    match label:
                        case "Notes":
                            note = block.select_one("p")

                            if note:
                                note_text = note.text.strip()
                                self.notes = note_text

                        case "Product Details":
                            details = block.select("p")

                            for detail in details:
                                text = detail.text.split(":")
                                key = (
                                    text[0]
                                    .strip()
                                    .lower()
                                    .replace(" ", "_")
                                    .replace("/", "_")
                                )

                                value = " ".join(text[1:]).strip().replace("#", "")

                                if key in [
                                    "sku",
                                    "origin",
                                    "type_varietal",
                                    "alcohol_content",
                                ]:
                                    if key not in vars(self).keys():
                                        raise Exception(
                                            "key is not a property of this class"
                                        )
                                    setattr(self, key, value)

                if self.notes is None:
                    note = sections[0].select_one("div:has(>div>h3) p")
                    if note:
                        self.notes = note.text.strip()

                    # uncomment if you want to use the critic review text as a backup for self.notes

                    # else:
                    #     review = sections[0].select_one('div:has(>svg[data-testid="FormatQuoteIcon"])')
                    #     if review:
                    #         self.notes = review.text.strip()


class WineItems(BaseModel):
    data: List[WineItem] = []

    def __init__(self, search_text: str, limit: int = 10) -> None:
        super().__init__()
        base_url = "https://www.klwines.com"
        url = f"{base_url}/Products?searchText={search_text}"
        soup = Page(url).soup

        products = soup.select(".tf-product-content>.tf-product-header>a")

        for i in range(min(len(products), limit)):
            product = products[i]

            links = product.get_attribute_list("href")
            if len(links) > 0:
                split_url = urlsplit(str(links[0]))

                product_id = parse_qs(split_url.query)["i"][0]

                if product_id:
                    self.data.append(WineItem(product_id))


search_text = "vodka"
data = WineItems(search_text).model_dump(by_alias=True)
pprint(data, indent=4)

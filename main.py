from pprint import pprint
from typing import Dict, List, Optional
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit

from pydantic import BaseModel

from Page import Page


class WineItem(BaseModel):
    product_link: Optional[str] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    sku: Optional[str] = None
    origin: Optional[str] = None
    type_varietal: Optional[str] = None
    alcohol_content: Optional[str] = None
    price: Optional[str] = None
    # image: Optional[str] = None

    def __init__(self, base_url: str, path: str) -> None:
        super().__init__()

        url = base_url + path
        self.product_link = url

        soup = Page(url).soup
        sections = soup.select("main>section")

        if len(sections) == 3:
            image = sections[0].select_one("img")
            if image:
                srcset = image.get_attribute_list("srcset")
                if len(srcset):
                    print(base_url+str(srcset[0]).strip())

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
                                        raise Exception("key is not a property of this class")
                                    setattr(self, key, value)

                if self.notes is None:
                    note = sections[0].select_one('div:has(>div>h3) p')
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

                query_params = parse_qs(split_url.query)
                filtered_query_params = {
                    key: query_params[key] for key in ["i"] if key in query_params
                }

                new_query_string = urlencode(filtered_query_params, doseq=True)

                path = urlunsplit(
                    (
                        split_url.scheme,
                        split_url.netloc,
                        split_url.path,
                        new_query_string,
                        split_url.fragment,
                    )
                )

                self.data.append(WineItem(base_url, path))


search_text = "vodka"
data = WineItems(search_text).model_dump()
pprint(data, indent=4)

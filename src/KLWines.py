import re
from typing import List, Optional
from urllib.parse import parse_qs, urlsplit

from bs4 import BeautifulSoup, Tag
from pydantic import BaseModel, Field

from Page import Page


def get_element_with_regex(elements: List[Tag], pattern: str) -> Tag | None:
    for element in elements:
        match = re.match(pattern, element.text, re.IGNORECASE)
        if match:
            return element
    return None


class KLWineItem(BaseModel):
    product_link: Optional[str] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    sku: Optional[str] = None
    origin: Optional[str] = None
    type_varietal: Optional[str] = Field(None, alias="type/varietal")
    alcohol_content: Optional[str] = Field(None, alias="alcohol content")
    price: Optional[str] = None
    image: Optional[str] = None


class KLWineItemFromProductId(KLWineItem):
    def __init__(self, product_id: str) -> None:
        super().__init__(
            **{
                "product_link": None,
                "name": None,
                "notes": None,
                "sku": None,
                "origin": None,
                "type/varietal": None,
                "alcohol content": None,
                "price": None,
                "image": None,
            }
        )

        base_url = "https://shop.klwines.com"

        url = f"{base_url}/products/details/{product_id}"
        self.product_link = url

        soup = Page(url).soup

        if name := soup.select_one("main h1"):
            self.name = name.text.strip()

        if spans := soup.select("span:has(>data)"):
            if price := get_element_with_regex(spans, r"^price:"):
                self.price = price.text.split(":")[1].strip()

        self._initialize_notes(soup)
        self._initialize_img(soup, base_url)
        self._initialize_product_details(soup)

    def _initialize_notes(self, soup: BeautifulSoup) -> None:
        if notes_header := get_element_with_regex(
            soup.select("div:has(>h3)"), r"^notes"
        ):
            if notes_header.parent:
                if notes := notes_header.parent.select_one("p"):
                    self.notes = notes.text.strip()

        if notes_header := get_element_with_regex(soup.select("h2"), r"^notes"):
            if notes_header.parent:
                if notes := notes_header.parent.select_one("p"):
                    self.notes = notes.text.strip()

    def _initialize_img(self, soup: BeautifulSoup, base_url: str) -> None:
        if zoom := get_element_with_regex(soup.select("main p"), r"^zoom"):
            if zoom.parent and zoom.parent.parent:
                if image := zoom.parent.parent.select_one("img"):
                    if srcset := image.get_attribute_list("srcset"):
                        if src := srcset[0]:
                            src_text = src.split(" ")[-2]
                            self.image = base_url + src_text

    def _initialize_product_details(self, soup: BeautifulSoup) -> None:
        product_details = soup.find(["h2", "h5"], string="Product Details")

        if product_details and product_details.parent:
            elements = product_details.parent.find_all("p")

            if origin := get_element_with_regex(elements, r"^origin:"):
                if origin:
                    self.origin = origin.text.split(":")[1].strip()

            if sku := get_element_with_regex(elements, r"^sku:"):
                if sku:
                    self.sku = sku.text.split(":")[1].strip().replace("#", "")

            if alcohol_content := get_element_with_regex(
                elements, r"^alcohol content:"
            ):
                if alcohol_content:
                    self.alcohol_content = alcohol_content.text.split(":")[1].strip()

            if type_varietal := get_element_with_regex(elements, r"^type/varietal:"):
                if type_varietal:
                    self.type_varietal = type_varietal.text.split(":")[1].strip()


class KLWines(BaseModel):
    data: List[KLWineItem] = []

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
                    self.data.append(KLWineItemFromProductId(product_id))

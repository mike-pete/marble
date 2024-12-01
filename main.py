from pprint import pprint
from typing import Dict, List, Optional

from bs4 import BeautifulSoup, Tag
from pydantic import BaseModel

from Page import Page


class WineItem(BaseModel):
    name: Optional[str] = None
    # sku: Optional[str] = None
    # notes: Optional[str] = None
    # origin: Optional[str] = None
    # type_varietal: Optional[str] = None
    # alcohol_content: Optional[str] = None
    # price: Optional[str] = None
    # image: Optional[str] = None
    product_link: Optional[str] = None


class WineItems(BaseModel):
    data: List[WineItem] = []

    def __init__(self, search_text: str, limit: int = 1) -> None:
        super().__init__()
        base_url = "https://www.klwines.com"
        url = f"{base_url}/Products?searchText={search_text}"
        soup = Page(url).soup

        products = soup.select(".tf-product-content")

        for i in range(min(len(products), limit)):
            product = products[i]

            data = WineItem()

            header = product.select_one(".tf-product-header>a")
            if header is not None:
                data.name = header.text.strip()
                links = header.get_attribute_list("href")
                if len(links) > 0:
                    path: str = str(links[0])
                    data.product_link = base_url + path

        self.data.append(data)


search_text = "vodka"
data = WineItems(search_text).model_dump()
pprint(data, indent=4)

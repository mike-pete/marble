from pprint import pprint
from typing import List, Optional
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit

from pydantic import BaseModel

from Page import Page


class WineItem(BaseModel):
    product_link: Optional[str] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    # sku: Optional[str] = None
    # origin: Optional[str] = None
    # type_varietal: Optional[str] = None
    # alcohol_content: Optional[str] = None
    # price: Optional[str] = None
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
                print(srcset)

            title = sections[0].select_one("h1")
            if title:
                self.name = title.text.strip()

            note = sections[0].select_one(
                'div:has(>svg[data-testid="FormatQuoteIcon"])'
            )
            if note:
                self.notes = note.text.strip()


class WineItems(BaseModel):
    data: List[WineItem] = []

    def __init__(self, search_text: str, limit: int = 1) -> None:
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

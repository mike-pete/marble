from pprint import pprint
from typing import ClassVar, Dict, List, Optional, TypeAlias, Union, Generic, TypeVar

from pydantic import BaseModel, model_validator

from Page import Page

ItemData: TypeAlias = Dict[str, Union[None, str, "ItemData"]]


# T = TypeVar('T')

# class Selector(Generic[T]):
#     _selector: str 

#     def __init__(self, selector:str) -> None:
#         self._selector = selector


# ###

# selector = Selector[str]('ok')


    # sku: Optional[str] = None
    # notes: Optional[str] = None
    # origin: Optional[str] = None
    # type_varietal: Optional[str] = None
    # alcohol_content: Optional[str] = None
    # price: Optional[str] = None
    # image: Optional[str] = None
    # product_link: Optional[str]

class WineItem(BaseModel):
    name: Optional[str]

    SELECTORS: ClassVar[Dict[str, str]] = {
        "name": '[data-app-insights-track-search-service-name="klwines-prod-productsearch"]'
    }

    model_config = {"json_schema_extra": {"exclude": ["SELECTORS"]}}



class WineItems(Page, BaseModel):
    data: List[WineItem] = []

    def __init__(self, url: str, limit: int = 10) -> None:
        BaseModel.__init__(self)
        Page.__init__(self, url)
        soup = self.soup
        items = soup.select(".tf-product-content")
        print(len(items))

        for i in range(min(len(items), limit)):
            obj: Dict[str, str] = {}
            item = items[i]
            print(WineItem.SELECTORS)
            name = item.select(WineItem.SELECTORS["name"])[0].text.strip()
            obj["name"] = name

            item2 = WineItem(**obj)
            print(item2.model_dump_json())
            print(name)

        # self.data.append(WineItem(**{"name": "ok"}))


search_text = "vodka"
url = f"https://www.klwines.com/Products?searchText={search_text}"
item = WineItems(url)
pprint(item.model_dump_json())




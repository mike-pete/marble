from pprint import pprint

from KLWines import KLWines

search_text = "vodka"
data = KLWines(search_text).model_dump(by_alias=True)
pprint(data, indent=4)

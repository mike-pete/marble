from pprint import pprint

from example_wine_items import notes_mismatch
from KLWines import KLWines

pprint(notes_mismatch.model_dump(by_alias=True))

search_text = "vodka"
data = KLWines(search_text, limit=1).model_dump(by_alias=True)["data"]
pprint(data, indent=4)

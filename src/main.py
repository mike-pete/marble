from pprint import pprint

from example_wine_items import exact_match, mismatch
from KLWines import KLWineItem, KLWines, compare_klwine_items

search_text = "vodka"
kl_wine_items = KLWines(search_text, limit=1).model_dump(by_alias=True)["data"]


for wine_item in kl_wine_items:
    base_item = KLWineItem(**wine_item)
    comparison_item = mismatch
    if comparison := compare_klwine_items(base_item, comparison_item):
        pprint(comparison.model_dump())

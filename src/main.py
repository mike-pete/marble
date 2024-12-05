from pprint import pprint

from example_wine_items import exact_match
from KLWines import KLWineItem, KLWines, compare_klwine_items

search_text = "vodka"
number_of_items_to_scrape = 10

print(f"Scraping {number_of_items_to_scrape} \"{search_text}\" items:\n")

kl_wine_items = KLWines(search_text, limit=number_of_items_to_scrape).model_dump(
    by_alias=True
)["data"]

pprint(kl_wine_items)


print("\n\nComparing each scraped item against comparison item:")

comparison_item = exact_match

for wine_item in kl_wine_items:
    base_item = KLWineItem(**wine_item)
    if comparison := compare_klwine_items(base_item, comparison_item):
        print('\n')
        pprint(comparison.model_dump())

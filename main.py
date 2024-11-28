from Page import Page

search_text = "vodka"
url = f"https://www.klwines.com/Products?searchText={search_text}"
page = Page(url)
soup = page.soup

items = soup.select(".tf-product-content")

print(len(items))
print(items[0])
print(items[0].select("a"))

# Marble Scraping

This code uses Python to scrap klwines.com and compare the scraped items to a "comparison item" to see how similar the klwines' products are to the product you're comparing against.

## Set Up

1. Create venv: `python3.13 -m venv .venv`

2. Use venv: `source ./.venv/bin/activate`

3. Install Requirements: `pip install -r requirements.txt`

4. Set up your `.env` file with Oxylabs credentials and an OpenAI API key

## DevX

Run mypy:

`mypy main.py --strict`

> **VSCode Note:**
>
> You might want to update VSCode with the following settings:
>
> ```json
> "mypy.runUsingActiveInterpreter": true,
> ```

After installing new dependencies make sure to add them to the requirements file:

`pip freeze > requirements.txt`

Run Ruff:

`ruff check`

`ruff format`

## Running Code

Running `python main.py` should result in something similar to this:

```shell
Scraping 10 "vodka" Items:


[{'alcohol content': '40%',
  'image': 'https://shop.klwines.com/_next/image?url=https%3A%2F%2Fcdn.klwines.com%2Fimages%2Fskus%2Fgenerated_638431997352028371_1692644x.jpg&w=256&q=75',
  'name': 'Wódka Vodka (1.75L)',
  'notes': 'A handle of good vodka will cost you $50. A handle of great vodka '
           'is just 29.99! Taste this blind against any of your big brand '
           "vodkas and you'll never go back. Wodka is the best value in vodka "
           'that we carry. Period. Wódka is one of the last estate-grown '
           'Polish rye vodkas left in existence. The distillery is near '
           'Kalisz, the oldest town in Poland, famous even in Roman times for '
           'its rye. Everything about the vodka is Polish, even the charcoal '
           '(a unique Polish birch), and most especially the rye: locally '
           'grown Dankowskie, a golden winter variant that vodka affectionados '
           'worldwide would consider one of the best and most coveted ryes. '
           'Distilled 5 times and mellowed twice. This special vodka is '
           'proofed using their polish spring water that flows and gets '
           'collected on the estate. A true product of place - not a concept '
           'often connected with Vodka.\r\n'
           '\r\n'
           'Beverage Testing Institute GOLD in 2010, 2014, 2015 & 2018\r\n'
           'Double Gold & Best Vodka (overall category winner/part of '
           'exclusive 1% club of brands @ San Francisco World Spirits '
           'Competition 2017',
  'origin': 'Poland',
  'price': '$29.99',
  'product_link': 'https://shop.klwines.com/products/details/1692644',
  'sku': '1692644',
  'type/varietal': 'Vodka'},
 {'alcohol content': '40%',
  'image': 'https://shop.klwines.com/_next/image?url=https%3A%2F%2Fcdn.klwines.com%2Fimages%2Fskus%2Fshiner_na-xl.jpg&w=256&q=75',
  'name': 'Skyy Vodka 1.75L',
  'notes': 'Special Order Only!  Will take 3-7 days to receive this product '
           'before it can be shipped.',
  'origin': 'United States',
  'price': '$39.99',
  'product_link': 'https://shop.klwines.com/products/details/640009',
  'sku': '640009',
  'type/varietal': 'Vodka'},
 {'alcohol content': '40%',
  'image': 'https://shop.klwines.com/_next/image?url=https%3A%2F%2Fcdn.klwines.com%2Fimages%2Fskus%2F1387622x.jpg&w=256&q=75',
  'name': 'Rocket Vodka 100% Apple Vodka (750ml)',
  'notes': 'This awesome vodka is locally made in El Dorado Hills from 100% '
           "apples and cut with Sierra Nevada mountain water. It's naturally "
           'gluten-free, has no sugar added, and is double carbon filtered for '
           'an exceptionally round taste. Winner of Best in Class vodka from '
           'the SIP awards and California Craft Spirits Competition.',
  'origin': 'California, United States',
  'price': '$29.99',
  'product_link': 'https://shop.klwines.com/products/details/1387622',
  'sku': '1387622',
  'type/varietal': 'Vodka'},
 {'alcohol content': '40%',
  'image': 'https://shop.klwines.com/_next/image?url=https%3A%2F%2Fcdn.klwines.com%2Fimages%2Fskus%2F1032172x.jpg&w=256&q=75',
  'name': 'Effen Vodka (750ml)',
  'notes': None,
  'origin': 'Netherlands',
  'price': '$24.99',
  'product_link': 'https://shop.klwines.com/products/details/1032172',
  'sku': '1032172',
  'type/varietal': 'Vodka'},
 {'alcohol content': '40%',
  'image': 'https://shop.klwines.com/_next/image?url=https%3A%2F%2Fcdn.klwines.com%2Fimages%2Fskus%2Fshiner_na-xl.jpg&w=256&q=75',
  'name': 'Skyy Vodka (750ml)',
  'notes': 'Classic vodka at a ridiculously low price!',
  'origin': 'United States',
  'price': '$14.99',
  'product_link': 'https://shop.klwines.com/products/details/1044153',
  'sku': '1044153',
  'type/varietal': 'Vodka'},
 {'alcohol content': '40%',
  'image': 'https://shop.klwines.com/_next/image?url=https%3A%2F%2Fcdn.klwines.com%2Fimages%2Fskus%2F640032x.jpg&w=256&q=75',
  'name': 'Ketel One Vodka (750ml)',
  'notes': 'Ketel One is made in Holland. It is a family-owned business that '
           'has been carrying on the tradition of vodka-making for eleven '
           'generations. The focus at Ketel One is quality, tradition, and '
           'personal commitment to their customers. This shows in their vodka '
           'by offering only the heart of each distillate, tasted by a member '
           'of the family before it is released. One of the best martini '
           'vodkas available.',
  'origin': 'Netherlands',
  'price': '$24.99',
  'product_link': 'https://shop.klwines.com/products/details/640032',
  'sku': '640032',
  'type/varietal': 'Vodka'},
 {'alcohol content': '40%',
  'image': 'https://shop.klwines.com/_next/image?url=https%3A%2F%2Fcdn.klwines.com%2Fimages%2Fskus%2F1005679x.jpg&w=256&q=75',
  'name': 'Charbay Vodka (1L)',
  'notes': "The wonderful Charbay Distillery has long been a partner of K&L's. "
           "They're widely regarded as one of the best craft distillers in the "
           'country with a meticulous commitment to making amazing products. '
           'Their flagship vodka is no exception and now at this absolutely '
           "amazing price, it's also one of the best values on the market.",
  'origin': 'California, United States',
  'price': '$17.99',
  'product_link': 'https://shop.klwines.com/products/details/1005679',
  'sku': '1005679',
  'type/varietal': 'Vodka'},
 {'alcohol content': '40%',
  'image': 'https://shop.klwines.com/_next/image?url=https%3A%2F%2Fcdn.klwines.com%2Fimages%2Fskus%2Fshiner_na-xl.jpg&w=256&q=75',
  'name': '360 Vodka (750ml)',
  'notes': 'Special Order Only!  Special order items are not in stock and are '
           'dependent upon quantity available from distribution. All special '
           'orders are final and non-refundable. Will take 3-7 business days '
           'to receive this product before it can be shipped. '
           'Quadruple-Distilled, Five-Times Filtered, Presented in 85% '
           'recycled bottles with reusable closures.  Eco-Friendly!',
  'origin': None,
  'price': '$36.99',
  'product_link': 'https://shop.klwines.com/products/details/1040359',
  'sku': '1040359',
  'type/varietal': 'Vodka'},
 {'alcohol content': '40%',
  'image': 'https://shop.klwines.com/_next/image?url=https%3A%2F%2Fcdn.klwines.com%2Fimages%2Fskus%2F1769177x.jpg&w=256&q=75',
  'name': 'Cathead Mississippi Vodka (750ml)',
  'notes': None,
  'origin': 'United States',
  'price': '$22.99',
  'product_link': 'https://shop.klwines.com/products/details/1769177',
  'sku': '1769177',
  'type/varietal': 'Vodka'},
 {'alcohol content': '40%',
  'image': 'https://shop.klwines.com/_next/image?url=https%3A%2F%2Fcdn.klwines.com%2Fimages%2Fskus%2Fshiner_na-xl.jpg&w=256&q=75',
  'name': 'Monopolowa Vodka (1.75L)',
  'notes': 'Special order only. Please allow 7-10 days for product to arrive.',
  'origin': 'Austria',
  'price': '$29.99',
  'product_link': 'https://shop.klwines.com/products/details/1429975',
  'sku': '1429975',
  'type/varietal': 'Vodka'}]


Comparing Each Scraped Item Against Comparison Item:


{'alcohol_content_match': True,
 'brand_match': True,
 'origin_match': True,
 'size_match': True,
 'sku': '1692644',
 'type_match': True}


{'alcohol_content_match': True,
 'brand_match': False,
 'origin_match': False,
 'size_match': True,
 'sku': '640009',
 'type_match': True}


{'alcohol_content_match': True,
 'brand_match': False,
 'origin_match': False,
 'size_match': False,
 'sku': '1387622',
 'type_match': True}


{'alcohol_content_match': True,
 'brand_match': False,
 'origin_match': False,
 'size_match': False,
 'sku': '1032172',
 'type_match': True}


{'alcohol_content_match': True,
 'brand_match': False,
 'origin_match': False,
 'size_match': False,
 'sku': '1044153',
 'type_match': True}


{'alcohol_content_match': True,
 'brand_match': False,
 'origin_match': False,
 'size_match': False,
 'sku': '640032',
 'type_match': True}


{'alcohol_content_match': True,
 'brand_match': False,
 'origin_match': False,
 'size_match': False,
 'sku': '1005679',
 'type_match': True}


{'alcohol_content_match': True,
 'brand_match': False,
 'origin_match': False,
 'size_match': False,
 'sku': '1040359',
 'type_match': True}


{'alcohol_content_match': True,
 'brand_match': False,
 'origin_match': False,
 'size_match': False,
 'sku': '1769177',
 'type_match': True}


{'alcohol_content_match': True,
 'brand_match': False,
 'origin_match': False,
 'size_match': True,
 'sku': '1429975',
 'type_match': True}
```

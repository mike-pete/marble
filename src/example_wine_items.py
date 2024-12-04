from KLWines import WineItem

exact_match = WineItem(
    **{
        "alcohol content": "40%",
        "image": "https://shop.klwines.com/_next/image?url=https%3A%2F%2Fcdn.klwines.com%2Fimages%2Fskus%2Fgenerated_638431997352028371_1692644x.jpg&w=256&q=75",
        "name": "Wódka Vodka (1.75L)",
        "notes": "A handle of good vodka will cost you $50. A "
        "handle of great vodka is just 29.99! Taste this "
        "blind against any of your big brand vodkas and "
        "you'll never go back. Wodka is the best value in "
        "vodka that we carry. Period. Wódka is one of the "
        "last estate-grown Polish rye vodkas left in "
        "existence. The distillery is near Kalisz, the "
        "oldest town in Poland, famous even in Roman "
        "times for its rye. Everything about the vodka is "
        "Polish, even the charcoal (a unique Polish "
        "birch), and most especially the rye: locally "
        "grown Dankowskie, a golden winter variant that "
        "vodka affectionados worldwide would consider one "
        "of the best and most coveted ryes. Distilled 5 "
        "times and mellowed twice. This special vodka is "
        "proofed using their polish spring water that "
        "flows and gets collected on the estate. A true "
        "product of place - not a concept often connected "
        "with Vodka.\r\n"
        "\r\n"
        "Beverage Testing Institute GOLD in 2010, 2014, "
        "2015 & 2018\r\n"
        "Double Gold & Best Vodka (overall category "
        "winner/part of exclusive 1% club of brands @ San "
        "Francisco World Spirits Competition 2017",
        "origin": "Poland",
        "price": "$29.99",
        "product_link": "https://shop.klwines.com/products/details/1692644",
        "sku": "1692644",
        "type/varietal": "Vodka",
    }
)

notes_mismatch = WineItem(
    **{
        **exact_match.model_dump(by_alias=True),
        "notes": "exotic beverage with fruity overtones and under-toung hints of oreo",
    }
)

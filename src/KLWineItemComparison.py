from typing import Optional

from pydantic import BaseModel

from KLWines import KLWineItem
from openai_client import client


class KLWineItemComparison(BaseModel):
    sku: Optional[str]
    brand_match: bool
    size_match: bool
    origin_match: bool
    type_match: bool
    alcohol_content_match: bool


def compare_klwine_items(
    base_item: KLWineItem, comparison_item: KLWineItem
) -> KLWineItemComparison | None:
    base_json = base_item.model_dump_json()
    comparison_json = comparison_item.model_dump_json()

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": """
                    Compare the two items. 
                    Only return True for fields that you are confident are a strong match. 
                    Return False if you aren't confident that the fields are a strong match.
                """,
            },
            {
                "role": "user",
                "content": """
                    For the Base Item and the Comparison Item below please do the following:
                    1. Compare the names, and return True in the brand_match field if you are confident that they do match.
                    2. Compare the sizes, and return True in the size_match field if you are confident that they do match.
                    3. Compare the origins, and return True in the origin_match field if you are confident that they do match.
                    4. Compare the types/varietals, and return True in the type_match field if you are confident that they do match.
                    5. Compare the "alcohol content", and return True in the alcohol_content_match field if you are confident that they do match.
                """
                + "\n\nBase Item:"
                + base_json
                + "\n\nComparison Item:"
                + comparison_json,
            },
        ],
        response_format=KLWineItemComparison,
    )

    if parsed := completion.choices[0].message.parsed:
        data = parsed
        data.sku = base_item.sku
        return data
    return None

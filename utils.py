from typing import List
from bs4 import Tag, NavigableString
import re

def get_element_with_text(elements: List[Tag], pattern: re.Pattern[str]) -> Tag | None:
    for element in elements:
        match = re.match(pattern, element.text)
        if match:
            return element
    return None

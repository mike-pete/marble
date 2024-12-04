from pprint import pprint

from dotenv import dotenv_values
from openai import OpenAI
from pydantic import BaseModel

# from example_wine_items import notes_mismatch
# from KLWines import KLWines

# pprint(notes_mismatch.model_dump(by_alias=True))

# search_text = "vodka"
# data = KLWines(search_text, limit=1).model_dump(by_alias=True)["data"]
# pprint(data, indent=4)

env = dotenv_values("../.env")
api_key = env["OPENAI_KEY"]

client = OpenAI(api_key=api_key)


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    response_format=CalendarEvent,
)

if parsed := completion.choices[0].message.parsed:
    data = parsed.model_dump()
    pprint(data)

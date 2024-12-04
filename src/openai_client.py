from dotenv import dotenv_values

from openai import OpenAI

env = dotenv_values("../.env")
api_key = env["OPENAI_KEY"]

client = OpenAI(api_key=api_key)

from openai import OpenAI
from decouple import config


def request_chatBot(prompt):

    client = OpenAI(
    organization='org-lbRNn8ZFnUrQIccFIQqZTO4K',
    project=config('PROJECT_ID'),
    api_key=config('OPENAI_API_KEY')
    )
    
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=False,
    )

    return stream

import os

from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2025-03-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

response_message_id = "msg_67f5cf5b3f7c8190979376902e34702b"

response = client.responses.retrieve(response_message_id)

print(response)

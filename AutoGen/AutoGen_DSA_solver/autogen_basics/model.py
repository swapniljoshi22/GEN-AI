import asyncio
from autogen_core.models import UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main():
    model_client = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        api_key="AIzaSyBDZR9AUb6y8Blk0y0lKtbKpQMbT0ncUsk",
    )

    response = await model_client.create([
        UserMessage(content="What is the capital of France?", source="user")
    ])

    print(response)
    await model_client.close()

# Run the async main function
asyncio.run(main())

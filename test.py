# # ACCESS_KEY = "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"

# import os
# from groq import Groq

# client = Groq(
#     # This is the default and can be omitted
#     api_key=os.environ.get("GROQ_API_KEY", "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"),
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant. Your response must be in German."
#         },
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],
#     model="llama3-70b-8192",
# )

# print(chat_completion.choices[0].message.content)
import os
import asyncio

from groq import AsyncGroq


async def main():
    client = AsyncGroq(api_key=os.environ.get("GROQ_API_KEY", "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"))

    stream = await client.chat.completions.create(
        #
        # Required parameters
        #
        messages=[
            # Set an optional system message. This sets the behavior of the
            # assistant and can be used to provide specific instructions for
            # how it should behave throughout the conversation.
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": "Explain the importance of fast language models",
            }
        ],

        # The language model which will generate the completion.
        model="llama3-8b-8192",

        #
        # Optional parameters
        #

        # Controls randomness: lowering results in less random completions.
        # As the temperature approaches zero, the model will become
        # deterministic and repetitive.
        temperature=0.5,

        # The maximum number of tokens to generate. Requests can use up to
        # 2048 tokens shared between prompt and completion.
        max_tokens=1024,

        # Controls diversity via nucleus sampling: 0.5 means half of all
        # likelihood-weighted options are considered.
        top_p=1,

        # A stop sequence is a predefined or user-specified text string that
        # signals an AI to stop generating content, ensuring its responses
        # remain focused and concise. Examples include punctuation marks and
        # markers like "[end]".
        stop=None,

        # If set, partial message deltas will be sent.
        stream=True,
    )

    # Print the incremental deltas returned by the LLM.
    async for chunk in stream:
        print(chunk.choices[0].delta.content, end="")

asyncio.run(main())
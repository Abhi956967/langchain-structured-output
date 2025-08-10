# from langchain_openai import OpenAI
# from dotenv import load_dotenv 
# from typing import TypedDict, Annotated, Literal, Optional

# load_dotenv()

# model  = ChatOpenAI()

# # schema
# class Review(TypedDict):

#     key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
#     summary: Annotated[str, "A brief summary of the review"]
#     sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
#     pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
#     cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
#     name: Annotated[Optional[str], "Write the name of the reviewer"]
    

# structured_model = model.with_structured_output(Review)

# result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

# The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

# However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

# Pros:
# Insanely powerful processor (great for gaming and productivity)
# Stunning 200MP camera with incredible zoom capabilities
# Long battery life with fast charging
# S-Pen support is unique and useful
                                 
# Review by Nitish Singh
# """)

# print(result['name'])


# ----------------------------------------------------------------------------------------------------------
    
# with_structured_output_typeddict_hf_api.py

import os
import json
from typing import TypedDict
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint  # ✅ new package

# 1. Load token from .env
load_dotenv()
hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    raise ValueError("Hugging Face API token not found. Please set HF_TOKEN in your .env file.")

# 2. Define the TypedDict schema
class Joke(TypedDict):
    setup: str
    punchline: str

# 3. Create Hugging Face chat model via API (no local download)
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=256,
    do_sample=False,
)

chat_model = ChatHuggingFace(llm=llm)

# 4. Bind to schema
structured_llm = chat_model.with_structured_output(Joke)

# 5. Invoke
# result = structured_llm.invoke(
#     "Tell me a short programming joke. Return the answer strictly in JSON format with keys: setup and punchline."
# )

# if result is None:
#     print("The model did not return valid structured output.")
# else:
#     print(result)
#     print(result["setup"])
#     print(result["punchline"])








    
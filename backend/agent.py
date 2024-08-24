from dotenv import dotenv_values
from langchain_ibm import WatsonxLLM
from langchain_core.prompts import PromptTemplate

# Load the environment variables
config = dotenv_values("./.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

## WATSONX
WATSONX_API_KEY = config["WATSONX_API_KEY"]
WATSONX_URL = config["WATSONX_URL"]
WATSONX_PROJECT_ID = config["WATSONX_PROJECT_ID"]

parameters = {
    "decoding_method": "sample",
    "max_new_tokens": 100,
    "min_new_tokens": 1,
    "temperature": 0.5,
    "top_k": 50,
    "top_p": 1,
}

watsonx_llm = WatsonxLLM(
    model_id="ibm/granite-13b-instruct-v2",
    apikey=WATSONX_API_KEY,
    url=WATSONX_URL,
    project_id=WATSONX_PROJECT_ID,
    params=parameters
    )


template = "Generate a random question about {topic}: Question: "

prompt = PromptTemplate.from_template(template)

llm_chain = prompt | watsonx_llm

topic = "dog"

text = llm_chain.invoke(topic)
print(text)
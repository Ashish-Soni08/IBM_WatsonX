from dotenv import dotenv_values
from langchain_core.prompts import PromptTemplate

# Load the environment variables
config = dotenv_values("./.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

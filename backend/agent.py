from dotenv import dotenv_values


config = dotenv_values("/backend/.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

## WATSONX
WATSONX_API_KEY = config["WATSONX_API_KEY"]
WATSONX_URL = config["WATSONX_API_URL"]
WATSONX_PROJECT_ID = config["WATSONX_PROJECT_ID"]


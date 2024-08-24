from dotenv import dotenv_values
import gradio as gr
import os

config = dotenv_values("./.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

## LANGSMITH(by Langchain)
LANGCHAIN_TRACING_V2=True
LANGCHAIN_ENDPOINT=config["LANGSMITH_API_URL"]
LANGSMITH_API_KEY = config["LANGSMITH_API_KEY"]
LANGSMITH_PROJECT = config["LANGSMITH_PROJECT"]
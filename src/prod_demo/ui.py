import os

import streamlit as st
import requests
from requests.exceptions import InvalidSchema, ConnectionError

BACKEND_SERVER = os.getenv("BACKEND_SERVER", "ai-prod-demo-service:80")

def backend_request(prompt):
    response = requests.get(f"http://{BACKEND_SERVER}/complete_text/?prompt={prompt}")
    response.raise_for_status()
    return response.json()['completed_text']


# Create a UI in Streamlit
st.title('Text Completion with FastAPI, Streamlit and Huggingface')

# Input text box for prompt
prompt = st.text_input("Enter your prompt:", "")

# Check if the prompt is not empty
if prompt:
    # Make a request to the FastAPI server
    try:
        completed_text = backend_request(prompt)
        st.write(f"Completed Text: {completed_text}")
    except InvalidSchema as e:
        st.write(f"An error occurred: {e}. Is the backend running?")
    except ConnectionError as e:
        st.write(f"An error occurred: {e}. Is the backend running?")
    except Exception as e:
        st.write(f"An error occurred: {e}")
        raise e

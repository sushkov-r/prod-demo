import streamlit as st
import requests

# Create a UI in Streamlit
st.title('Text Completion with FastAPI, Streamlit and Huggingface')

# Input text box for prompt
prompt = st.text_input("Enter your prompt:", "YourPromptHere")

# Check if the prompt is not empty
if prompt:
    # Make a request to the FastAPI server
    try:
        response = requests.get(f'ai-prod-demo-service:80/complete_text/?prompt={prompt}')
        if response.status_code == 200:
            completed_text = response.json()['completed_text']
            st.write(f"Completed Text: {completed_text}")
        else:
            st.write(f"Failed to get response. Status code: {response.status_code}")
    except Exception as e:
        st.write(f"An error occurred: {e}")

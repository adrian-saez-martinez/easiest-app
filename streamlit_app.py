import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load the tokenizer and model
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="Qwen/Qwen2.5-1.5B-Instruct")
pipe(messages)

# Streamlit app layout
st.title("🎈 My new app with Qwen model")
st.write("Let's start building a simple app with the Qwen model.")
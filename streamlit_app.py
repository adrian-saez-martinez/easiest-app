import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")

# Streamlit app layout
st.title("🎈 My new app with Qwen model")
st.write("Let's start building a simple app with the Qwen model.")
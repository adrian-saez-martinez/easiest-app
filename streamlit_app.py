import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")

# Streamlit app layout
st.title("🎈 My new app with Qwen model")
st.write("Let's start building a simple app with the Qwen model.")

# User input
user_input = st.text_input("Enter your text here:")

# Process input and generate output when text is provided
if user_input:
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Display the generated text
    st.write("Generated response:")
    st.write(generated_text)

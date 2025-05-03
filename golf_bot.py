
import streamlit as st
import openai
import os

st.set_page_config(page_title="Golf Club & Fitting Assistant", page_icon="⛳")
st.title("🏌️ Golf Club & Fitting Assistant")

# Get OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.warning("Please set the OPENAI_API_KEY environment variable to use this app.")
else:
    openai.api_key = api_key

    user_input = st.text_input("Ask me a golf gear or fitting question:")

    if user_input:
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a golf club fitting expert. Provide clear and helpful answers."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.markdown("### 🧠 Answer")
            st.write(response['choices'][0]['message']['content'])

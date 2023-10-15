import streamlit as st
import pandas as pd
from pandasai.llm import OpenAI
from pandasai import SmartDataframe
from dotenv import dotenv_values

key = dotenv_values(".env")
llm = OpenAI(api_token=key['OPENAPI_KEY'])

# App title
st.set_page_config(page_title="🏀💬 NBAGPT")

def load_data():
    data = pd.read_csv('./data/all_seasons.csv', index_col=0)
    df = SmartDataframe(data, config={"llm": llm})
    return df

def generate_response(prompt):
    res = df.chat(prompt)
    return res

st.title("🏀💬NBAGPT")
df = load_data()

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt:= st.chat_input("Enter in a question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(f"{prompt}")

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Looking up information..."):
            res = generate_response(prompt=prompt)
            st.markdown(res)
    message = {"role": "assistant", "content": res}
    st.session_state.messages.append(message)

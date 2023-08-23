from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import os
import sys
import constants
import streamlit as st
import streamlit as st
os.environ['OPENAI_API_KEY'] = constants.API_KEY

loader = TextLoader("./file.txt")
index = VectorstoreIndexCreator().from_loaders([loader])


st.session_state.messages = []
if not st.session_state.messages:
    st.session_state.messages.append({"role": "bot", "content": "Ask something..."})
else:
    for message in st.session_state.messages:
        with st.chat_message(message.get("role")):
            st.markdown(message.get("content"))

prompt = st.chat_input("Ask a question")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("bot"):
        st.write(index.query(prompt))
    st.session_state.messages.append({"role": "bot", "content": index.query(prompt)})
     

import streamlit as st
import requests

API_URL = "https://4cee-136-114-35-161.ngrok-free.app/summarize"
API_KEY = "secret123"

st.title("YouTube / Text Summarizer")

option = st.radio("Choose input type:", ["YouTube Link", "Text"])

if option == "YouTube Link":
    content = st.text_input("Paste YouTube URL")
    input_type = "youtube"
else:
    content = st.text_area("Paste text", height=300)
    input_type = "text"

if st.button("Summarize"):
    if not content:
        st.warning("Please provide input")
    else:
        with st.spinner("Summarizing..."):
            res = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {API_KEY}"},
                json={
                    "type": input_type,
                    "content": content
                }
            )

            if res.status_code == 200:
                st.success("Summary")
                st.write(res.json()["summary"])
            else:
                st.error(res.text)

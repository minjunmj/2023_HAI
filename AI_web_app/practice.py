from api.AI import AIAPI
import streamlit as st

def main():
    
    st.title("2023 HAI 여름방학 Web APP 개발 과제")

    st.subheader("Image to Text API 활용")
    query = st.file_uploader('Input Image')
    api = AIAPI()
    response = ""
    if query is not None:
        st.subheader("입력된 이미지")
        st.image(query)
        global respose
        response = api.query_image2text(query, key='image2text')
        st.markdown("결과")
        st.text(response)

    st.subheader("GPT API를 이용한 요약")
    if response:
        title, summarize = api.query_text2text(response)
        st.markdown("원문")
        st.text(response)
        st.markdown("결과")
        st.subheader(title)
        st.text(summarize)


if __name__ == '__main__':
    main()

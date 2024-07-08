import streamlit as st
import data.data as dd
import datetime
user_id = st.session_state.user_id
username = st.session_state.username
st.title("AI智能助手 👏")
st.subheader(f"欢迎{username}使用")
st.text("这是一个AI助手，可以回答你的任何问题，请尽情使用吧！")
role_user = "user"
role_assistant = "assistant"
list = dd.query_message_by_user_id(user_id=user_id)
if list:
    for msg in list:
        with st.chat_message(msg["role"]):
            st.write(msg["message"])
else:
    with st.chat_message("assistant"):
        st.write("我是你的私人智能AI助手，可以回答你的任何问题，请问你有什么问题？")

problem = st.chat_input("请输入你的问题")
if problem:
    with st.chat_message("user"):
        st.write(problem)
        datetime_user = datetime.datetime.now()
        dd.add_chat_message(user_id, problem,role_user,datetime_user)
    with st.chat_message("assistant"):
        reply = "祝你生活愉快"
        datetime_assistant = datetime.datetime.now()
        st.write(reply)
        dd.add_chat_message(user_id, reply,role_assistant,datetime_assistant)

col1, col2 = st.columns([1.0, 0.2])
with col1:
    st.empty()
with col2:
    if st.button("退出", key="exit_button"):
        st.write("成功退出！")
        st.switch_page("login.py")
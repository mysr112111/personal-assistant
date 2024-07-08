import streamlit as st
import data.data as dd
import time
st.set_page_config(
    page_title="私人助手登录页面",
    page_icon="🙂"
)

st.title("私人助手登录页面")
username = st.text_input("请输入用户名")
password = st.text_input("请输入密码",type="password")
st.markdown("---")
loginFlag = st.button("登录", key="login_button", help="点击登录按钮")
registerFlag = st.button("没有账号？点击注册", key="register_button", help="点击注册按钮")
st.write("")

feedback_area = st.empty()
def login(username, password):
    if username and password:
        result = dd.query_user_by_username(username)
        if result is None:
            feedback_area.error("用户不存在，请前往注册")
        else:
            if result["password"] == password:
                feedback_area.success("登录成功！")
                time.sleep(1)
                st.session_state.user_id = result["user_id"]
                st.session_state.username = result["username"]
                st.switch_page("pages/chatbot.py")
            else:
                feedback_area.error("用户存在，密码不正确！")
    else:
        feedback_area.error("请填写账号和密码！")



if loginFlag:
    login(username,password)

if registerFlag:
    st.switch_page("pages/register.py")
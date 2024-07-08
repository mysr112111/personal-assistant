import streamlit as st
import re
import data.data as dd
import time
st.set_page_config(
    page_title="私人助手注册页",
    page_icon="😀"
)
st.title("私人助手注册页 👏")
username = st.text_input("请输入手机号")
password = st.text_input("请输入密码",type="password")
repass = st.text_input("请再次输入密码",type="password")
registerFlag = st.button("注册")
loginFlag = st.button("已有账号？点击登录")

def register(username,password,repass):
    if username and password and repass:
        if re.match('^(13|15|17|18|19)[0-9]{9}$', username):
            if password == repass and len(password) >=8:
                if dd.query_user_by_username(username) is None:
                    dd.add_user(username,password)
                    st.success("注册成功")
                    time.sleep(2)
                    st.switch_page("login.py")
                else:
                    st.error("用户已注册，请勿重复注册！")
            else:
                st.error("两次密码不一致或者密码长度字段不足8位")
        else:
            st.error("手机号格式不正确")

    else:
        st.error("请务必填写相关注册信息")

if registerFlag:
    register(username, password, repass)

if loginFlag:
    st.switch_page("login.py")
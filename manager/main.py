
import streamlit as st
from loguru import logger

from authencation import login,logout,prelogin
from page import admin_page

def main():
    st.session_state.authenticated = False
    prelogin()
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'token' not in st.session_state:
        st.session_state.token = ''

    if not st.session_state.authenticated:
        login_container = st.container()
    
        with login_container:
            st.title("TEP 用户登录")
            hostname=st.text_input("主机名",value="http://localhost:8000/api/v1")
            passkey = st.text_input("密钥")
            if st.button("登录"):
                login(passkey,hostname)
    else:
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            st.title("登陆成功")
        with col3:
            if st.button("退出登录"):
                logout()
        admin_page()


if __name__ == "__main__":
    main()


import streamlit as st
import env
import jwt
from net import HTTP
from loguru import logger

def create_jwt(token:str,data:dict):
    auth_string = jwt.encode(data,token,algorithm="HS256")
    return auth_string

def parse_jwt(token:str)->dict:
    try:
        payload = jwt.decode(token,algorithms=["HS256"],options={"verify_signature": False})
        logger.debug(f"JWT has been parsed, {payload}")
    except Exception as e:
        logger.error(e)
    return payload

def logout():
    with open(env.TOKEN_FILE, "w") as file:
        file.write("")
    with open(env.USER_FILE, "w") as file:
        file.write("")
    st.session_state.authenticated = False
    st.session_state.token = ''
    st.session_state.username = ''
    st.rerun()

def load_user():
    try:
        with open(env.USER_FILE, "r") as file:
            data =file.read().strip()
            return data
    except FileNotFoundError:
        return None
def load_token():
    try:
        with open(env.TOKEN_FILE, "r") as file:
            data =file.read().strip()
            return data
    except FileNotFoundError:
        return None
def save_token(token:str):
    with open(env.TOKEN_FILE, "w") as file:
        file.write(token)
def save_user(username:str):
    with open(env.USER_FILE, "w") as file:
        file.write(username)
def login(passkey:str,hostname:str):
    if hostname:
        HTTP.update_baseurl(hostname)
    try:
        header = create_jwt(passkey,{"usr":"admin","uid":1,"per":["admin"]})
        HTTP.update_headers({"Authorization":"Bearer "+header})
        result = HTTP.get("/authencation")
        if result.status_code == 200:
            save_token(header)
            save_user(hostname)
            st.session_state.authenticated = True
            st.session_state.token = header
            st.rerun()
        else:
            st.session_state.authenticated = False
            st.error("无效的用户名或密码")
    except Exception as e:
        logger.error(e)
        st.error("登录请求失败,请检查API是否正常工作")

def prelogin():
    token = load_token()
    user = load_user()
    if token and user:
        HTTP.update_headers({"Authorization":"Bearer "+token})
        st.session_state.authenticated = True
        st.session_state.token = token
        st.session_state.user = user
    else:
        st.session_state.authenticated = False 

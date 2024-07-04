

from net import HTTP
import streamlit as st
import pandas as pd
from loguru import logger
# add pdfs
# get logs
# download files


def get_all_logs():
    resp = HTTP.get("/syslog")
    return resp.json()

def page():
    st.header("Book")
    st.subheader("Get all Logs")
    if st.button("Get all Logs"):
        all_log = get_all_logs()
        pd_table = pd.DataFrame(all_log,index=[idx for idx in range(1,len(all_log)+1)])
        st.write(pd_table)

    get_log_container = st.container()
    with get_log_container:
        st.subheader("Get Log by filename")
        filename = st.text_input(label="Filename")
        if st.button("Get Log by filename"):
            resp = HTTP.get(f"/syslog/{filename}")
            st.write(resp.json().get("log"))
            logger.info(resp.text)
    if st.button("get all files"):
        all_file = HTTP.get("/files").json()
        pd_table = pd.DataFrame(all_file,index=[idx for idx in range(1,len(all_file)+1)])
        st.write(pd_table)
    st.subheader("Create PDF")
    add_book_container = st.container()
    with add_book_container:
        file_contents=b''
        uploaded_file = st.file_uploader("请选择要上传的文件", type=["pdf"])
        if uploaded_file is not None:
            file_contents = uploaded_file.read()
        if st.button("Create PDF"):
            r = HTTP.upload_file("/pdf/upload",file_contents,uploaded_file.name)
            logger.info(r.text)
            if r.status_code == 200:
                img = r.json()["filename"]
                logger.info(img)
                st.write(img)
                st.success("Upload Success")
            else:
                st.error("Failed to upload image")


from pydantic import BaseModel
from net import HTTP
import streamlit as st
import pandas as pd
from loguru import logger
from datetime import datetime


def format_datetime(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-3]

"""
{
  "title": "string",
  "desc": "string",
  "content": "string",
  "img": "string",
  "link": "string",
  "datetime": "2024-07-02T15:05:15.761Z",
  "publish": "出版社官方",
  "expire_time": "2024-07-02T15:05:15.761Z"
}
"""
class NoteSchema(BaseModel):
    title:str
    desc:str
    content:str
    img:str
    link:str
    datetime:str
    publish:str
    expire_time:str



# CURD user

def get_all_notes():
    resp = HTTP.get("/notification")
    return resp.json()
def delete_user():
    ...
    # not going to impl
def update_user():
    ...
    # not going to impl

def delete_note(bookid:int):
    resp = HTTP.api_delete(f"/notification/{bookid}")
    return resp.json()

def page():
    st.header("Book")
    st.subheader("Get all notes")
    if st.button("Get all notes"):
        all_note = get_all_notes()
        pd_table = pd.DataFrame(all_note,index=[idx for idx in range(1,len(all_note)+1)])
        st.write(pd_table)
    st.subheader("Delete note by ID")
    note_id = st.number_input(label="Note ID",step=1)
    if st.button("Delete this Book"):
        delete_note(note_id)
    st.subheader("Get current user info")

    st.subheader("Create note")
    add_book_container = st.container()
    with add_book_container:
        title = st.text_input(label="Title")
        desc = st.text_input(label="Description")
        content = st.text_input(label="Content")
        link = st.text_input(label="Link")
        publish = st.text_input(label="publish")
        publish_time = st.date_input(label="Publish time",value=datetime.now())
        # 创建一个文件上传组件
        file_contents=b''
        uploaded_file = st.file_uploader("请选择要上传的文件", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            file_contents = uploaded_file.read()
            st.image(file_contents)
        if st.button("Create Book"):
            r = HTTP.upload_file("/image/upload",file_contents,uploaded_file.name)
            logger.info(r.text)
            if r.status_code == 200:
                img = r.json()["filename"]
                logger.info(img)
                bookSchema = NoteSchema(title=title,desc=desc,content=content,img=img,link=link,publish=publish,datetime=format_datetime(publish_time),expire_time=format_datetime(publish_time))
                resp = HTTP.json_post("/notification", bookSchema.model_dump())
                if resp.status_code == 200:
                    st.toast("Book created successfully")
            else:
                st.error("Failed to upload image")
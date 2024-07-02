

from pydantic import BaseModel
from net import HTTP
import streamlit as st
import pandas as pd
from loguru import logger
class BookSchema(BaseModel):
    title:str
    author:str
    desc:str
    content:str
    img:str
    link:str
    group:str

# CURD user

def get_all_books():
    resp = HTTP.get("/book")
    return resp.json()
def delete_user():
    ...
    # not going to impl


def delete_book(bookid:int):
    resp = HTTP.api_delete(f"/book/{bookid}")
    return resp.json()

def page():
    st.header("Book")
    st.subheader("Get all books")
    if st.button("Get all books"):
        all_books = get_all_books()
        pd_table = pd.DataFrame(all_books,index=[idx for idx in range(1,len(all_books)+1)])
        st.write(pd_table)
    st.subheader("Delete Book by ID")
    book_id = st.number_input(label="Book ID",step=1)
    if st.button("Delete this Book"):
        delete_book(book_id)
    st.subheader("Get current user info")

    st.subheader("Create Book")
    add_book_container = st.container()
    with add_book_container:
        title = st.text_input(label="Title")
        author = st.text_input(label="Author")
        desc = st.text_input(label="Description")
        content = st.text_input(label="Content")
        link = st.text_input(label="Link")
        group = st.text_input(label="Group")
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
                bookSchema = BookSchema(title=title,author=author,desc=desc,content=content,img=img,link=link,group=group)
                resp = HTTP.json_post("/book", bookSchema.model_dump())
                if resp.status_code == 200:
                    st.toast("Book created successfully")
            else:
                st.error("Failed to upload image")


import streamlit as st
from subitem import inline_book,inline_note,inline_resource,inline_system
def admin_page():
    side_modules = [
        "主界面",
        "书籍管理",
        "公告管理",
        "资源管理",
        "系统状态",
    ]
    option = st.sidebar.radio("导航", tuple(side_modules))
    if option == "主界面":
            # 标题 + 介绍
            st.title("TEP后台管理系统")
            st.markdown("""
                ## 介绍
            """)
    elif option == "书籍管理":  
        inline_book.page()
    elif option == "公告管理":
        inline_note.page()
    elif option == "资源管理":
        inline_resource.page()
    else:
        st.write("系统状态")
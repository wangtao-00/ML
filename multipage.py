# -*- coding: utf-8 -*-
# @Time : 2023/12/19 20:27
# @Author : wangtao
# @Email : wngtaow@outlook.com
# @File :multipage.py
import streamlit as st

class MultiPage:
    def __init__(self):
        self.pages = []

    def add_page(self,title,func):
        self.pages.append(
            {
                "title":title,
                "function":func
            }
        )

    def run(self):
        page = st.sidebar.selectbox(
            "App navigation",
            self.pages,
            format_func=lambda page: page["title"]
        )
        page["function"]()
# -*- coding: utf-8 -*-
# @Time : 2023/12/19 19:41
# @Author : wangtao
# @Email : wngtaow@outlook.com
# @File :home.py

import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_metrics import metric_row


def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def app():
    load_css('style/style.css')
    load_coding = load_lottie('https://lottie.host/de5c0597-bf96-4539-8506-fa08341c2780/B2T72Flctp.json')
    img_sphere = Image.open('image/sphere.jpg')
    img_nano = Image.open('image/nano.jpg')

    # part 1
    with st.container():
        st.subheader("Hi, this is snake:snake:")
        st.title('aaaaaa')
        st.write("I love making abstract cube animations, it's even more fun when there is more than one cube. ")
        st.write('[More........]https://app.lottiefiles.com/')

    # part 2
    with st.container():
        st.write("-----")
        l_column,r_column = st.columns(2)
        with l_column:
            st.header("what i do ")
            st.write('########')
            st.write("""
            If you use my animations in your product or if you need to contact me please 
            - feel free to email me at isionresources@gmail.com or chat with me on Instagram 
            - at isionindustries
            """)
        with r_column:
            st_lottie(load_coding,height=200,key='coding')
    # part 3
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_sphere)
        with text_column:
            st.subheader("The explosion ball")
            st.write(
                """
                Learn how to model a explosion ball!
                In this tutorial, I'll show you exactly how to do it
                """
            )
    # nano
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_nano)
        with text_column:
            st.subheader("Nano Sphere")
            st.write(
                """
                Discover how to make a visually appealing Nano Sphere!
                In this tutorial, I'll show you exactly how to do it.
                """
            )
        # ---- CONTACT ----
    with st.container():
        with st.form("my_form", clear_on_submit=False):
            name = st.text_input("请输入用户名")
            passwd = st.text_input("请输入密码", type="password")
            passwd_re = st.text_input("请再次输入密码", type="password")
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("欢迎用户 {}".format(name))






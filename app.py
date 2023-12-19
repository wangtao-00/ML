# -*- coding: utf-8 -*-
# @Time : 2023/12/19 19:26
# @Author : wangtao
# @Email : wngtaow@outlook.com
# @File :app.py.py

import streamlit as st
from multipage import MultiPage
from Pages import home, machine_leaning

st.set_page_config(page_title="ML", page_icon=":tiger:", layout="wide")
st.title('Machine Learning Application')

app = MultiPage()

# add applications
app.add_page('Home', home.app)
app.add_page('Machine Learning', machine_leaning.app)

# Run application
if __name__ == '__main__':
    app.run()
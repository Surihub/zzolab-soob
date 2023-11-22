import streamlit as st
# import [폴더명].[파일명] as [별칭]
# import mymodule.module1 as mm

# from mymodule.module1 import greeting, chat
from mymodule.module1 import *

st.title("Hello module!")
name = st.text_input("이름을 입력해주세요!!!!!")
greeting(name)
chat(name)


# key = st.secrets['datagokr']['key']
# st.title(key)
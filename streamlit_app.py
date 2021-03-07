# -*- coding: utf-8 -*-

import streamlit as st

# Streamlit encourages well-structured code, like starting execution in a main() function.
def main():
    print('hello world')
    st.markdown('# 一级标题')
    st.markdown('**粗体**')
    st.markdown('*斜体*')
    st.markdown('~~删除~~')

if __name__ == "__main__":
    main()

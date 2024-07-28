import streamlit as st
import pandas as pd

if __name__ == '__main__':
    st.title('Hello World')
    st.write('This is a test')
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))
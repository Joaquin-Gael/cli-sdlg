import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from components.models.user import User
from components.API import GET

if __name__ == '__main__':
    responce = GET.users(url='http://127.0.0.1:8000/API/users/')
    with st.sidebar:
        st.title('Hospital SDLG :blue[CLI]')
        if responce is not None:
            st.success('This is a success data!', icon="✅")
        else:
            st.error('This is an error', icon="🚨")
    st.header('Users Table')
    st.table(
        User.data_frame_users(
            users_obj=[User.validate_user(user_data) for user_data in responce]
        )
    )
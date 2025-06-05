import os
import streamlit as st

st.set_page_config(page_title="KMD IoT Platform", page_icon="🧊", layout="wide", initial_sidebar_state="expanded", menu_items={"Grafana": "https://grafana.dev.context.kmd.dk"})

st.title("KMD IoT Platform management utils")

if st.user.is_logged_in:
    st.table(st.user)

st.dataframe(os.environ.items())

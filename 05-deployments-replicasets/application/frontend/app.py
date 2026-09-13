import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="CKAD App", page_icon="☸️")
st.title("CKAD App")
st.caption(f"API: `{API_URL}`")
st.divider()

st.subheader("Health")

if st.button("Verificar"):
    try:
        r = requests.get(f"{API_URL}/health", timeout=5)
        data = r.json()
        if data.get("status") == "ok":
            st.success("ok :)")
        else:
            st.error("falhou :(")
        st.json(data)
    except Exception as e:
        st.error(f"Sem conexão: {e}")

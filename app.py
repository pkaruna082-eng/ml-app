import streamlit as st

# App Title
st.title("Single Person Information App")

# Input
st.subheader("Enter Person Details")
name = st.text_input("Enter your name:")

# Output
if st.button("Submit"):
    if name.strip():
        st.success("Information submitted successfully!")
        st.write("Name:", name)
    else:
        st.warning("Please enter your name.")

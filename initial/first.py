import streamlit as st
st.title("HELLO World")
st.write("hello")
st.header("hiiii")
st.write("Python language")
st.header("this is header")
st.subheader("this is subheader")
st.text_input("Enter ur name:")
st.number_input("Enter ur age:")
st.text_area("Enter ur address:")
st.slider("select your age:",0,100)
st.checkbox("I Agree")
options=st.selectbox("Select any option",["opt1","opt2","opt3"])
st.write("You selected",options)
st.radio("Select ur gender",["M","F","Other"])
st.sidebar.title("SIDEBAR TITLE")
st.sidebar.write("This is sidebar ")
st.sidebar.text_input("Enter your email")
st.sidebar.selectbox("select ur country",["India","US","China"])





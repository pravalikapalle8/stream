import streamlit as st
import pandas as pd 
import time

st.set_page_config(page_title="Student Dashboard")
tab1,tab2=st.tabs(["form","info"])
with tab1:
    st.header("Student form")
    name=st.text_input("Name")
    age=st.number_input("Age",1,100)
    course = st.selectbox("Course",["python","java","SQL"])
    lan=st.multiselect("know_language",["Telugu","English","Hindi","Malayalam","French"])
    date=st.date_input("Date")
    
    checkbox=st.checkbox("I Agree!")
    if st.button("Submit"):
        if checkbox:
          
            st.success("Submitted Successfully")
            st.write(name)
            st.write(age)
            st.write(course)
            st.write(lan)
            st.write(date)
            st.balloons()
            
        else:
            st.warning("please check the checkbox")

with tab2:
    st.header("Upload a file")
    file=st.file_uploader("Choose a file",type=["csv"])
    if file is not None:
        df=pd.read_csv(file)
        st.success("file uploaded")
        st.write("Student Data")
        st.dataframe(df)
        st.write("Summary")
        c1,c2,c3=st.columns(3)
        c1.metric("Rows",df.shape[0])
        c2.metric("Columns",df.shape[1])
        with st.expander("see only column names"):
            st.write(df.columns)
        if st.button("Process"):
            p=st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                p.progress(i+1)
            st.toast("processed")
        with st.spinner("loading... "):
            time.sleep(10)
            st.write("completed.")
            st.write("ThankYou!")
            st.snow()

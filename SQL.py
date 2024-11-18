import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
import sqlite3
import google.generativeai as genai


api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("API Key not found! Check your .env file or environment setup.")

genai.configure(api_key=api_key)


def get_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

def query(sql, db):
    conn = sqlite3.connect(db) 
    cur = conn.cursor() 
    cur.execute(sql) 
    rows = cur.fetchall() 
    conn.commit()
    conn.close()
    return rows


# Define your prompt    
prompt = ['''You are an expert in converting English questions to SQL query! The SQL database has the name STUDENT and has the following columns - NAME, CLASS, ROLLNO \n\nFor example,\nExample 1 - How many entries of records are present?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ; \nExample 2 - Tell me all the students studying in Data Science class?, the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science"; also the sql code should not have ``` in beginning or end and sql word in output''']
# Streamlit setup
st.set_page_config(page_title="Retrieve SQL Data")
st.header("SQL Retriever")
question = st.text_input("Input your SQL query condition:", key="input")
submit = st.button("Submit")

if submit:
    sql_query = get_response(question, prompt)
    rows = query(sql_query, "student.db")
    st.subheader("Query Result:")
    for row in rows:
        st.text(" ".join(row))

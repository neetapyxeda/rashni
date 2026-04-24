import streamlit as st

st.write("Hello Welcome!!!")
num = int(st.text_input("Enter your favorite number:"))
if num%2 == 0:
  st.write("It's even number")
else:
  st.write("It's an odd number")

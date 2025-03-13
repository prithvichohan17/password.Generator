import re
import streamlit as st 

#page styling
st.set_page_config(page_title="Password strenlit Checter By Mehak Alamgir",page_icon="🌘",layout="centered")
st.markdown(""" 
<style>
    .main{text-align:center;}
    .st.TextInput {width:60% !important; margin:auto;}
    .stButton button{width: 50%; background-color#4CAF50; color:white; font-size: 18px;}
    .stButton button:hover{backgound-color:#45a049;}
</style>
    """,unsafe_allow_html=True)
# page title and decription
st.title("🔐password Strength Generator")
st.write("Enter your password below to check its  secrity level.🔍")

# function to check password strength
def chect_password_strength(password):
    score =0
    feedback =[]

    if len(password) >=8:
        score +=1 #increased score by 1
    else:
        feedback.append("❌password should be **atleast 8 character long**.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]",password): 
        score +=1
    else:
        feedback.append("❌password should be **both upper case (A-Z)and lower case (a-z) letters**.")
    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("❌password should be **at least one numder (0-9)**.")

# special characters
    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")
    #  display password strangth results
    if score == 4:
        st.success("✅ **Strong password**Your password is secure.")
    elif score ==3:
        st.info("⚠️**Moderate Password** - consider imporving security by adding more feature")
    else:
        st.error("❌**week Password** - Follow the suggestion below to strength it. ")
    if feedback:
        with st.expander("🔍**Impove Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password",type="password",help= "Ensure your password is strong🔐")

# Button working
if st.button("check strength"):
    if password:
        chect_password_strength(password)
    else:
        st.warning("please enter a password frist!")
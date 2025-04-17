import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker By Musaarrat Huma", page_icon=":🌘:", layout="centered")
#custom css
st.markdown("""
<style>
        .main {text-align: center;}
        .stTextInput {width: 60% !important; margin: auto; }
        .stButton>button {
            background: linear-gradient(45deg, #81b3e1, #b8a6eb);
            color: white;
            font-size: 25px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
            box-shadow: 0px 5px 15px rgba(0, 201, 225, 0.4);
            text-align: center;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background: linear-gradient(45deg, #92fe9d, #00c9ff);
            color: black;
        }   
            .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 10px;
            color: #2c2c54 !important;
        }
</style>                
""", unsafe_allow_html=True)
#page title and description
st.title("🔐Password Strength Checker")
st.write("Check the strength of your password and get tips to make it stronger and also check its security level.🔍")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should contain both uppercase and lowercase letters.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one number.")

#special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1  
    else:
        feedback.append("❌Password should contain at least one special character.") 

#display password strength results
    if score == 4:
        st.success("✅ **Strong Password** Your password is strong!")            
    elif score == 3:
        st.info("⚠️ **Moderate Password** Your password is moderate. Consider adding more complexity.")
    else:
        st.warning("❗ **Weak Password** - Follow the suggestion below to strength it.")

#display feedback
    if feedback:
        with st.expander("🔍**Improve Your Password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong and secure 🔐")

#Button Working
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("❗Please enter a password to check its strength.") #show warning if password is empty
                        
st.markdown("<div class='footer'> Password Strength Checker By Musaarrat Huma </div>", unsafe_allow_html=True)

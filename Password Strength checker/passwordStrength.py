import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker")

st.title("🔐 Password Strength Checker")
st.write("Check how strong and secure your password is.")

password = st.text_input("Enter your password", type="password")

# ---------- checker function ----------

def analyze_password(pw):
    score = 0
    feedback = []

    # Length check
    if len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
        feedback.append("Increase length to at least 12 characters")
    else:
        feedback.append("Password too short (minimum 8 characters)")

    # Uppercase
    if re.search(r"[A-Z]", pw):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", pw):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Numbers
    if re.search(r"\d", pw):
        score += 1
    else:
        feedback.append("Add numbers")

    # Symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
        score += 1
    else:
        feedback.append("Add special symbols")

    # Common patterns
    common = ["password", "1234", "admin", "qwerty"]
    for word in common:
        if word in pw.lower():
            feedback.append("Avoid common words/patterns")
            score -= 1
            break

    return score, feedback


# ---------- UI output ----------

if password:

    score, feedback = analyze_password(password)

    st.subheader("Result")

    # strength label
    if score <= 2:
        st.error("❌ Weak Password")
        st.progress(20)

    elif score <= 4:
        st.warning("⚠️ Medium Password")
        st.progress(55)

    else:
        st.success("✅ Strong Password")
        st.progress(90)

    st.write("Strength Score:", score, "/ 6")

    if feedback:
        st.subheader("🔎 Suggestions to Improve")
        for item in feedback:
            st.write("•", item)
    else:
        st.success("No major weaknesses detected 👍")

else:
    st.info("Enter a password to begin analysis")

# ---------- footer ----------

st.divider()
st.caption("Educational tool — checks rule-based password strength only.")

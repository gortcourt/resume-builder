import streamlit as st
from fpdf import FPDF

st.title("Resume Builder")

# Form inputs
name = st.text_input("Full Name")
email = st.text_input("Email")
education = st.text_area("Education")
experience = st.text_area("Work Experience")
skills = st.text_area("Skills")

def sanitize_text(text):
    # Replace common problematic Unicode characters with ASCII-safe ones
    if text:
        return text.replace("•", "-").replace("–", "-").replace("—", "-")
    return ""

if st.button("Generate Resume"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Sanitize user input
    name = sanitize_text(name)
    email = sanitize_text(email)
    education = sanitize_text(education)
    experience = sanitize_text(experience)
    skills = sanitize_text(skills)

    pdf.cell(200, 10, txt=name, ln=True)
    pdf.cell(200, 10, txt=email, ln=True)
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt="Education:\n" + education)
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt="Experience:\n" + experience)
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt="Skills:\n" + skills)

    pdf.output("resume.pdf")
    with open("resume.pdf", "rb") as f:
        st.download_button("Download Resume", f, file_name="resume.pdf")
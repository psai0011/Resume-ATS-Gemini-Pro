from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import io
import base64
import fitz  # PyMuPDF instead of pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    # Using PyMuPDF instead of pdf2image to avoid Poppler dependency
    pdf_bytes = uploaded_file.read()
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    first_page = pdf_document.load_page(0)
    
    # Convert to image
    pix = first_page.get_pixmap()
    img_bytes = pix.tobytes("jpeg")
    
    pdf_parts = [
        {
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_bytes).decode()
        }
    ]
    return pdf_parts

## streamlit app
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description", key="input")
uploaded_file = st.file_uploader("Upload resume (PDF)...", type=['pdf'])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell me About The Resume")
submit2 = st.button("How Can I Improvise my Skills")
submit3 = st.button("Percentage Match")

input_prompt1 = """You are an experienced HR with Tech Experience in the field of any one job role from Data Science, Full Stack, MLOps Engineer, AI Engineer, Big Data Engineer, Data Analyst, Web Development, DevOps, DBA. Your task is to review the provided resume against the job description. Please share the professional evaluation on whether the candidate's profile aligns with the job requirements. Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements."""

input_prompt2 = """You are a skilled career advisor with expertise in Data Science, Full Stack, MLOps Engineering, AI Engineering, Big Data Engineering, Data Analysis, Web Development, DevOps, and Database Administration. Based on the resume and job description provided, suggest specific skills and areas the candidate should improve to better match the job requirements and advance in their career path."""

input_prompt3 = """You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of any job role from Data Science, Full Stack, MLOps Engineer, AI Engineer, Big Data Engineer, Data Analyst, Web Development, DevOps, DBA and Deep ATS functionality. Your task is to evaluate the resume against the provided job description. Give me the percentage of the match if the resume matches job description. First the output should come as percentage and then keywords missing and last final thoughts."""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.header("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.header("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.header("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
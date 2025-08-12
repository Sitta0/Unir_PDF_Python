import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO

st.title("Juntar PDFs Fácil")

uploaded_files = st.file_uploader(
    "Selecione os arquivos PDF na ordem desejada",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("Juntar PDFs"):
        merger = PdfMerger()
        for uploaded_file in uploaded_files:
            merger.append(uploaded_file)
        
        output = BytesIO()
        merger.write(output)
        merger.close()
        output.seek(0)

        st.download_button(
            label="Download do PDF unido",
            data=output,
            file_name="pdf_unido.pdf",
            mime="application/pdf"
        )

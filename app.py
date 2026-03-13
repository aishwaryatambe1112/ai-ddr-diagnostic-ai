import streamlit as st

from src.extractor import extract_text
from src.image_extractor import extract_images
from src.chunker import chunk_text
from src.vector_store import create_vector_store
from src.ddr_writer import generate_ddr
from src.pdf_writer import generate_pdf

st.title("AI DDR Inspection System")

inspection = st.file_uploader("Upload Inspection Report")

thermal = st.file_uploader("Upload Thermal Report")

if st.button("Generate Report"):

    with open("inspection.pdf","wb") as f:
        f.write(inspection.read())

    with open("thermal.pdf","wb") as f:
        f.write(thermal.read())

    text1 = extract_text("inspection.pdf")
    text2 = extract_text("thermal.pdf")

    combined = text1 + text2

    chunks = chunk_text(combined)

    index, embeddings = create_vector_store(chunks)

    report = generate_ddr(combined)

    st.subheader("Generated DDR")

    st.write(report)

    generate_pdf(report,"output/report.pdf")

    with open("output/report.pdf","rb") as f:

        st.download_button(
            "Download PDF Report",
            f,
            "DDR_Report.pdf"
        )

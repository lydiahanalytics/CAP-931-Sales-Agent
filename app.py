import streamlit as st

from pypdf import PdfReader

from dotenv import load_dotenv
from agents import (
    company_research_agent,
    competitor_agent,
    leadership_agent,
    sales_strategy_agent,
    report_agent,
)

load_dotenv()

def extract_uploaded_file(uploaded_file):
    if uploaded_file is None:
        return ""

    try:
        if uploaded_file.type == "application/pdf":
            reader = PdfReader(uploaded_file)
            text = ""

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

            return text[:12000]

        elif uploaded_file.type == "text/plain":
            return uploaded_file.getvalue().decode(
                "utf-8",
                errors="ignore"
            )[:12000]

    except Exception as error:
        st.warning(f"Could not read uploaded file: {error}")

    return ""

st.set_page_config(
    page_title="CAP 931 Sales Assistant Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Sales Assistant Agent")
st.write(
    "Enter information about your product and prospective customer "
    "to generate strategic sales insights."
)

st.subheader("Sales Opportunity Information")

product_name = st.text_input(
    "Product Name",
    value="AI-Powered Talent Acquisition Platform"
)

company_url = st.text_input(
    "Prospective Company URL",
    value="https://www.microsoft.com"
)

product_category = st.text_input(
    "Product Category",
    value="AI Recruiting & Talent Analytics"
)

competitors = st.text_area(
    "Competitor URLs or Names",
    value="Workday\nOracle"
)

value_proposition = st.text_area(
    "Value Proposition",
    value=(
        "An AI-powered recruiting platform that helps enterprises "
        "identify qualified candidates faster, automate repetitive "
        "recruiting tasks, and use talent analytics to improve "
        "hiring decisions."
    )
)

target_customer = st.text_input(
    "Target Customer",
    value="Chief Human Resources Officer / Head of Talent Acquisition"
)

uploaded_file = st.file_uploader(
    "Optional: Upload Product Overview",
    type=["pdf", "txt"]
)

st.divider()

if st.button("Generate Sales Insights", type="primary"):

    required_fields = {
        "Product Name": product_name,
        "Prospective Company URL": company_url,
        "Product Category": product_category,
        "Competitors": competitors,
        "Value Proposition": value_proposition,
        "Target Customer": target_customer,
    }

    missing_fields = [
        field_name
        for field_name, field_value in required_fields.items()
        if not field_value.strip()
    ]

    if missing_fields:
        st.error(
            "Please complete the following required fields: "
            + ", ".join(missing_fields)
        )
        st.stop()

    product_document = extract_uploaded_file(uploaded_file)

    context = f"""
Product Name: {product_name}
Company URL: {company_url}
Product Category: {product_category}
Competitors: {competitors}
Value Proposition: {value_proposition}
Target Customer: {target_customer}

Product Document Information:
{product_document if product_document else "No product document uploaded."}
"""

    with st.spinner("Company Research Agent is working..."):
        company_result = company_research_agent(context)

    with st.spinner("Competitor Intelligence Agent is working..."):
        competitor_result = competitor_agent(context)

    with st.spinner("Leadership Research Agent is working..."):
        leadership_result = leadership_agent(context)

    with st.spinner("Sales Strategy Agent is working..."):
        sales_strategy_result = sales_strategy_agent(context)

    with st.spinner("Executive Report Agent is preparing the final brief..."):
        final_report = report_agent(
            company_result,
            competitor_result,
            leadership_result,
            sales_strategy_result,
            context
        )

    st.success("Sales intelligence analysis complete.")

    st.subheader("Executive Sales Intelligence Brief")
    st.markdown(final_report)

    with st.expander("View Company Research Agent Output"):
        st.markdown(company_result)

    with st.expander("View Competitor Agent Output"):
        st.markdown(competitor_result)

    with st.expander("View Leadership Agent Output"):
        st.markdown(leadership_result)

    with st.expander("View Sales Strategy Agent Output"):
        st.markdown(sales_strategy_result)
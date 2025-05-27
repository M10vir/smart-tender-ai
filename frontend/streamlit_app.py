import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Smart Tender AI", layout="centered")

st.title("📑 Smart Tender AI – Admin Console")

menu = st.sidebar.radio("Choose Function", ["Generate RFP", "Estimate Budget", "Score Vendor Proposal"])

# ------------------- RFP Generator -------------------
if menu == "Generate RFP":
    st.header("📝 Generate Request for Proposal (RFP)")
    title = st.text_input("Tender Title")
    objectives = st.text_area("Project Objectives", height=200)

    if st.button("Generate RFP"):
        if not title or not objectives:
            st.warning("Please fill both fields.")
        else:
            response = requests.post(f"{API_URL}/generate-rfp", json={
                "tender_title": title,
                "project_objectives": objectives
            })
            if response.status_code == 200:
                st.success("✅ RFP Generated")
                st.text_area("Generated RFP", response.json()["generated_rfp"], height=400)
            else:
                st.error("Error: " + response.json()["detail"])

# ------------------- Budget Estimator -------------------
elif menu == "Estimate Budget":
    st.header("💰 Budget Estimation")

    project_title = st.text_input("Project Title")
    items = []
    with st.form("budget_form"):
        for i in range(5):
            item = st.text_input(f"Item {i+1} Name", key=f"item_{i}")
            quantity = st.number_input(f"Item {i+1} Quantity", min_value=0, step=1, key=f"qty_{i}")
            if item:
                items.append({"item": item, "quantity": quantity})
        submitted = st.form_submit_button("Estimate Budget")
    
    if submitted and project_title and items:
        response = requests.post(f"{API_URL}/estimate-budget", json={
            "project_title": project_title,
            "items": items
        })
        if response.status_code == 200:
            st.success("✅ Budget Estimate")
            st.text_area("Estimated Budget", response.json()["budget_estimate"], height=300)
        else:
            st.error("Error: " + response.json()["detail"])

# ------------------- Vendor Scoring -------------------
elif menu == "Score Vendor Proposal":
    st.header("📤 Upload Proposal for Scoring")
    uploaded_file = st.file_uploader("Upload DOCX file", type=["docx"])

    if st.button("Score Proposal") and uploaded_file:
        files = {"file": (uploaded_file.name, uploaded_file, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")}
        response = requests.post(f"{API_URL}/score-vendor", files=files)
        if response.status_code == 200:
            st.success("✅ Vendor Score")
            st.text_area("Score Report", response.json()["score_report"], height=400)
        else:
            st.error("Error: " + response.json()["detail"])

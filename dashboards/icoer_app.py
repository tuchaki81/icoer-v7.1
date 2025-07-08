import streamlit as st
import pandas as pd
import json
from src.icoer_calc import compute_icoer

st.set_page_config(page_title="ICOER v7.1", layout="centered")
st.title("🧠 ICOER v7.1 Dashboard")
st.markdown("Compute and visualize Informational Coherence from symbolic, EEG, and temporal data.")

# --- File Upload ---
st.sidebar.header("Upload Inputs")
text_file = st.sidebar.file_uploader("Upload JSON Text File", type=["json"])
eeg_file = st.sidebar.file_uploader("Upload EEG CSV File", type=["csv"])

if text_file and eeg_file:
    # Save temporary files
    with open("temp_text.json", "wb") as f:
        f.write(text_file.read())
    with open("temp_eeg.csv", "wb") as f:
        f.write(eeg_file.read())

    # Compute ICOER
    result = compute_icoer("temp_text.json", "temp_eeg.csv")
    S = round(result['S'], 3)
    B = round(result['B'], 3)
    T = round(result['T'], 3)
    H = round(result['H'], 3)
    ICOER = round(result['ICOER'], 3)

    # --- Display results ---
    st.subheader("🔍 Results")
    st.metric("S (Symbolic Coherence)", S)
    st.metric("B (Biological Coherence)", B)
    st.metric("T (Temporal Sync)", T)
    st.metric("H (Informational Entropy)", H)
    st.metric("🧮 ICOER", ICOER)

    # --- Bar Chart ---
    st.subheader("📊 Component Breakdown")
    df = pd.DataFrame({
        "Component": ["S", "B", "T", "H", "ICOER"],
        "Value": [S, B, T, H, ICOER]
    })
    st.bar_chart(data=df.set_index("Component"))

else:
    st.warning("Upload both a text file (.json) and EEG file (.csv) to begin analysis.")

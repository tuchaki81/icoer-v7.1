import streamlit as st
import json
from src.icoer_calc import compute_icoer

st.set_page_config(page_title="ICOER v7.1 App", layout="centered")
st.title("🧠 ICOER v7.1 — Informational Coherence Index")

# Carrega o sample_texts.json
with open("data/sample_texts.json", "r", encoding="utf-8") as f:
    samples = json.load(f)

# Lista de opções de texto
sample_keys = list(samples.keys())
selected_key = st.selectbox("📄 Escolha um exemplo de texto:", sample_keys)
selected_text = samples[selected_key]

st.markdown(f"**Texto Selecionado:**\n\n_{selected_text['text']}_")

# Exibir botão para calcular
if st.button("🔍 Calcular ICOER"):
    # Simula os caminhos dos arquivos
    text_path = "data/sample_texts.json"
    eeg_path = "data/simulated_eeg.csv"

    # Executa o cálculo
    result = compute_icoer(text_path, eeg_path)

    st.success("✅ Cálculo concluído!")
    st.subheader("📊 Resultados dos Módulos")

    # Visualização dos módulos
    st.metric("🧠 S — Texto (SLECMA)", f"{result['S']:.3f}")
    st.metric("🧬 B — Biológico (EEG)", f"{result['B']:.3f}")
    st.metric("⏱️ T — Temporal", f"{result['T']:.3f}")
    st.metric("🌀 H — Entropia Informacional", f"{result['H']:.3f}")
    st.markdown("---")
    st.metric("🧩 ICOER v7.1", f"{result['ICOER']:.3f}")

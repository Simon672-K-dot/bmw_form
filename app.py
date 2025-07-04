
import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="BMW Arbeitsanweisung", layout="wide")

# --- Passwortschutz ---
PASSWORD = "bmw2025"
pw_input = st.text_input("🔐 Passwort eingeben:", type="password")
if pw_input != PASSWORD:
    st.warning("🔒 Zugang nur mit gültigem Passwort.")
    st.stop()

# --- Titel & Kopfbereich ---
st.markdown('<h1 style="text-align:center;">📄 Arbeitsanweisung</h1>', unsafe_allow_html=True)

col_top1, col_top2 = st.columns(2)
with col_top1:
    sortierstart = st.date_input("📆 Sortierstart")
    st.write("DEBUG - Sortierstart:", sortierstart)
with col_top2:
    freigabe = st.text_input("📌 Freigabe")

# Unterhalb von Freigabe: drei IDs nebeneinander
col_ids1, col_ids2, col_ids3 = st.columns(3)
with col_ids1:
    auftrag_bbw = st.text_input("🧾 Auftrags-ID BBW")
with col_ids2:
    auftrag_bmw = st.text_input("🧾 Auftrags-ID BMW")
with col_ids3:
    kritischster_bi = st.selectbox("📊 Kritischster BI", list(range(1, 11)))

st.markdown("---")

# --- Drei Spalten ab Zeile 3 ---
st.markdown('<h3 style="background-color:#e8e8e8;padding:10px;">📋 Prüf- & Teildaten</h3>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    pruefumfang = st.text_input("📄 Prüfumfang")
    taetigkeit = st.text_input("🛠️ Tätigkeit")
    fehlerbild_a = st.text_input("❌ Fehlerbild A")
    fehlerbild_d = st.text_input("❌ Fehlerbild D")
    motorentyp = st.text_input("🚗 FZG / Motorentyp")
    ansprechpartner_bbw = st.text_input("👷 Ansprechpartner BBW")
    pruefort = st.text_input("🏭 Sortier-/Prüfort")

with col2:
    lieferant = st.text_input("🚚 Lieferant")
    fehlerbild_b = st.text_input("❌ Fehlerbild B")
    fehlerbild_e = st.text_input("❌ Fehlerbild E")
    verbautakt = st.text_input("⚙️ Verbaukontakt")
    tagesbedarf = st.text_input("📦 Tagesbedarf")
    ansprechpartner_kunde = st.text_input("👤 Ansprechpartner Kunde")
    arbeitsorte = st.text_input("📍 Arbeitsort(e)")

with col3:
    fehlerbild_c = st.text_input("❌ Fehlerbild C")
    fehlerbild_f = st.text_input("❌ Fehlerbild F")
    abteilung_bmw = st.text_input("🏷️ Abteilung BMW")
    sortierregel = st.text_input("📑 Sortierregel")

st.markdown("---")

# --- I.O. Markierung & PSA Bereich ---
st.markdown('<h3 style="background-color:#dff0d8;padding:10px;">✅ I.O. Markierung</h3>', unsafe_allow_html=True)
io_markierung = st.text_input("Markierung gemäß Vorgabe")

st.markdown('<h3 style="background-color:#d9edf7;padding:10px;">🧤 PSA</h3>', unsafe_allow_html=True)
psa = st.text_input("Persönliche Schutzausrüstung (z.B. Brille, Handschuhe)")
handschuhe = st.text_input("Handschuhe")
zusaetzliche_standards = st.text_input("Zusätzliche Standards")

# --- COP / ESD / Prüfablauf + Bild nebeneinander ---
st.markdown('<h3 style="background-color:#fcf8e3;padding:10px;">⚙️ COP / ESD / Prüfablauf</h3>', unsafe_allow_html=True)
col_a, col_b, col_c = st.columns([1,1,1])
with col_a:
    cop = st.selectbox("COP-relevant", ["Ja", "Nein"])
    esd = st.selectbox("ESD-relevant", ["Ja", "Nein"])
    tecsa = st.selectbox("TecSa-relevant", ["Ja", "Nein"])
with col_b:
    pruefablauf = st.text_area("📋 Prüfablauf")
with col_c:
    bild = st.file_uploader("📸 Bauteilbild hochladen", type=["jpg", "png", "jpeg"])

# --- Gebotsschilder ---
st.markdown('<h3 style="background-color:#f5f5f5;padding:10px;">🛡️ Gebots- und Warnschilder (Bilderauswahl)</h3>', unsafe_allow_html=True)

col_b1, col_b2, col_b3, col_b4 = st.columns(4)

with col_b1:
    st.image("images/fusschutz.jpg", width=100)
    fusschutz_selected = st.checkbox("Fußschutz")

with col_b2:
    st.image("images/warnweste.jpg", width=100)
    warnweste_selected = st.checkbox("Warnweste")

with col_b3:
    st.image("images/fußgaenger.jpg", width=100)
    fussweg_selected = st.checkbox("Fußgängerweg")

with col_b4:
    st.image("images/augenschutz.jpg", width=100)
    augenschutz_selected = st.checkbox("Augenschutz")

ausgewaehlte_bilder = []
if fusschutz_selected:
    ausgewaehlte_bilder.append("Fußschutz")
if warnweste_selected:
    ausgewaehlte_bilder.append("Warnweste")
if fussweg_selected:
    ausgewaehlte_bilder.append("Fußgängerweg")
if augenschutz_selected:
    ausgewaehlte_bilder.append("Augenschutz")

st.markdown("**Ausgewählte Schilder:**")

for schild in ausgewaehlte_bilder:
    st.markdown(f"- ✅ {schild}")




# --- NEUE SEITE: Serienbehälter ---

st.markdown('<h1 style="text-align:center;">📄 Arbeitsanweisung</h1>', unsafe_allow_html=True)

# --- Erste Zeile: Sortierstart & Freigabe ---
col1a, col1b = st.columns(2)
with col1a:
    sortierstart2 = st.date_input("📅 Sortierstart (Seite 2)", key="sortierstart2")
with col1b:
    freigabe2 = st.text_input("📝 Freigabe", key="freigabe2")

# --- Zweite Zeile: Auftrags-IDs & Kritischer BI ---
col2a, col2b, col2c = st.columns(3)
with col2a:
    auftrag_bbw2 = st.text_input("🧾 Auftrags-ID BBW", key="auftrag_bbw2")
with col2b:
    auftrag_bmw2 = st.text_input("🧾 Auftrags-ID BMW", key="auftrag_bmw2")
with col2c:
    kritischster_bi2 = st.selectbox("📊 Kritischster BI", list(range(1, 11)), key="kritischster_bi2")

st.markdown('<div style="background-color:#f0f0f0;padding:10px;"><strong>📋 Prüfumfang</strong></div>', unsafe_allow_html=True)
pruefumfang2 = st.text_area("", height=80, key="pruefumfang2")

# --- Serienbehälter-Bereich ---
st.markdown('<h3 style="background-color:#e6e6e6;padding:10px;">📦 Serienbehälter</h3>', unsafe_allow_html=True)

col_img, col_kommentar = st.columns([2, 1])
with col_img:
    serienbild2 = st.file_uploader("📸 Bild vom Serienbehälter hochladen", type=["jpg", "jpeg", "png"], key="serienbild2")
    if serienbild2:
        st.image(serienbild2, use_column_width=True)

with col_kommentar:
    kommentar_serien = st.text_area("💬 Kommentar zum Behälter", height=220, key="kommentar_serien")

# --- Untere 3-Spalten-Zeile ---
col_a, col_b, col_c = st.columns(3)
with col_a:
    abteilung_bmw2 = st.text_input("🏢 Abteilung BMW", key="abteilung_bmw2")
with col_b:
    ansprechpartner_kunde2 = st.text_input("👤 Ansprechpartner Kunde", key="ansprechpartner_kunde2")
with col_c:
    erstellt_von = st.text_input("🖊️ AAW erstellt von", key="erstellt_von")








import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="BMW Teileprüfung", layout="wide")
st.title("🔐 Zugriff geschützt")

# --- Passwortschutz ---
PASSWORD = "bmw2025"
pw_input = st.text_input("Bitte Passwort eingeben:", type="password")
if pw_input != PASSWORD:
    st.warning("🔒 Zugang nur mit gültigem Passwort.")
    st.stop()

st.title("🧾 BMW Teileprüfungs-Formular")

# --- Abschnitt: Teilinformationen ---
st.markdown('<h3 style="background-color:#d9edf7;padding:10px;">🔹 Teilinformationen</h3>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    datum = st.date_input("📅 Datum der Prüfung", value=datetime.today())
    teilenummer = st.text_input("🔢 Teilenummer")
    arbeitsort = st.text_input("🏭 Arbeitsort")

with col2:
    teilebezeichnung = st.text_input("📄 Teilebezeichnung")
    auftrags_id_bmw = st.text_input("🧾 Auftrags-ID BMW")
    auftrags_id_bbw = st.text_input("🧾 Auftrags-ID BBW")

with col3:
    abteilung = st.text_input("🏷️ Abteilung BMW")
    ansprechpartner = st.text_input("📞 Ansprechpartner")
    kritischer_bi = st.selectbox("📊 Kritischer BI", list(range(1, 11)))

# --- Abschnitt: Prüfdetails ---
st.markdown('<h3 style="background-color:#fcf8e3;padding:10px;">🔸 Prüfdetails</h3>', unsafe_allow_html=True)
col4, col5, col6 = st.columns(3)

with col4:
    io_nio = st.selectbox("✅ Zustand des Teils", ["IO", "NIO"])
with col5:
    fehlerbild = st.selectbox("❗ Fehlerbild", ["-", "A", "B", "C", "D", "E", "F"]) if io_nio == "NIO" else "-"
with col6:
    kommentar = st.text_area("💬 Bemerkung")

# --- Abschnitt: PSA und Bilder ---
st.markdown('<h3 style="background-color:#dff0d8;padding:10px;">🟢 PSA & Mitarbeiter</h3>', unsafe_allow_html=True)
col7, col8, col9 = st.columns(3)

with col7:
    mitarbeiter = st.text_input("👤 Mitarbeitername")
with col8:
    foto = st.file_uploader("📷 Foto hochladen", type=["jpg", "png", "jpeg"])
with col9:
    pass

# --- Abschnitt: Gebotsschilder ---
st.markdown('<h3 style="background-color:#f5f5f5;padding:10px;">🛡️ Gebots- und Warnschilder</h3>', unsafe_allow_html=True)
gebotsschilder = [
    "M001 Allgemeines Gebotszeichen",
    "M003 Gehörschutz benutzen",
    "M004 Augenschutz benutzen",
    "M008 Fußschutz benutzen",
    "M009 Handschutz benutzen",
    "M010 Schutzkleidung benutzen",
    "M011 Hände waschen",
    "M012 Handlauf benutzen",
    "M013 Gesichtsschutz benutzen"
]
ausgewaehlte_gebote = st.multiselect("Wählen Sie die zutreffenden Schilder aus:", gebotsschilder)

# --- Speichern ---
if st.button("📥 Eintrag speichern"):
    eintrag = {
        "Datum": datum.strftime("%Y-%m-%d"),
        "Teilenummer": teilenummer,
        "Arbeitsort": arbeitsort,
        "Teilebezeichnung": teilebezeichnung,
        "Auftrags-ID BMW": auftrags_id_bmw,
        "Auftrags-ID BBW": auftrags_id_bbw,
        "Abteilung": abteilung,
        "Ansprechpartner": ansprechpartner,
        "Kritischer BI": kritischer_bi,
        "IO/NIO": io_nio,
        "Fehlerbild": fehlerbild,
        "Kommentar": kommentar,
        "Mitarbeiter": mitarbeiter,
        "Foto": foto.name if foto else "",
        "Gebotsschilder": "; ".join(ausgewaehlte_gebote)
    }

    df = pd.DataFrame([eintrag])
    if not os.path.exists("berichte.csv"):
        df.to_csv("berichte.csv", index=False)
    else:
        df.to_csv("berichte.csv", mode='a', header=False, index=False)

    if foto:
        os.makedirs("fotos", exist_ok=True)
        with open(os.path.join("fotos", foto.name), "wb") as f:
            f.write(foto.read())

    st.success("✅ Eintrag wurde gespeichert!")

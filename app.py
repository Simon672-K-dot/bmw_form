import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="BMW Teileprüfung", layout="centered")

# --- Passwortschutz ---
PASSWORD = "bmw2025"
st.title("🔐 Zugriff geschützt")

pw_input = st.text_input("Bitte Passwort eingeben:", type="password")
if pw_input != PASSWORD:
    st.warning("🔒 Zugang nur mit gültigem Passwort.")
    st.stop()

st.title("🧾 BMW Teileprüfungs-Formular")

# --- Eingabefelder ---
datum = st.date_input("📅 Datum der Prüfung", value=datetime.today())
teilenummer = st.text_input("🔢 Teilenummer")
teilebezeichnung = st.text_input("📄 Teilebezeichnung")
io_nio = st.selectbox("✅ Zustand des Teils", ["IO", "NIO"])
fehlerbild = st.selectbox("❗ Fehlerbild (nur bei NIO)", ["-", "A", "B", "C", "D", "E", "F"]) if io_nio == "NIO" else "-"
kommentar = st.text_area("💬 Bemerkung")
foto = st.file_uploader("📷 Foto hochladen", type=["jpg", "png", "jpeg"])
mitarbeiter = st.text_input("👤 Mitarbeitername")

# --- Daten speichern ---
if st.button("📥 Eintrag speichern"):
    eintrag = {
        "Datum": datum.strftime("%Y-%m-%d"),
        "Teilenummer": teilenummer,
        "Teilebezeichnung": teilebezeichnung,
        "IO/NIO": io_nio,
        "Fehlerbild": fehlerbild,
        "Kommentar": kommentar,
        "Foto": foto.name if foto else "",
        "Mitarbeiter": mitarbeiter
    }

    df = pd.DataFrame([eintrag])

    if not os.path.exists("berichte.csv"):
        df.to_csv("berichte.csv", index=False)
    else:
        df.to_csv("berichte.csv", mode='a', index=False, header=False)

    # Save photo if uploaded
    if foto:
        os.makedirs("fotos", exist_ok=True)
        with open(os.path.join("fotos", foto.name), "wb") as f:
            f.write(foto.read())

    st.success("✅ Eintrag wurde gespeichert!")

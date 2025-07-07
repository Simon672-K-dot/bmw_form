
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




# --- NEUE SEITE ---

import streamlit as st
from datetime import date

st.set_page_config(page_title="Bauteil Dokumentation", layout="wide")

st.markdown("## 📋 Auswahl der Bauteile zur Dokumentation")

# --- Anzahl je Bauteiltyp ---
num_serien = st.number_input("📦 Serienbehälter", min_value=0, max_value=10, value=0)
num_io = st.number_input("✅ I.O.-Bauteil", min_value=0, max_value=10, value=0)
num_nio = st.number_input("❌ N.I.O.-Bauteil", min_value=0, max_value=10, value=0)
num_markierung = st.number_input("🖊️ I.O.-Markierung", min_value=0, max_value=10, value=0)
num_freigabezettel = st.number_input("📑 Freigabezettel", min_value=0, max_value=10, value=0)

st.markdown("---")

# --- Wiederverwendbare Layout-Funktion ---
def render_block(typ, index):
    st.markdown(f"<h3 style='background-color:#f0f0f0;padding:10px;'>{typ} {index+1}</h3>", unsafe_allow_html=True)

    st.markdown('<div style="background-color:#e8e8e8;padding:8px;margin-bottom:10px;"><strong>📋 Prüfumfang</strong></div>', unsafe_allow_html=True)
    st.text_area(f"Prüfumfang {typ} {index+1}", key=f"pruefumfang_{typ}_{index}")

    col_img, col_kommentar = st.columns([2, 1])
    with col_img:
        bild = st.file_uploader(f"📸 Bild für {typ} {index+1}", type=["jpg", "jpeg", "png"], key=f"img_{typ}_{index}")
        if bild:
            st.image(bild, use_column_width=True)

    with col_kommentar:
        st.text_area("💬 Kommentar", height=200, key=f"kommentar_{typ}_{index}")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.text_input("🏢 Abteilung BMW", key=f"abteilung_{typ}_{index}")
    with col_b:
        st.text_input("👤 Ansprechpartner Kunde", key=f"ansprechpartner_{typ}_{index}")
    with col_c:
        st.text_input("🖊️ AAW erstellt von", key=f"erstellt_von_{typ}_{index}")

    st.markdown("---")

# --- Serienbehälter Blöcke ---
for i in range(num_serien):
    render_block("📦 Serienbehälter", i)

# --- I.O.-Bauteil Blöcke ---
for i in range(num_io):
    render_block("✅ I.O.-Bauteil", i)

# --- N.I.O.-Bauteil Blöcke ---
for i in range(num_nio):
    render_block("❌ N.I.O.-Bauteil", i)

# --- I.O.-Markierung Blöcke ---
for i in range(num_markierung):
    render_block("🖊️ I.O.-Markierung", i)

# --- Freigabezettel Blöcke ---
for i in range(num_freigabezettel):
    render_block("📑 Freigabezettel", i)






# --- Seite 3:Nachweis Freigabe Section---
st.markdown('<h2 style="text-align:center; background-color:#e6e6e6; padding:10px;">🧾 Nachweis Freigabe</h2>', unsafe_allow_html=True)

# Row: Freigabe BBW and BMW
col1, col2 = st.columns(2)
with col1:
    freigabe_bbw = st.text_input("✅ Freigabe B.B.W", key="freigabe_bbw")
with col2:
    freigabe_bmw = st.text_input("🏁 Freigabe BMW", key="freigabe_bmw")

# Allgemeine Anweisungen (green area)
st.markdown('<div style="background-color:#dff0d8;padding:10px;"><strong>✅ Allgemeine Anweisungen</strong></div>', unsafe_allow_html=True)
anweisungen = st.text_area("", height=150, key="allgemeine_anweisungen")

# Zusatz für QCat-gesteuerte Aufträge
st.markdown('<div style="background-color:#f9f9f9;padding:10px;"><strong>📌 Zusatz für QCat-gesteuerte Aufträge:</strong></div>', unsafe_allow_html=True)
zusatz_qcat = st.text_area("", height=150, key="zusatz_qcat")






#---Seite 4:Mitarbeiter Einweisung---

st.markdown("## 🧾 Einweisungsübersicht")

# Define 15 rows with 5 columns
columns = [
    "Name unterwiesene Person",
    "Datum Unterweisung",
    "Unterschrift unterwiesene Person",
    "Unterschrift Unterweisender",
    "Unterwiesen durch"
]

df_matrix = pd.DataFrame({col: [""] * 15 for col in columns})

# Editable matrix-style table
edited_matrix = st.data_editor(df_matrix, num_rows="dynamic", use_container_width=True)




#---Seite 5:Anhang zur Arbeitsanweisung---


import pandas as pd
import streamlit as st

# 🔴 Main headline in red
st.markdown("<h2 style='color:red;'>📎 Anhang zur Arbeitsanweisung</h2>", unsafe_allow_html=True)

# 🔹 Subheadline for table section
st.markdown("<h4 style='margin-top:-10px;'>📦 Materialdaten</h4>", unsafe_allow_html=True)

# 📋 Define table columns
columns = [
    "Materialnummer",
    "Materialbezeichnung",
    "Lieferant",
    "Fehlerort",
    "Fehlerart",
    "BI"
]

# Empty editable table
df_anhang = pd.DataFrame(columns=columns)

# 📝 Dynamic editor
edited_df = st.data_editor(
    df_anhang,
    num_rows="dynamic",
    use_container_width=True,
    hide_index=True
)



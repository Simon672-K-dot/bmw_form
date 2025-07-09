
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

# --- Erste Zeile: Sortierstart ---
sortierstart = st.date_input("📅 Sortierstart")
st.write("DEBUG – Sortierstart:", sortierstart)

# --- Zweite Zeile: Freigabe Überschrift ---
st.markdown("### 📌 Freigabe")


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

# ✅ Headline with light green underline
st.markdown("""
<div style="border-bottom: 4px solid #b6e3b6; padding-bottom: 5px; margin-bottom: 15px;">
    <h2 style="color:#262730; margin:0;">📎 Anhang zur Arbeitsanweisung</h2>
</div>
""", unsafe_allow_html=True)

# 🔹 Subheadline
st.markdown("<h4 style='margin-top:-10px;'>📦 Materialdaten</h4>", unsafe_allow_html=True)

# 📋 Define initial table with deletion column
columns = [
    "Materialnummer",
    "Materialbezeichnung",
    "Lieferant",
    "Fehlerort",
    "Fehlerart",
    "BI",
    "🗑️ Löschen?"
]

# Leeres DataFrame (dynamisch erweiterbar)
df_anhang = pd.DataFrame(columns=columns)

# 📝 Editable table
edited_df = st.data_editor(
    df_anhang,
    num_rows="dynamic",
    use_container_width=True,
    hide_index=True
)

# 🧹 Filter rows where "🗑️ Löschen?" is not checked (False or NaN)
if not edited_df.empty:
    cleaned_df = edited_df[(edited_df["🗑️ Löschen?"] != True) | (edited_df["🗑️ Löschen?"].isna())]




#---Seite 6: Ergebnisserfassung 


import streamlit as st
import pandas as pd

# Title Section
st.markdown('<h2 style="text-align:center;">📊 Ergebniserfassung</h2>', unsafe_allow_html=True)

# Header section: Auftrag, Lieferant, Teile-Nr., Teilebezeichnung
col1, col2, col3, col4 = st.columns(4)
with col1:
    auftrag = st.text_input("Auftrag", value="19991", disabled=True)
with col2:
    lieferant = st.text_input("Lieferant", value="DAIMAY FRANCE")
with col3:
    teil_nr = st.text_input("Teile-Nr.")
with col4:
    teil_bez = st.text_input("Teilebezeichnung")

# Sub-header: Datum, Art der Tätigkeit, Art der Prüfung
col5, col6, col7 = st.columns(3)
with col5:
    datum = st.date_input("📅 Datum")
with col6:
    taetigkeit = st.text_input("Art der Tätigkeit")
with col7:
    pruefart = st.selectbox("Art der Prüfung", [
        "Erstprüfung", "200% Prüfung", "Wdh. Prüfung IO", "Wdh. Prüfung NIO"
    ])

# Prüfort & IO-F-NR
col8, col9 = st.columns(2)
with col8:
    pruefort = st.selectbox("Prüfort", ["Q-Fläche", "Bandbegleitend"])
with col9:
    io_fnr = st.selectbox("IO - F. NR.", ["VZ3 Neufahrn / AP", "VZ3 München / AP"])

# --- FEHLERBILDER ABSCHNITT ---
st.markdown('<h4 style="margin-top: 30px;">🟥 Fehlerbilder:</h4>', unsafe_allow_html=True)

# Erste Reihe: A, B, C mit Textfeldern
cols_abc = st.columns([1, 4, 1, 4, 1, 4])
with cols_abc[0]:
    st.markdown('<div style="background-color:#ff4d4d;color:white;text-align:center;font-weight:bold;padding:6px;border-radius:5px;">A</div>', unsafe_allow_html=True)
with cols_abc[1]:
    fehler_a = st.text_input(" ", key="fehler_a")
with cols_abc[2]:
    st.markdown('<div style="background-color:#ff4d4d;color:white;text-align:center;font-weight:bold;padding:6px;border-radius:5px;">B</div>', unsafe_allow_html=True)
with cols_abc[3]:
    fehler_b = st.text_input(" ", key="fehler_b")
with cols_abc[4]:
    st.markdown('<div style="background-color:#ff4d4d;color:white;text-align:center;font-weight:bold;padding:6px;border-radius:5px;">C</div>', unsafe_allow_html=True)
with cols_abc[5]:
    fehler_c = st.text_input(" ", key="fehler_c")

# Zweite Reihe: D, E, F mit Textfeldern
cols_def = st.columns([1, 4, 1, 4, 1, 4])
with cols_def[0]:
    st.markdown('<div style="background-color:#ff4d4d;color:white;text-align:center;font-weight:bold;padding:6px;border-radius:5px;">D</div>', unsafe_allow_html=True)
with cols_def[1]:
    fehler_d = st.text_input(" ", key="fehler_d")
with cols_def[2]:
    st.markdown('<div style="background-color:#ff4d4d;color:white;text-align:center;font-weight:bold;padding:6px;border-radius:5px;">E</div>', unsafe_allow_html=True)
with cols_def[3]:
    fehler_e = st.text_input(" ", key="fehler_e")
with cols_def[4]:
    st.markdown('<div style="background-color:#ff4d4d;color:white;text-align:center;font-weight:bold;padding:6px;border-radius:5px;">F</div>', unsafe_allow_html=True)
with cols_def[5]:
    fehler_f = st.text_input(" ", key="fehler_f")

# Ergebnisseingabe Tabelle
st.markdown('<h4 style="margin-top:20px;">📥 Ergebnisseingabe</h4>', unsafe_allow_html=True)

columns = [
    "Lieferschein Nr.", "HU-Nummer", "ID OK", "Gesamt geprüft", "IO",
    "NIO A", "NIO B", "NIO C", "NIO D", "NIO E", "NIO F",
    "NIO Gesamt", "Nachgearbeitet", "Rest NIO", "Bemerkung"
]
df_ergebnis = pd.DataFrame(columns=columns)

edited_df = st.data_editor(
    df_ergebnis,
    num_rows="dynamic",
    use_container_width=True,
    key="ergebniserfassung_matrix"
) 

       






#---Seite 7: Teil von Ergebniserfassung---


import streamlit as st
import pandas as pd

# Set page section title (continuation of Ergebniserfassung, no new header)
st.markdown("### 👷‍♂️ Mitarbeitereintrag zur Ergebniserfassung")

# Initial table structure for Mitarbeiter-Eintrag
default_data = {
    "Bearbeitung durch Mitarbeiter": ["" for _ in range(5)],
    "Anfangszeit der Prüfung": ["" for _ in range(5)],
    "Endzeit der Prüfung": ["" for _ in range(5)],
    "Personalnr.": ["" for _ in range(5)],
}

df_mitarbeiter = pd.DataFrame(default_data)

# Use data editor for dynamic editing
edited_mitarbeiter = st.data_editor(
    df_mitarbeiter,
    num_rows="dynamic",
    use_container_width=True
)

# Right section: Freigabe & Buchung
st.markdown("### 🧾 Freigabe und Buchung")

col1, col2 = st.columns(2)

with col1:
    freigabe_checkbox = st.checkbox("✅ Freigabe für Ergebniserfassung erteilt")
    personalnr_freigabe = st.text_input("👤 Personalnr. (Freigabe)", key="freigabe_personal")

with col2:
    buchung_checkbox = st.checkbox("✅ Buchung der Ergebniserfassung im B.B.W. Portal erfolgt")
    personalnr_buchung = st.text_input("👤 Personalnr. (B.B.W. Portal)", key="buchung_personal")

# Remarks
st.markdown("### 📝 Bemerkungen")
bemerkungen = st.text_area("Bemerkungen sind im QCat zu erfassen", height=100)




# -----------------------------------
# ✅ Function to fill the PDF
# -----------------------------------
import fitz  # PyMuPDF

def fill_pdf(template_path, output_path, data):
    doc = fitz.open(template_path)

    for page in doc:
        for widget in page.widgets():
            field_name = widget.field_name.lower()  # make lowercase
            if field_name in data:
                widget.field_value = data[field_name]
                widget.update()

    doc.save(output_path)
    doc.close()







# --- FINAL SUBMIT BUTTON ---
from io import BytesIO

if st.button("✅ Formular abgeben"):
    data = {
        'Sortierstart': str(sortierstart),
        'Auftrags-ID BBW': auftrag_bbw,
        'Auftrags-ID BMW': auftrag_bmw,
        'Kritischster BI': str(kritischster_bi),
        # Add more keys as you map the fields
    }

    filled_filename = f"filled_{auftrag_bmw}.pdf"
    fill_pdf("bbw_template_fillable.pdf", filled_filename, data)

    with open(filled_filename, "rb") as file:
        st.download_button(
            label="📥 PDF herunterladen",
            data=file,
            file_name=filled_filename,
            mime="application/pdf"
        )

    st.success("✅ Das Formular wurde erfolgreich abgegeben und als PDF gespeichert!")








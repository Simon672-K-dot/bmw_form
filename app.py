
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
    bild1 = st.file_uploader("📸 Bauteilbild hochladen", type=["jpg", "png", "jpeg"], key="bild1")

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

num_bauteilbild = st.number_input("📸 Bauteilbild", min_value=0, max_value=10, value=0)
num_nio = st.number_input("❌ NIO-Bauteil", min_value=0, max_value=10, value=0)
num_hilfsmittel = st.number_input("🔧 Prüf-/Hilfsmittel", min_value=0, max_value=10, value=0)
num_pruefablauf = st.number_input("📋 Allgemeiner Prüfablauf", min_value=0, max_value=10, value=0)
num_io_markierung = st.number_input("🖊️ IO-Markierung", min_value=0, max_value=10, value=0)


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
            st.image(bild, use_container_width=True)


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
for i in range(num_bauteilbild):
    render_block("Bauteilbild", i)

for i in range(num_nio):
    render_block("NIO-Bauteil", i)

for i in range(num_hilfsmittel):
    render_block("Prüf-/Hilfsmittel", i)

for i in range(num_pruefablauf):
    render_block("Allgemeiner Prüfablauf", i)

for i in range(num_io_markierung):
    render_block("IO-Markierung", i)




# 🔄 Dynamisch hochgeladene Bilder aus render_block() einsammeln
uploaded_bauteilbilder = []

for typ in ["Bauteilbild", "NIO-Bauteil", "Prüf-/Hilfsmittel", "Allgemeiner Prüfablauf", "IO-Markierung"]:
    for i in range(10):  # max 10 Einträge je Typ
        key = f"img_{typ}_{i}"
        if key in st.session_state and st.session_state[key] is not None:
            uploaded_bauteilbilder.append(st.session_state[key])








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
else:
    cleaned_df = pd.DataFrame(columns=columns)




#FUNCTION 



def fill_pdf_with_multiple_images(template_path, output_path, data, image_dict=None, extra_images=None):

    import fitz  # PyMuPDF
    from PIL import Image
    import io

    doc = fitz.open(template_path)

    # Fill text fields
    for page in doc:
        widgets = page.widgets()
        if widgets:
            for widget in widgets:
                field_name = widget.field_name
                if field_name in data:
                    widget.field_value = data[field_name]
                    widget.update()

    # ✅ Insert images at placeholder fields
    if image_dict:
        for field_name, img_file in image_dict.items():
            if img_file:
                img = Image.open(img_file).convert("RGB")
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format="PNG")
                img_stream = img_byte_arr.getvalue()

                for page in doc:
                    widgets = page.widgets()
                    for widget in widgets:
                        if widget.field_name == field_name:
                            image_rect = widget.rect
                            widget.field_value = ""
                            widget.update()
                            page.insert_image(image_rect, stream=img_stream)
                            break
        # ✅ Remove extra pages after Anhang
    while len(doc) > 8:
        doc.delete_page(len(doc) - 1)



        # ➕ Neue Seiten für zusätzliche Bilder (z.B. Bauteildokumentation)
    if extra_images:
        for img_file in extra_images:
            img = Image.open(img_file).convert("RGB")
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format="PNG")
            img_stream = img_byte_arr.getvalue()

            # Neue leere Seite (A4-Größe)
            page = doc.new_page(width=595, height=842)

            # Bild auf Seite einfügen mit Rand
            page.insert_image(fitz.Rect(50, 50, 545, 792), stream=img_stream)

    doc.save(output_path)
    doc.close()
    
   




# --- FINAL SUBMIT BUTTON ---
from io import BytesIO

if st.button("✅ Formular abgeben"):
    data = {
        # Page 1
        "Sortierstart": str(sortierstart),
        "AuftragsID BBW1": auftrag_bbw,
        "AuftragsID BMW1": auftrag_bmw,
        "Kritischster BI": str(kritischster_bi),
        "Tätigkeit": taetigkeit,
        "Lieferant": lieferant,
        "Fehlerbild A": fehlerbild_a,
        "Fehlerbild B": fehlerbild_b,
        "Fehlerbild C": fehlerbild_c,
        "Fehlerbild D": fehlerbild_d,
        "Fehlerbild E": fehlerbild_e,
        "Fehlerbild F": fehlerbild_f,
        "FZG  Motorentyp": motorentyp,
        "Verbautakt": verbautakt,
        "Tagesbedarf": tagesbedarf,
        "Abteilung BMW": abteilung_bmw,
        "Ansprechpartner BBW": ansprechpartner_bbw,
        "Ansprechpartner Kunde": ansprechpartner_kunde,
        "SortierPrüfort": pruefort,
        "Arbeitsorte": arbeitsorte,
        "Sortierregel": sortierregel,
        "IO Markierung": io_markierung,
        "PSA": psa,
        "Handschuhe": handschuhe,
        "Zusätzliche Standards": zusaetzliche_standards,
        "COP": cop,
        "Prüfablauf": pruefablauf,
        "Gebots und Warnschilder": ", ".join(ausgewaehlte_bilder),

        # Page 3–6 (NIO, Prüfmittel, Prüfablauf, IO-Markierung)
        "NIO-Bauteil3": "—",
        "Hilfsmittel4": "—",
        "Prüfablauf5": pruefablauf,
        "IO-Markierung6": io_markierung,

        "Abteilung BMW3": abteilung_bmw,
        "Ansprechpartner Kunde3": ansprechpartner_kunde,
        "AAW erstellt von3": "Dein Name",

        "Abteilung BMW4": abteilung_bmw,
        "Ansprechpartner Kunde4": ansprechpartner_kunde,
        "AAW erstellt von4": "Dein Name",

        "Abteilung BMW5": abteilung_bmw,
        "Ansprechpartner Kunde5": ansprechpartner_kunde,
        "AAW erstellt von5": "Dein Name",

        "Abteilung BMW6": abteilung_bmw,
        "Ansprechpartner Kunde6": ansprechpartner_kunde,
        "AAW erstellt von6": "Dein Name",

        # Page 7: Nachweis Freigabe
        "Freigabe Formel I": freigabe_bmw,
        "Zusatz": zusatz_qcat,
        "AA1": anweisungen,

        # Page 8: Materialdaten rows:1-2
               
        "Materialnummer1": cleaned_df.iloc[0]["Materialnummer"] if len(cleaned_df) > 0 else "",
        "Materialbezeichnung1": cleaned_df.iloc[0]["Materialbezeichnung"] if len(cleaned_df) > 0 else "",
        "Lieferant1": cleaned_df.iloc[0]["Lieferant"] if len(cleaned_df) > 0 else "",
        "Fehlort1": cleaned_df.iloc[0]["Fehlerort"] if len(cleaned_df) > 0 else "",
        "Fehlart1": cleaned_df.iloc[0]["Fehlerart"] if len(cleaned_df) > 0 else "",
        "BI_1": cleaned_df.iloc[0]["BI"] if len(cleaned_df) > 0 else "",

        "Materialnummer2": cleaned_df.iloc[1]["Materialnummer"] if len(cleaned_df) > 1 else "",
        "Materialbezeichnung2": cleaned_df.iloc[1]["Materialbezeichnung"] if len(cleaned_df) > 1 else "",
        "Lieferant2": cleaned_df.iloc[1]["Lieferant"] if len(cleaned_df) > 1 else "",
        "Fehlort2": cleaned_df.iloc[1]["Fehlerort"] if len(cleaned_df) > 1 else "",
        "Fehlart2": cleaned_df.iloc[1]["Fehlerart"] if len(cleaned_df) > 1 else "",
        "BI_2": cleaned_df.iloc[1]["BI"] if len(cleaned_df) > 1 else "",

    }

    image_fields = {
        "Bauteilbild_box": bild1,
        "Bauteilbild2": bild1,
    }

    # Output in memory (no saving to disk)
    pdf_output = BytesIO()
    fill_pdf_with_multiple_images("bbw_template_fillable.pdf", pdf_output, data, image_fields)

    st.download_button(
        label="📥 PDF herunterladen",
        data=pdf_output.getvalue(),
        file_name=f"Arbeitsanweisung_{auftrag_bmw}.pdf",
        mime="application/pdf"
    )

    st.success("✅ Das Formular wurde erfolgreich abgegeben und als PDF generiert!")

    






if st.button("📋 Zeige PDF-Feldnamen (PyPDF2)"):
    from PyPDF2 import PdfReader

    pdf_path = "bbw_template_fillable.pdf"
    reader = PdfReader(pdf_path)
    fields = reader.get_fields()

    st.markdown("### 🧾 Gefundene Formularfelder:")
    if fields:
        for name in fields:
            st.write(f"Field name: '{name}'")
    else:
        st.warning("⚠️ Keine Formularfelder gefunden.")
   

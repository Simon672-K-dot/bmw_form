
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

# Unterhalb von Freigabe: vier Felder nebeneinander
col_freigabe, col_ids1, col_ids2, col_ids3 = st.columns(4)

with col_freigabe:
    freigabe_bmw = st.text_input("✅ Rev/Freigabe")

with col_ids1:
    auftrags_id = st.text_input("🧾 Auftrags-ID")

with col_ids2:
    vorgangs_nr = st.text_input("🧾 VorgangsNr")

with col_ids3:
    bi = st.selectbox("📊 BI", list(range(1, 8)))


st.markdown("---")

# --- Drei Spalten ab Zeile 3 ---
st.markdown('<h3 style="background-color:#e8e8e8;padding:10px;">📋 Prüf- & Teildaten</h3>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    auftrag = st.text_input("📄 Auftrag")
    taetigkeit = st.text_input("🛠️ Tätigkeit")
    fehlerbild_a = st.text_input("❌ Fehlerbild A")
    fehlerbild_b = st.text_input("❌ Fehlerbild B")
    fehlerbild_c = st.text_input("❌ Fehlerbild C")
    fehlerbild_d = st.text_input("❌ Fehlerbild D")
    fehlerbild_e = st.text_input("❌ Fehlerbild E")
    fehlerbild_f = st.text_input("❌ Fehlerbild F")
    
with col2:
    lieferant = st.text_input("🚚 Lieferant")
    kst = st.text_input("⚙️ KST")
    tagesbedarf = st.text_input("📦 Tagesbedarf")
    ansprechpartner_kunde = st.text_input("👤 Ansprechpartner Kunde")
    arbeitsorte = st.text_input("📍 Arbeitsort(e)")
    Werk = st.text_input("Prüfort Werk")

with col3:

    abteilung = st.text_input("🏷️ Abteilung")
    sortierregel = st.text_input("📑 Sortierregel")
    motorentyp = st.text_input("🚗 FZG / Motorentyp")
    Auftraggeber = st.text_input("👷 Auftraggeber")
    pruefort = st.text_input("🏭 Sortier-/Prüfort")
    Koordinator = st.text_input("Koordinator")


st.markdown("---")




# ---  Markierung & PSA Bereich ---



st.markdown('<h3 style="background-color:#d9edf7;padding:10px;">🧤 PSA</h3>', unsafe_allow_html=True)

# --- PSA Symbol Selection Block ---
st.markdown('<h3 style="background-color:#f5f5f5;padding:10px;">🛡️ Gebots- und Warnschilder (Bilderauswahl)</h3>', unsafe_allow_html=True)

col_b1, col_b2, col_b3, col_b4 = st.columns(4)

with col_b1:
    st.image("images/fusschutz.jpg", width=100)
    fusschutz_selected = st.checkbox("Fußschutz")
    st.image("images/helm1.png", width=100)
    helm_selected = st.checkbox("Helm")

with col_b2:
    st.image("images/warnweste.jpg", width=100)
    warnweste_selected = st.checkbox("Warnweste")
    st.image("images/Handschuhe.png", width=100)
    handschuhe_selected = st.checkbox("Handschuhe")

with col_b3:
    st.image("images/fußgaenger.jpg", width=100)
    fussweg_selected = st.checkbox("Fußgängerweg")

with col_b4:
    st.image("images/augenschutz.jpg", width=100)
    augenschutz_selected = st.checkbox("Augenschutz")

# Collect selected image labels
ausgewaehlte_bilder = []
if fusschutz_selected:
    ausgewaehlte_bilder.append("Fußschutz")
if helm_selected:
    ausgewaehlte_bilder.append("Helm")
if warnweste_selected:
    ausgewaehlte_bilder.append("Warnweste")
if handschuhe_selected:
    ausgewaehlte_bilder.append("Handschuhe")
if fussweg_selected:
    ausgewaehlte_bilder.append("Fußgängerweg")
if augenschutz_selected:
    ausgewaehlte_bilder.append("Augenschutz")

# Show selection
st.markdown("**Ausgewählte Schilder:**")
for schild in ausgewaehlte_bilder:
    st.markdown(f"- ✅ {schild}")



# Headline: Markierung (green)
st.markdown('<h3 style="background-color:#dff0d8;padding:10px;">✅ Markierung</h3>', unsafe_allow_html=True)
markierung = st.text_input("Markierung gemäß Vorgabe")

# Headline: Beschreibung / Prüfablauf (orange)
st.markdown('<h3 style="background-color:#ffe5b4;padding:10px;">📝 Beschreibung / Prüfablauf</h3>', unsafe_allow_html=True)
beschreibung_pruefablauf = st.text_area("Prüfablauf Beschreibung")

# Headline: Zusätzliche Informationen (red)
st.markdown('<h3 style="background-color:#f2dede;padding:10px;">📌 Zusätzliche Informationen</h3>', unsafe_allow_html=True)
col_left, col_right = st.columns([2, 1])

with col_left:
    zusaetzliche_infos = st.text_area("Zusätzliche Angaben")

with col_right:
    cop = st.selectbox("COP-Relevant", ["", "Ja", "Nein"])
    esd = st.selectbox("ESD-Relevant", ["", "Ja", "Nein"])
    tecsa = st.selectbox("TecSa-Relevant", ["", "Ja", "Nein"])

# Build COP field value for PDF (print only if selection is not empty)
if cop == "Ja":
    cop_field_value = "cop: Ja"
elif cop == "Nein":
    cop_field_value = "cop: Nein"
else:
    cop_field_value = ""






# --- NEUE SEITE ---






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

st.markdown("---")
st.markdown("### 🔍 PDF-Felder anzeigen (Debug Tool)")

if st.button("📋 Zeige PDF-Feldnamen (PyPDF2)"):
    from PyPDF2 import PdfReader
    import os

    pdf_path = "bbw_template_fillable.pdf"
    st.write("📁 Dateipfad:", pdf_path)
    st.write("🧪 Datei existiert:", os.path.exists(pdf_path))

    try:
        reader = PdfReader(pdf_path)
        fields = reader.get_fields()

        st.markdown("### 🧾 Gefundene Formularfelder:")
        if fields:
            for name in fields:
                st.write(f"Field name: '{name}'")
        else:
            st.warning("⚠️ Keine Formularfelder gefunden.")
    except Exception as ecop_text_lines = []






# Build content for the "Cop" field (combined string)


# Combine COP/ESD/TecSa selections into one string for the "Cop" PDF field
cop_text_lines = []

if cop:
    cop_text_lines.append(f"cop: {cop}")
if esd:
    cop_text_lines.append(f"esd: {esd}")
if tecsa:
    cop_text_lines.append(f"tecsa: {tecsa}")

cop_field_value = "\n".join(cop_text_lines)







if st.button("✅ Formular abgeben"):
    data = {
        # ✅ First Section (Pages 1–2)
        "Freigabe": freigabe_bmw,
        "Sortierstart": str(sortierstart),
        "Auftrags-ID": auftrags_id,
        "Auftrag": auftrag,
        "BI": str(bi),
        "VorgangsNr": vorgangs_nr,
    
        "Tätigkeit": taetigkeit,
        "Lieferant": lieferant,
        "Fehlerbild A": fehlerbild_a,
        "Fehlerbild B": fehlerbild_b,
        "Fehlerbild C": fehlerbild_c,
        "Fehlerbild D": fehlerbild_d,
        "Fehlerbild E": fehlerbild_e,
        "Fehlerbild F": fehlerbild_f,
        "FZG / Motorentyp": motorentyp,
        "KST": kst,
        "Tagesbedarf": tagesbedarf,
    
        "Abteilung": abteilung,
        "Auftraggeber": Auftraggeber,
        "Ansprechpartner Kunde": ansprechpartner_kunde,
        "Prüfort Werk": pruefort,
        "Arbeitsort(e)": arbeitsorte,
        "Sortierregel": sortierregel,
        "Koordinator": Koordinator,
    
        "Markierung": markierung,
        "PSA": psa,
        "Cop": cop_field_value,
    
        "Prüfablauf": beschreibung_pruefablauf
        "Gebots und Warnschilder": ", ".join(ausgewaehlte_bilder),
    
        # ✅ Page 7 – Freigabe Section
        "Freigabe Formel I": freigabe_bmw,
        "Zusatz": zusatz_qcat,
        "AA1": anweisungen,
    
        # ✅ Page 8 – Materialdaten Rows 1–2
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





    

        # Dynamisch erzeugtes image_fields Dictionary für spezifisches Mapping
    image_fields = {}
    
    field_counter = 2  # Start bei 2, weil "Bauteilbild2" die erste ist
    for i, img in enumerate(uploaded_bauteilbilder):
        image_fields[f"Bauteilbild{field_counter}"] = img
        field_counter += 1
    
        


    # Collect extra images
    uploaded_bauteilbilder = []
    for typ in ["Bauteilbild", "NIO-Bauteil", "Prüf-/Hilfsmittel", "Allgemeiner Prüfablauf", "IO-Markierung"]:
        for i in range(10):
            key = f"img_{typ}_{i}"
            if key in st.session_state and st.session_state[key] is not None:
                uploaded_bauteilbilder.append(st.session_state[key])


   


    # Output in memory (no saving to disk)
    pdf_output = BytesIO()
    fill_pdf_with_multiple_images("bbw_template_fillable.pdf", pdf_output, data, image_fields, extra_images)



    st.download_button(
        label="📥 PDF herunterladen",
        data=pdf_output.getvalue(),
        file_name=f"Arbeitsanweisung_{auftrag_bmw}.pdf",
        mime="application/pdf"
    )

    st.success("✅ Das Formular wurde erfolgreich abgegeben und als PDF generiert!")





from PyPDF2 import PdfReader
reader = PdfReader("bbw_template_fillable.pdf")
fields = reader.get_fields()
for name in fields:
    print(name)


    






   

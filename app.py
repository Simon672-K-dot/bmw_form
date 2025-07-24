
import streamlit as st
import pandas as pd
from datetime import datetime
import os
import fitz


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






# Unterhalb von Freigabe: vier Felder nebeneinander
col_freigabe, col_ids1, col_ids2, col_ids3 = st.columns(4)

with col_freigabe:
    freigabe_bmw = st.text_input("✅ Freigabe")
    rev_text = st.text_input("🔁 REV (erscheint auf jeder Seite)")


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
    fehlerbild_a = st.text_input("❌ Fehlerbild A")
    fehlerbild_b = st.text_input("❌ Fehlerbild B")
    fehlerbild_c = st.text_input("❌ Fehlerbild C")
    fehlerbild_d = st.text_input("❌ Fehlerbild D")
    fehlerbild_e = st.text_input("❌ Fehlerbild E")
    fehlerbild_f = st.text_input("❌ Fehlerbild F")
    
with col2:
    auftrag = st.text_input("📄 Auftrag")
    lieferant = st.text_input("🚚 Lieferant")
    kst = st.text_input("⚙️ KST")
    tagesbedarf = st.text_input("📦 Tagesbedarf")
    ansprechpartner_kunde = st.text_input("👤 Ansprechpartner Kunde")
    arbeitsorte = st.text_input("📍 Arbeitsort(e)")
    Werk = st.text_input("Prüfort Werk")
    

with col3:
    taetigkeit = st.text_input("🛠️ Tätigkeit")
    abteilung = st.text_input("🏷️ Abteilung")
    sortierregel = st.text_input("📑 Sortierregel")
    motorentyp = st.text_input("🚗 FZG / Motorentyp")
    Auftraggeber = st.text_input("👷 Auftraggeber")
    pruefort = st.text_input("🏭 Sortier-/Prüfort")
    Koordinator = st.text_input("Koordinator")
    AAW = st.text_input("AAW erstellt")
    


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



#Bild feld für Bild 1

st.markdown('<h3 style="background-color:#e1f5fe;padding:10px;">📸 Bauteilbild</h3>', unsafe_allow_html=True)
bauteilbild = st.file_uploader("Bild des Bauteils hochladen", type=["png", "jpg", "jpeg"], key="bauteilbild1")





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

    col_img, col_kommentar = st.columns([2, 1])

    with col_img:
        bild = st.file_uploader(
            f"📸 Bild für {typ} {index+1}",
            type=["jpg", "jpeg", "png"],
            key=f"img_{typ}_{index}"
        )
        if bild:
            st.image(bild, use_container_width=True)

    with col_kommentar:
        st.text_input("📝 Name (z. B. NIO-Bauteil, IO-Bauteil)", key=f"name_{typ}_{index}")
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





# 🔄 bilder

image_comment_blocks = []

# ✅ Add image from the first page (manually)
if "bauteilbild1" in st.session_state and st.session_state["bauteilbild1"]:
    image_comment_blocks.append({
        "image": st.session_state["bauteilbild1"],
        "comment": "",  # or: st.session_state.get("kommentar_erste_bild", "")
        "name": "Bauteilbild (Seite 1)"
    })

# ✅ Add image blocks from the expandable sections
for typ in ["Bauteilbild", "NIO-Bauteil", "Prüf-/Hilfsmittel", "Allgemeiner Prüfablauf", "IO-Markierung"]:
    i = 0
    image_key = f"img_{typ}_{i}"
    comment_key = f"kommentar_{typ}_{i}"
    name_key = f"name_{typ}_{i}"

    image = st.session_state.get(image_key)
    comment = st.session_state.get(comment_key)
    name = st.session_state.get(name_key)

    if image:
        image_comment_blocks.append({
            "image": image,
            "comment": comment or "",
            "name": name or ""
        })

        image_number = len(image_comment_blocks)  # e.g., 1, 2, 3, ...
        


if len(image_comment_blocks) > 4:
    st.warning("⚠️ Maximal 4 Bilder mit Kommentaren erlaubt – nur die ersten 4 werden übernommen.")
    image_comment_blocks = image_comment_blocks[:4]





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

# ✅ Save cleaned material data to session state
st.session_state["material_data"] = cleaned_df.to_dict(orient="records")




   




# --- FINAL SUBMIT BUTTON ---

#d bug 
from io import BytesIO

st.markdown("---")
st.markdown("### 🔍 PDF-Felder anzeigen (Debug Tool)")

if st.button("📋 Zeige PDF-Feldnamen (PyPDF2)"):
    from PyPDF2 import PdfReader
    import os

    pdf_path = "template.pdf"
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
    except Exception as e:
         st.warning(f"⚠️ Fehler beim Auslesen der Felder: {e}")









def fill_pdf_with_fields_and_images(field_data, image_comment_blocks, template_path="template.pdf", output_path="arbeitsanweisung_output.pdf"):
    doc = fitz.open(template_path)
    # ✅ Manually fill Bild1 on the first page (from image_comment_blocks[0])
    if len(image_comment_blocks) > 0:
        bild1_stream = image_comment_blocks[0]["image"]
        for page in doc:
            for widget in page.widgets():
                if widget.field_name == "Bild1":
                    rect = widget.rect
                    img_stream = bild1_stream.read()
                    page.insert_image(rect, stream=img_stream)
                    bild1_stream.seek(0)


    # Fill all shared fields (e.g. Auftrag, BI, Rev)
    for page in doc:
        for widget in page.widgets():
            field_name = widget.field_name
            if field_name in field_data:
                widget.field_value = str(field_data[field_name])
                widget.update()

    # Fill up to 4 image + comment + name fields
    # ✅ Corrected: Fill up to 4 image + comment + name fields
    # ✅ Fill image + comment + name starting from Bild2 on Page 2
    # ✅ Fill Bild1 from the first image only (no comment/name)
    if len(image_comment_blocks) > 0:
        block = image_comment_blocks[0]
        for page in doc:
            for widget in page.widgets():
                if widget.field_name == "Bild1":
                    rect = widget.rect
                    img_stream = block["image"].read()
                    page.insert_image(rect, stream=img_stream)
                    block["image"].seek(0)
                    break

    # ✅ Fill Bild2–Bild5, Kommentar1–4, Name1–4
    for i in range(1, min(5, len(image_comment_blocks))):
        block = image_comment_blocks[i]
        bild_field = f"Bild{i + 1}"          # Starts at Bild2
        kommentar_field = f"Kommentar{i}"    # Starts at Kommentar1
        name_field = f"Name{i}"              # Starts at Name1
    
        for page in doc:
            for widget in page.widgets():
                if widget.field_name == bild_field:
                    rect = widget.rect
                    img_stream = block["image"].read()
                    page.insert_image(rect, stream=img_stream)
                    block["image"].seek(0)
    
                elif widget.field_name == kommentar_field:
                    widget.field_value = block["comment"]
                    widget.update()
    
                elif widget.field_name == name_field:
                    widget.field_value = block["name"]
                    widget.update()



    doc.save(output_path)
    return output_path


# Save the material table input
st.session_state["material_data"] = cleaned_df.to_dict(orient="records")



if st.button("✅ Formular abgeben"):
    data = {
        # ✅ First Section (Pages 1–2)
        "Freigabe": freigabe_bmw,
        "Sortierstart": str(sortierstart),
        "AuftragsID": auftrags_id,
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
        "FZGMotorentyp": motorentyp,
        "KST": kst,
        "Tagesbedarf": tagesbedarf,
    
        "Abteilung": abteilung,
        "Auftraggeber": Auftraggeber,
        "Ansprechpartner Kunde": ansprechpartner_kunde,
        "Prüfort Werk": Werk,
        "Arbeitsorte": arbeitsorte,
        "Sortierregel": sortierregel,
        "Koordinator": Koordinator,
        "AAW erstellt":AAW,
    
        "MarkierungRow1": markierung,
        "PSARow1": ", ".join(ausgewaehlte_bilder), 
        "Cop": cop_field_value,
        "Zusätzliche InfosRow1": zusaetzliche_infos,
        "Rev":rev_text,
        "SortierPrüfort":pruefort,
    
        
        "BeschreibungPrüfablaufRow1": beschreibung_pruefablauf,
        "Gebots und Warnschilder": ", ".join(ausgewaehlte_bilder),
        "Rev Freigabe": freigabe_bmw,
        "AAW erstellt": AAW,


    }
    
    
   
    
    # ✅ Page 8 – Materialdaten Rows 1–2
    # ⬇️ material_data is your table (already collected from st.data_editor)
    material_data = st.session_state.get("material_data", [])

    for i, row in enumerate(material_data[:10]):  # Only handle first 10 rows
        row_index = i + 1  # Row1 to Row10
        
        data[f"MaterialnummerRow{row_index}"] = row.get("Materialnummer", "")
        data[f"MaterialbezeichnungRow{row_index}"] = row.get("Materialbezeichnung", "")
        data[f"LieferantRow{row_index}"] = row.get("Lieferant", "")
        data[f"FehlerortRow{row_index}"] = row.get("Fehlerort", "")
        data[f"FehlerartRow{row_index}"] = row.get("Fehlerart", "")
        data[f"BIRow{row_index}"] = row.get("BI", "")
    
      
    







    cop_text_lines = []

    if cop:
        cop_text_lines.append(f"cop: {cop}")
    if esd:
        cop_text_lines.append(f"esd: {esd}")
    if tecsa:
        cop_text_lines.append(f"tecsa: {tecsa}")
    
    data["COP"] = "\n".join(cop_text_lines)



    # ✅ Map image comments and names to PDF fields
    data["Kommentar1"] = image_comment_blocks[0]["comment"] if len(image_comment_blocks) > 0 else ""
    data["Kommentar2"] = image_comment_blocks[1]["comment"] if len(image_comment_blocks) > 1 else ""
    data["Kommentar3"] = image_comment_blocks[2]["comment"] if len(image_comment_blocks) > 2 else ""
    data["Kommentar4"] = image_comment_blocks[3]["comment"] if len(image_comment_blocks) > 3 else ""
    
    data["Name1"] = image_comment_blocks[0]["name"] if len(image_comment_blocks) > 0 else ""
    data["Name2"] = image_comment_blocks[1]["name"] if len(image_comment_blocks) > 1 else ""
    data["Name3"] = image_comment_blocks[2]["name"] if len(image_comment_blocks) > 2 else ""
    data["Name4"] = image_comment_blocks[3]["name"] if len(image_comment_blocks) > 3 else ""

    st.write("✅ FINAL DATA PASSED TO PDF:", data)




    cop_text_lines = []

    if cop:
        cop_text_lines.append(f"cop: {cop}")
    if esd:
        cop_text_lines.append(f"esd: {esd}")
    if tecsa:
        cop_text_lines.append(f"tecsa: {tecsa}")
    
    data["COP"] = "\n".join(cop_text_lines)

        

    
# Call your new function to generate the PDF
    output_path = fill_pdf_with_fields_and_images(
        data,
        image_comment_blocks,
        template_path="template.pdf",
        output_path="arbeitsanweisung_output.pdf"
    )

    # ✅ Show the download button
    with open(output_path, "rb") as f:
        st.download_button(
            "📥 PDF herunterladen",
            f,
            file_name=f"Arbeitsanweisung_{auftrags_id}.pdf",  # 👈 here
            mime="application/pdf"
        )



    st.success("✅ Das Formular wurde erfolgreich abgegeben und als PDF generiert!")











    

from PyPDF2 import PdfReader
reader = PdfReader("template.pdf")
fields = reader.get_fields()
for name in fields:
    print(name)







import fitz  # PyMuPDF



def fill_pdf_with_fields_and_images(field_data, image_comment_blocks, template_path="template.pdf", output_path="arbeitsanweisung_output.pdf"):
    doc = fitz.open(template_path)

    # Fill all shared fields (e.g. Auftrag, BI, Rev)
    for page in doc:
        for widget in page.widgets():
            field_name = widget.field_name
            if field_name in field_data:
                widget.field_value = str(field_data[field_name])
                widget.update()

    # Fill up to 4 image + comment + name fields
    for i, block in enumerate(image_comment_blocks):
        index = i + 1  # for Bild1, Kommentar1, Name/Name2...

        bild_field = f"Bild{index}"
        kommentar_field = f"Kommentar{index}"
        name_field = "Name" if index == 1 else f"Name{index}"
        print(f"🔍 Filling {kommentar_field} = '{block['comment']}'")
        print(f"🔍 Filling {name_field} = '{block['name']}'")


        for page in doc:
            for widget in page.widgets():
                if widget.field_name == bild_field:
                    rect = widget.rect
                    img_stream = block["image"].read()
                    page.insert_image(rect, stream=img_stream)
                    block["image"].seek(0)  # Reset stream in case reused

                elif widget.field_name == kommentar_field:
                    widget.field_value = block["comment"]
                    widget.update()

                elif widget.field_name == name_field:
                    widget.field_value = block["name"]
                    widget.update()

    doc.save(output_path)
    return output_path


    






   

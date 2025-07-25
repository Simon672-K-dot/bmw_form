# BMW Arbeitsanweisung Tool

Dieses Tool vereinfacht das Erstellen von **Arbeitsanweisungen** bei der Teileprüfung. Es ersetzt das alte Excel-Formular durch ein digitales Formular und erzeugt automatisch eine ausgefüllte PDF-Datei.

---

## ✅ Was ist enthalten?

| Datei               | Beschreibung |
|--------------------|--------------|
| `app.py`           | Das Programm, das das digitale Formular zeigt (Streamlit-App) |
| `template.pdf`     | Die offizielle PDF-Vorlage, die automatisch ausgefüllt wird |
| `requirements.txt` | Liste der Programme (Python-Pakete), die zum Ausführen benötigt werden |
| `images/`          | Enthält Bilder, z. B. für PSA-Symbole wie Fußschutz oder Warnweste |
| `README.md`        | Diese Anleitung |

---

## ▶️ Wie funktioniert das?

1. Man öffnet ein Formular im Browser (nach Start des Programms).
2. Man füllt alle Felder aus, z. B. Auftrags-ID, BI, Kommentare.
3. Es können bis zu 7 Bilder mit Kommentaren hinzugefügt werden.
4. Ein Klick auf **„Formular abgeben“** erzeugt die finale PDF.
5. Die PDF enthält automatisch alle Angaben und Bilder, passend zum BMW-Layout.

---

## 💡 Technischer Hintergrund (einfach erklärt)

- Das Tool wurde mit **Python** und **Streamlit** programmiert.
- Es nutzt eine PDF-Vorlage (`template.pdf`) und füllt die Felder automatisch mit den eingegebenen Daten.
- Alle Felder (z. B. Auftrags-ID, BI, Rev, Kommentare) werden **direkt in die PDF geschrieben**.
- Das Tool kann auf einem Laptop oder einem internen BMW-Server ausgeführt werden.

---

## 🛠️ Wie kann man es starten?

### Voraussetzungen:
- Python ist installiert (Version 3.8 oder höher)
- Internetzugang für einmaliges Installieren der Pakete

### Schritte:

1. **Pakete installieren** (nur beim ersten Mal):

```bash
pip install -r requirements.txt
```

2. **Tool starten**:

```bash
streamlit run app.py
```

3. Formular wird im Browser geöffnet:
   `http://localhost:8501`

---

## 🔐 Hinweis

- Das Formular ist durch ein Passwort geschützt: **bmw2025**
- Dieses Passwort kann in der Datei `app.py` geändert werden

---

Bei Fragen zur Benutzung → Simon kontaktieren 😉

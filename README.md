---

# 📇 CSV → VCF Converter

Easily convert a simple **CSV roster** into a single `.vcf` (vCard) file you can import into **📱 iPhone**, **🤖 Android**, **📧 Outlook**, or **📂 Google Contacts (Gmail)**.

---

## ✨ Features

* 🔄 Convert a CSV with **first name, last name, desk phone, cell phone, and email**
* 📂 Output a **single `.vcf` file** containing all contacts
* 📱 Works with **iPhone**, **Android**, **Outlook**, and **Gmail**
* ⚡ Uses **vCard 3.0** (widely compatible)
* 🧹 Skips empty rows automatically
* 🛡️ Escapes special characters safely (commas, semicolons, etc.)

---

## 📂 CSV Format

Your CSV **must include a header row** exactly like this:

```csv
first_name,last_name,desk_phone,cell_phone,email
Jane,Doe,555-123-4567,555-987-6543,jane.doe@example.com
John,Smith,555-222-3333,,john.smith@example.com
Alex,Johnson,,555-444-5555,alex.j@example.org
Maria,Gonzalez,555-888-9999,555-111-2222,maria.g@example.com
```

✅ Tips:

* Leave cells blank if data is missing (`cell_phone`, `desk_phone`, or `email`)
* Save/export as **UTF-8 CSV** if possible

---

## ⚙️ Usage

### 1️⃣ Install Python

Check Python is installed:

```bash
python --version
```

or

```bash
python3 --version
```

---

### 2️⃣ Run the Script

**Windows (PowerShell):**

```powershell
cd "C:\Users\sam\OneDrive\Hobbies\GitHub\csv2vcf"
python csv_to_vcf.py "G35 Roster.csv" "G35-roster.vcf"
```

**macOS / Linux (Terminal):**

```bash
cd ~/path/to/csv2vcf
python3 csv_to_vcf.py "G35 Roster.csv" "G35-roster.vcf"
```

* `csv_to_vcf.py` → the script
* `"G35 Roster.csv"` → your input CSV
* `"G35-roster.vcf"` → output file (all contacts combined)

---

## 📥 Importing Contacts

### 🍏 iPhone

* **Option 1 – Email:** Email the `.vcf`, open it on iPhone → **Add All Contacts**
* **Option 2 – AirDrop:** AirDrop from Mac → Accept → **Add All Contacts**
* **Option 3 – iCloud:** [iCloud.com → Contacts](https://www.icloud.com/) → ⚙️ → **Import vCard**

---

### 🤖 Android

1. Copy `.vcf` to your phone (USB, Drive, or email)
2. Open **Contacts** app
3. Tap ⋮ → **Import/Export** → Import from `.vcf`
4. Select your file

---

### 📧 Outlook

**Desktop (Windows):**

* File → **Open & Export → Import/Export** → **Import a VCARD file (.vcf)**

**Web (Outlook.com / Office 365):**

* [Outlook People](https://outlook.live.com/people/) → **Manage → Import contacts** → Select `.vcf`

---

### 📂 Google Contacts (Gmail)

1. Go to [Google Contacts](https://contacts.google.com/)
2. Click **Import** (left menu)
3. Select your `.vcf` file
4. Contacts sync automatically to Android if Google Contacts is enabled

---

## 📝 Example Output

From the sample CSV above, the `.vcf` will look like this:

```text
BEGIN:VCARD
VERSION:3.0
N:Doe;Jane;;;
FN:Jane Doe
TEL;TYPE=WORK:555-123-4567
TEL;TYPE=CELL:555-987-6543
EMAIL;TYPE=INTERNET:jane.doe@example.com
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Smith;John;;;
FN:John Smith
TEL;TYPE=WORK:555-222-3333
EMAIL;TYPE=INTERNET:john.smith@example.com
END:VCARD
```

---

## 🛠️ Troubleshooting

⚠️ **Common Issues & Fixes**

* ❌ **Only the first contact appears on iPhone**
  → Ensure there are **no blank lines** between `END:VCARD` and `BEGIN:VCARD`. The script already prevents this.

* ❌ **File won’t import**
  → Check that it ends with `.vcf` and headers are correct (`first_name,last_name,desk_phone,cell_phone,email`).

* ❌ **Special characters look wrong**
  → Save CSV as **UTF-8 encoding**.

* ❌ **Command errors**
  → Make sure you run the script, not the CSV itself:

  ```powershell
  python csv_to_vcf.py "contacts.csv" "contacts.vcf"
  ```

  ✅ NOT

  ```powershell
  python "contacts.csv" contacts.vcf
  ```

* ❌ **Spaces in filenames**
  → Always wrap filenames in quotes: `"EvilCorps Roster.csv"`

---

Do you also want me to add a **Quick Start (3 steps only)** section at the top for users who just want the short version?

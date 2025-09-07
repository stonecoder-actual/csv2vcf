````markdown
# 📇 CSV to VCF Converter

Convert a simple CSV roster into a single `.vcf` (vCard) file that can be imported into **iPhone**, **Android**, and **Outlook** contacts.

---

## ✨ Features
- Takes a CSV with **first name, last name, desk phone, cell phone, and email**
- Generates a **single `.vcf` file** with all contacts
- Compatible with **vCard 3.0** (works across iPhone, Android, Outlook, Gmail, iCloud)
- Skips empty rows
- Escapes special characters safely (commas, semicolons, etc.)

---

## 📂 CSV Format

Your CSV must include a **header row** exactly like this:

```csv
first_name,last_name,desk_phone,cell_phone,email
Jane,Doe,555-123-4567,555-987-6543,jane.doe@example.com
John,Smith,555-222-3333,,john.smith@example.com
Alex,Johnson,,555-444-5555,alex.j@example.org
Maria,Gonzalez,555-888-9999,555-111-2222,maria.g@example.com
````

* Leave cells blank if data is missing (`cell_phone`, `desk_phone`, or `email`).
* Save/export the file as `UTF-8 CSV` if possible.

---

## ▶️ Usage

### 1. Install Python

Make sure you have Python 3 installed. Check with:

```bash
python --version
```

or

```bash
python3 --version
```

### 2. Run the script

From PowerShell (Windows):

```powershell
cd "C:\Users\sam\OneDrive\Hobbies\GitHub\csv2vcf"
python csv_to_vcf.py "G35 Roster.csv" "G35-roster.vcf"
```

From macOS / Linux:

```bash
cd ~/path/to/csv2vcf
python3 csv_to_vcf.py "G35 Roster.csv" "G35-roster.vcf"
```

* `csv_to_vcf.py` → the script
* `"G35 Roster.csv"` → your input CSV
* `"G35-roster.vcf"` → output file (all contacts combined)

---

## 📱 Importing into iPhone

**Option 1 – Email**

1. Email the `.vcf` file to yourself.
2. Open the email on iPhone.
3. Tap the attachment → **Add All Contacts**.

**Option 2 – AirDrop**

1. AirDrop the `.vcf` file from a Mac to your iPhone.
2. Tap **Accept** → **Add All Contacts**.

**Option 3 – iCloud**

1. Go to [iCloud.com → Contacts](https://www.icloud.com/).
2. Click the ⚙️ gear → **Import vCard**.
3. Choose your `.vcf`.
4. Contacts will sync to your iPhone automatically.

---

## 📱 Importing into Android

1. Copy the `.vcf` to your phone (via USB, Google Drive, or email).
2. Open the **Contacts** app.
3. Tap ⋮ (menu) → **Import/Export** → Import from `.vcf`.
4. Select the file.

---

## 📧 Importing into Outlook

### Outlook Desktop (Windows)

1. Open Outlook.
2. Go to **File → Open & Export → Import/Export**.
3. Choose **Import a VCARD file (.vcf)**.
4. Select your `.vcf`.
5. Contacts will be added to your Outlook address book.

### Outlook on the Web (Outlook.com / Office 365)

1. Go to [Outlook.com People](https://outlook.live.com/people/).
2. Select **Manage → Import contacts**.
3. Choose **Browse** → select your `.vcf`.
4. Click **Import**.

---

## ✅ Example Output

For the above CSV, the `.vcf` will look like this:

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

* **Only the first contact appears on iPhone**
  Make sure there are **no blank lines between `END:VCARD` and `BEGIN:VCARD`**. The script already ensures this.

* **File won’t import**
  Verify it ends with `.vcf`, and the CSV headers are correct (`first_name,last_name,desk_phone,cell_phone,email`).

* **Special characters look wrong**
  Ensure your CSV is saved as **UTF-8** encoding.

* **Command errors**
  Make sure you are running the script, not the CSV. Example:

  ```powershell
  python csv_to_vcf.py "contacts.csv" "contacts.vcf"
  ```

  **NOT**

  ```powershell
  python "contacts.csv" contacts.vcf
  ```

* **Spaces in filenames**
  Always wrap filenames with quotes if they have spaces (e.g., `"G35 Roster.csv"`).

```

Would you like me to also add **Google Contacts (Gmail)** import steps so Android users who sync via Gmail can follow along?
```

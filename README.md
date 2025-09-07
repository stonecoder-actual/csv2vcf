# 📇 CSV to VCF Converter

Convert a simple CSV roster into a single `.vcf` (vCard) file that can be imported into **iPhone** and **Android** contacts.

---

## ✨ Features
- Takes a CSV with **first name, last name, desk phone, cell phone, and email**
- Generates a **single `.vcf` file** with all contacts
- Compatible with **vCard 3.0** (best for Android & iOS)
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

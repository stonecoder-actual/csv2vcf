import csv
import sys
from pathlib import Path

def esc(s: str) -> str:
    """Escape vCard special characters: backslash, semicolon, comma, newline."""
    return (
        (s or "")
        .replace("\\", "\\\\")
        .replace(";", r"\;")
        .replace(",", r"\,")
        .replace("\n", r"\n")
        .replace("\r", "")
    )

def build_vcard(row: dict) -> str:
    first = (row.get("first_name") or "").strip()
    last  = (row.get("last_name") or "").strip()
    fn = f"{first} {last}".strip()

    desk = (row.get("desk_phone") or "").strip()
    cell = (row.get("cell_phone") or "").strip()
    email = (row.get("email") or "").strip()

    lines = []
    lines.append("BEGIN:VCARD")
    lines.append("VERSION:3.0")
    lines.append(f"N:{esc(last)};{esc(first)};;;")
    lines.append(f"FN:{esc(fn)}")

    if desk:
        lines.append(f"TEL;TYPE=WORK:{esc(desk)}")
    if cell:
        lines.append(f"TEL;TYPE=CELL:{esc(cell)}")
    if email:
        lines.append(f"EMAIL;TYPE=INTERNET:{esc(email)}")

    lines.append("END:VCARD")
    return "\n".join(lines)

def main():
    if len(sys.argv) < 3:
        print("Usage: python csv_to_vcf.py contacts.csv all_contacts.vcf")
        sys.exit(1)

    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    with in_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        vcards = [build_vcard(row) for row in reader if any(row.values())]

    # Join WITHOUT an extra trailing newline
    content = "\n".join(vcards)
    out_path.write_text(content, encoding="utf-8")

    print(f"✅ Wrote {len(vcards)} contacts to {out_path}")

if __name__ == "__main__":
    main()

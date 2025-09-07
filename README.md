📇 CSV to VCF Converter

Convert a simple CSV roster into a single .vcf (vCard) file that can be imported into iPhone, Android, Outlook, and Google Contacts (Gmail).

Features

Convert a CSV with first name, last name, desk phone, cell phone, and email

Output a single .vcf file containing all contacts

Uses vCard 3.0 (widely compatible across iPhone, Android, Outlook, Gmail, iCloud)

Skips empty rows automatically

Escapes special characters safely (commas, semicolons, etc.)

CSV Format

The CSV must include a header row exactly like this:

first_name,last_name,desk_phone,cell_phone,email
Jane,Doe,555-123-4567,555-987-6543,jane.doe@example.com
John,Smith,555-222-3333,,john.smith@example.com
Alex,Johnson,,555-444-5555,alex.j@example.org
Maria,Gonzalez,555-888-9999,555-111-2222,maria.g@example.com


Leave cells blank if data is missing (cell_phone, desk_phone, or email)

Save/export the file as UTF-8 CSV if possible

Usage
1. Install Python

Check your Python installation:

python --version


or

python3 --version

2. Run the Script

Windows (PowerShell):

cd "C:\Users\sam\OneDrive\Hobbies\GitHub\csv2vcf"
python csv_to_vcf.py "G35 Roster.csv" "G35-roster.vcf"


macOS / Linux (Terminal):

cd ~/path/to/csv2vcf
python3 csv_to_vcf.py "G35 Roster.csv" "G35-roster.vcf"


csv_to_vcf.py → the script

"G35 Roster.csv" → your input CSV

"G35-roster.vcf" → output file (all contacts combined)

Importing Contacts
iPhone

Option 1 – Email

Email the .vcf file to yourself

Open the email on iPhone

Tap the attachment → Add All Contacts

Option 2 – AirDrop

AirDrop the .vcf file from a Mac to your iPhone

Tap Accept → Add All Contacts

Option 3 – iCloud

Go to iCloud.com → Contacts

Click the ⚙️ gear → Import vCard

Choose your .vcf

Contacts will sync to your iPhone automatically

Android

Copy the .vcf to your phone (via USB, Google Drive, or email)

Open the Contacts app

Tap ⋮ (menu) → Import/Export → Import from .vcf

Select the file

Outlook

Outlook Desktop (Windows):

Open Outlook

Go to File → Open & Export → Import/Export

Choose Import a VCARD file (.vcf)

Select your .vcf

Contacts will be added to your Outlook address book

Outlook on the Web (Outlook.com / Office 365):

Go to Outlook.com People

Select Manage → Import contacts

Choose Browse → select your .vcf

Click Import

Google Contacts (Gmail)

Open Google Contacts

On the left menu, click Import

Choose Select File and pick your .vcf

Click Import

If your phone syncs with Google Contacts, the contacts will appear automatically

Example Output

For the sample CSV above, the .vcf file will look like this:

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

Troubleshooting

Only the first contact appears on iPhone
Ensure there are no blank lines between END:VCARD and BEGIN:VCARD. The script already ensures this.

File won’t import
Confirm the file ends with .vcf and the CSV headers are correct (first_name,last_name,desk_phone,cell_phone,email).

Special characters look wrong
Save your CSV as UTF-8 encoding.

Command errors
Make sure you run the script, not the CSV file. Example:

python csv_to_vcf.py "contacts.csv" "contacts.vcf"


NOT

python "contacts.csv" contacts.vcf


Spaces in filenames
Always wrap filenames with quotes if they contain spaces (e.g., "EvilCorps Roster.csv")

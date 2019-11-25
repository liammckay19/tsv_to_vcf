# tsv_to_vcf
Converts a TSV (Tab Separated Values) table into a Virtual Contact File (VCF)

Currently, only supports Group, Email, Name fields.

Example input file:

| Group     | Email            | Name       |
|-----------|------------------|------------|
| GroupName | name@example.com | First Last |

Example output file:

```BEGIN:VCARD
VERSION:3.0
N:Spaceseparated; Nameis;;;
FN: NAMEIS SPACESEPARATED
ORG: ORG;
EMAIL: EMAIL@EMAIL.COM
END:VCARD

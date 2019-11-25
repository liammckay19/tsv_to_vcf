import glob
import io
import sys

import os

VCARD_FORMAT="BEGIN:VCARD\nVERSION:3.0\nN:{LAST}; {FIRST};;;\nFN: {FULLNAME}\nORG: {ORG};\nEMAIL: {EMAIL}\nEND:VCARD\n"

def main():
	outputCount = 0
	if not os.path.exists("outputVCFs"):
		os.mkdir("outputVCFs")
		print("Output location: outputVCFs/ directory")
	with open(glob.glob('*.tsv')[0], 'r') as group_email_name:
		print("selected TSV file: "+glob.glob('*.tsv')[0])
		for row in group_email_name.readlines():
			row=row.rstrip()
			try:
				group, email, name = row.split("\t")
			except ValueError:
				if len(row.split("\t")) == 2:
					group, email = row.split("\t")
					name = email
				else:
					print("couldnt parse \""+row+"\". continuing...")
					continue
			if len(name.split(" ")) == 2:
				first, last = name.split(" ")
				first = first.capitalize().rstrip()
				last = last.capitalize().rstrip()
			else:
				first = name.capitalize()
				last = name.capitalize()

			with open("outputVCFs/"+email+".vcf", 'w') as vcard_file:
				if name =="":
					name=email
					first=email
					last=email
				vcard_file.write(VCARD_FORMAT.format(
					FIRST=first.rstrip(),
					LAST=last.rstrip(),
					FULLNAME=name.rstrip(),
					EMAIL=email.rstrip(),
					ORG=group.rstrip()))
				outputCount+=1 
	print("wrote "+str(outputCount)+" vcf files")


main()
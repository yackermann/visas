import os
import json

bfolder = "data/geo"
print("Starting validating " + bfolder + "/")
for file in os.listdir(bfolder):
	if file.endswith(".geo.json"):
		try:
			data = ""
			with open(bfolder + "/"+ file) as f:
				data = json.loads(f.read())

			with open(bfolder + "/"+ file, "w") as w:
				w.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
		except:
			print("Error while validating file: " + bfolder + "/" + file)
print("Validation of " + bfolder + "/ completed.\n")


vfolder = "data/visa"
print("Starting validating " + vfolder + "/")
for file in os.listdir(vfolder):
	if file.endswith(".visa.json"):
		try:
			data = ""
			with open(vfolder + "/"+ file) as f:
				data = json.loads(f.read())

			with open(vfolder + "/"+ file, "w") as w:
				w.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
		except:
			print("Error while validating file: " + bfolder + "/" + file)

print("Validation of " + vfolder + "/ completed.")
import os
import json

bfolder = "data"
for file in os.listdir(bfolder):
	if file.endswith(".geo.json"):
		data = ""
		with open(bfolder + "/"+ file) as f:
			data = json.loads(f.read())

		with open(bfolder + "/"+ file, "w") as w:
			w.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
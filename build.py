import os
import json
import datetime

data = {
	"type" : "FeatureCollection",
	"features": []
}
bfolder = "data"
for file in os.listdir(bfolder):
	if file.endswith(".geo.json"):
		with open(bfolder + "/"+ file) as f:
			data["features"].append(json.loads(f.read())["features"][0])

data["build_time"] = datetime.datetime.utcnow().isoformat()

with open("dist/world.geo.json", "w") as w:
	w.write(json.dumps(data))

with open("countries.json") as f:
	with open("dist/countries.json","w") as w:
		w.write(json.dumps(json.loads(f.read())))
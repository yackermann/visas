import os
import json
import datetime

data = {
	"type" : "FeatureCollection",
	"features": []
}
bfolder = "countries"
for file in os.listdir(bfolder):
	if file.endswith(".geo.json"):
		with open(bfolder + "/"+ file) as f:
			data["features"].append(json.loads(f.read()))


data["build_time"] = datetime.datetime.utcnow().isoformat()

with open("world.geo.json", "w") as w:
	w.write(json.dumps(data))
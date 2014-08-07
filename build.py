import os
import json
import datetime

geodata = {
	"type" : "FeatureCollection",
	"features": []
}
timestamp = datetime.datetime.utcnow().isoformat()


bfolder = "data/geo"
for file in os.listdir(bfolder):
	if file.endswith(".geo.json"):
		with open(bfolder + "/"+ file) as f:
			geodata["features"].append(json.loads(f.read())["features"][0])

geodata["build_time"] = timestamp
with open("dist/world.geo.json", "w") as w:
	w.write(json.dumps(geodata))



visadata = []
vfolder = "data/visa"
for file in os.listdir(vfolder):
	if file.endswith(".visa.json"):
		with open(vfolder + "/"+ file) as f:
			visadata.append(json.loads(f.read()))

with open("dist/world.visa.json","w") as w:
	w.write(json.dumps(visadata))


with open("data/info/countries.json") as f:
	with open("dist/countries.json","w") as w:
		w.write(json.dumps(json.loads(f.read())))
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


countries_g = []
countries_v = []
countries = {}
 
visas = []
 
countries_temp = ""
visas_temp = ""
geo_temp = ""
 
todo = ""
with open("dist/world.visa.json") as f:
	visas_temp = json.loads(f.read())
 
with open("dist/world.geo.json") as f:
	geo_temp = json.loads(f.read())
 
with open("dist/countries.json") as f:
	countries_temp = json.loads(f.read())
 
for i in countries_temp:
	countries[i["cca2"]] = i["name"]
	countries_g.append(i['cca2'])
	countries_v.append(i['cca2'])
 
 
todo += "### Todo for visa data\n"
for i in visas_temp:
	if i['cca2'] in countries_v:
		countries_v.remove(i['cca2'])
 
for i in countries_v:
	todo += "- " + i + " : " + countries[i] + "\n"
 
todo += "\n### Todo for geo data\n"

for i in geo_temp["features"]:
	if i["id"] in countries_g:
		countries_g.remove(i["id"])

for i in countries_g:
	todo += "- " + i + " : " + countries[i] + "\n"

with open("TODO.md","w") as w:
	w.write(todo)
visas in JSON
==============

##### A **visa** data progect

##### What do I do in this project?
* I provide data about visa requirements for citizens of a different countries.
* I provide geographical data according to the **[de facto](https://en.wikipedia.org/wiki/De_facto)**, not **[de jure](https://en.wikipedia.org/wiki/De_jure)** status of territory.
* If you need geo data with **de jure** status, please use https://github.com/mledoze/countries
* This is an **apolitical** project.

##### Where I can find the data?
* Geo data is in **data/geo/** folder
* Visa data is in **visa/geo/** folder
* Countries data in **data/info/countries.json**
* Compressed version of the data can be found in **dist/** folder

##### Contribution: 
* Any kind of contribuion is welcome. Specially at kipping visa information up to date.

##### Visa types:
* u - Customs union(e.g. Schengen Zone)
* f - Visa not required
* e - Electronic visa required(e.g. ESTA, ETA)
* o - Visa getting obtained online
* a - Visa on arrival
* r - Visa required
* d - Visa refused(e.g.Iran visa for citizens of Israel)

##### Building data:
* Run <code>tool.py build</code> to build compressed version of all countries.
* Run <code>tool.py build --validate</code> to validate your json and make it nicely aligned.

##### Modifying data:
* Run <code>tool.py visa add \<cca2\> \<name\></code> to add new visa.
* Run <code>tool.py visa set \<visa_type\> \<from-cca2\> \(--cross \| --requirement \| --policy\) \<to-cca2\>...</code> to set visa requirement for country to country(s).
* Run <code>tool.py visa rm \<cca2\></code> to remove visa.

##### Other projects used:
* https://github.com/mledoze/countries
* https://github.com/docopt/docopt

##### Useful links:
* http://geojson.io/
* http://geojson.org/
* http://docopt.org/
* https://en.wikipedia.org/wiki/Category:Visa_requirements_by_nationality

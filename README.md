DFGD - De facto geo data
==============

##### A **de-facto** geo data progect

##### What do I do in this project?
* I provide data about visa requirements for citizens of a different countries.
* I provide geographical data according to the **[de facto](https://en.wikipedia.org/wiki/De_facto)**, not **[de jure](https://en.wikipedia.org/wiki/De_jure)** status of territory.
* If you need geo data with **de jure** status, use https://github.com/mledoze/countries
* This is an **apolitical** project.

##### Where I can find the data?
* Geo data is in **data/geo/** folder
* Visa data is in **visa/geo/** folder
* Countries data in **data/info/countries.json**
* Compressed version of the data can be found in **dist/** folder

##### Contribution: 
* Any kind of contribuion is welcome. Specially at kipping visa information up to date.

##### Building the data.
* Run <code>tool.py build</code> to build compressed version of all countries.
* Run <code>tool.py build --validate</code> to validate your json and make it nicely aligned.

##### Other projects used:
* https://github.com/mledoze/countries

##### Useful links:
* http://geojson.io/
* http://geojson.org/
* https://en.wikipedia.org/wiki/Category:Visa_requirements_by_nationality
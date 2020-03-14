# py-corona.py
simple parser for data about corona virus concerning Greece


data from : 

https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6


specific data from: 

https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Z7biAeD8PAkqgmWhxG2A/FeatureServer/1/query?f=json&where=(Confirmed%20%3E%200)%20AND%20(Country_Region%3D%27Greece%27)&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc%2CCountry_Region%20asc%2CProvince_State%20asc&outSR=102100&resultOffset=0&resultRecordCount=250&cacheHint=true

Instructions for install:
* create a virtualenv
* pip install -r requirements.txt

Example usage:
* python py_corona.py 

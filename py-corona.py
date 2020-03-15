import datetime
import requests
import time
import os
from datetime import timedelta

URL = "https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Z7biAeD8PAkqgmWhxG2A/FeatureServer/1/query?f=json&where=(Confirmed%20%3E%200)%20AND%20(Country_Region%3D%27Greece%27)&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc%2CCountry_Region%20asc%2CProvince_State%20asc&outSR=102100&resultOffset=0&resultRecordCount=250&cacheHint=true"


def time_setup(datatime):
    datetimeFormat = "%m/%d/%Y %H:%M:%S"
    time_now = time.strftime(datetimeFormat, time.localtime())
    time_last_update = time.strftime(datetimeFormat, time.localtime(datatime / 1000.0))
    time_diff = datetime.datetime.strptime(
        time_now, datetimeFormat
    ) - datetime.datetime.strptime(time_last_update, datetimeFormat)
    print("time now    : ", time_now)
    print("last update : ", time_last_update)


def get_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        data = data["features"][0]["attributes"]
        time_setup(data["Last_Update"])
    else:
        data = None
        print(response.status_code)
    return data


def main():
    data = get_info(URL)
    if data:
        items = ["Country_Region", "Confirmed", "Active", "Recovered", "Deaths"]
        for item in items:
            print(item, data[item])


main()

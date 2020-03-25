import argparse
import datetime
import requests
import sys
import time
from dateutil import parser

URL = "https://bing.com/covid/data?IG=7C3AD603E5764F8585272A649F2A0E5B"


def time_setup(datatime, iso=False):
    datetimeFormat = "%Y-%m-%d %H:%M:%S"
    time_now = time.strftime(datetimeFormat, time.localtime())

    if not iso:
        time_last_update = time.strftime(datetimeFormat, time.localtime(datatime / 1000.0))
    else:
        datatime=datatime[:19]
        time_last_update = parser.isoparse(datatime)

    time_diff = datetime.datetime.strptime(
        time_now, datetimeFormat
    ) - datetime.datetime.strptime(str(time_last_update), datetimeFormat)

    print("Time Now         : {} \nLast Update      : {} \nTime DIFF        : {}".format(time_now, time_last_update, time_diff))


def get_info(url, country):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        sys.exit("ERROR : {} : {}".format(response.status_code, URL))
    data = response.json()
    data = data['areas']
    coun=[]
    for item in range(len(data)):
        if country in data[item]['id']:
            country_data = data[item]

    time_setup(country_data['lastUpdated'], iso=True)
    return country_data


def all_countries(country=None):
    countries = ['chinamainland', 'italy', 'unitedstates', 'spain', 'germany', 'iran', 'france',
        'southkorea', 'switzerland', 'unitedkingdom', 'netherlands', 'austria', 'belgium', 'norway',
        'sweden', 'denmark', 'canada', 'portugal', 'malaysia', 'brazil', 'australia', 'japan',
        'czechrepublic', 'turkey', 'israel', 'ireland', 'pakistan', 'diamondprincess', 'luxembourg',
        'chile', 'poland', 'ecuador', 'greece', 'finland', 'qatar', 'iceland', 'indonesia', 'singapore',
        'thailand', 'saudiarabia', 'slovenia', 'philippines', 'romania', 'peru', 'india', 'bahrain',
        'russia', 'estonia', 'egypt', 'hongkong', 'panama', 'southafrica', 'lebanon', 'argentina', 'iraq',
        'colombia', 'croatia', 'mexico', 'slovakia', 'kuwait', 'serbia', 'bulgaria', 'armenia',
        'sanmarino', 'taiwan', 'unitedarabemirates', 'algeria', 'latvia', 'costarica', 'dominicanrepublic',
        'uruguay', 'hungary', 'jordan', 'morocco', 'bosniaandherzegovina', 'vietnam', 'andorra',
        'northmacedonia', 'brunei', 'moldova', 'albania', 'belarus', 'cyprus', 'malta', 'srilanka',
        'venezuela', 'lithuania', 'newzealand', 'burkinafaso', 'tunisia', 'kazakhstan', 'azerbaijan',
        'cambodia', 'oman', 'georgia', 'palestinianauthority', 'ukraine', 'senegal', 'uzbekistan',
        'liechtenstein', 'cameroon', 'bangladesh', 'afghanistan', 'honduras', 'congodrc', 'nigeria',
        'paraguay', 'cuba', 'ghana', 'kosovo', 'bolivia', 'jamaica', 'guatemala', 'guernsey', 'macau',
        'rwanda', 'togo', 'jersey', 'ctedivoire', 'kyrgyzstan', 'mauritius', 'montenegro', 'maldives',
        'monaco', 'mongolia', 'ethiopia', 'trinidadandtobago', 'kenya', 'seychelles', 'equatorialguinea',
        'tanzania', 'barbados', 'bahamas', 'gabon', 'guyana', 'suriname', 'capeverde',
        'centralafricanrepublic', 'elsalvador', 'madagascar', 'liberia', 'namibia', 'zimbabwe', 'angola',
        'benin', 'bhutan', 'fiji', 'haiti', 'isleofman', 'mauritania', 'nicaragua', 'saintlucia', 'sudan',
        'zambia', 'antiguaandbarbuda', 'chad', 'djibouti', 'eritrea', 'eswatini', 'guinea', 'nepal', 'niger',
        'papuanewguinea', 'stvincentandthegrenadines', 'somalia', 'uganda', 'vaticancity']
    if country in countries:
        return country
    else:
        print("INFO : available countries :\n", countries)
        sys.exit("ERROR : finding country {} in available countries".format(country))

def main():
    parser = argparse.ArgumentParser(
    description="""search statistics for corona virus in bing Example Usage:
    python py-corona.py --c greece"""
    )
    parser.add_argument("--country", metavar="--c", type=str, default='greece', help="enter country name")
    args = parser.parse_args()
    country = args.country.lower()
    all_countries(country)

    data = get_info(URL, country)

    items = ['displayName', 'totalConfirmed', 'totalRecovered', 'totalDeaths']
    for i in items:
        print ('{} : '.format(i), data[i])


main()

# py-corona.py
simple parser for data about corona virus concerning Greece  
due to unstable api backend, furher development was halted


data from :
https://bing.com/covid/data?IG=7C3AD603E5764F8585272A649F2A0E5B


Instructions for install:
* create a virtualenv
* pip install -r requirements.txt

Example usage:
print a help message:
* python py-corona.py --help

get data for greece:
* python py_corona.py --c greece

print all available countries:
* python py_corona.py --c wrong_country_name


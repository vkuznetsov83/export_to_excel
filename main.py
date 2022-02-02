from urllib import response
import openpyxl
import requests
import datetime
import json

with open('test_data.json') as file:
    data = json.load(file)
print(data)
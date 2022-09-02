import pandas as pd
import requests

class Main:
    def __init__(self):
        global ticker 
        global apiKey
        ticker=input("Select ticker: ")
        apiKey="71d797ce96bd5189d62ea531ef4f847d"

    def getCFS():    
        global apiKey
        get_cfs=requests.get(f"fhttps://fmpcloud.io/api/v3/cash-flow-statement/AAPL?limit=120&apikey={apiKey}").json()
        print(get_cfs)

    
    def calcCFS():
        return None
o=Main()
o.getCFS


        




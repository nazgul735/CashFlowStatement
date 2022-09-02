import request 
import pandas as pd

class Main:
    def __init__(self):
        global ticker 
        global apiKey
        ticker=input("Select ticker: ")
        apiKey=""

    def getCFS():    
        return f"https://fmpcloud.io/api/v3/cash-flow-statement/{ticker}?limit=120&apikey={apiKey}"

    
    def calcCFS():


        




import requests
import matplotlib.pyplot as plt
class BalanceSheet():
    def establishConnection(var: None) -> list:
        api_key=open('apiKey.txt', 'r').read()
        api_key=str(api_key)
        ticker="AAPL"
        yr=5
        list=[api_key, ticker, yr]
        return list
    def getDataBalanceSheet(var: None)->list:
        api_key=BalanceSheet().establishConnection()[0]
        ticker=BalanceSheet().establishConnection()[1]
        yr=BalanceSheet().establishConnection()[2]
        balSheet_statement=requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?limit={yr}&apikey={api_key}')
        balSheet_statement=balSheet_statement.json()
        balanceSheet=list(reversed([balSheet_statement[i]['totalAssets'] for i in range(len(balSheet_statement))]))
        return balanceSheet
    def plotData(var: None)->None:
        balanceSheet=BalanceSheet().getDataBalanceSheet()
        plt.plot(balanceSheet, label="Total Asset")
        plt.legend(loc="upper left")
        plt.show()
BalanceSheet().plotData()
    
# https://financialmodelingprep.com/api/v3/income-statement/AAPL?limit=120&apikey=bb0877b9f0c2dd35ff11c1b88a24509e
import requests
import matplotlib.pyplot as plt
class IncomeStatement():
    def establishConnection(var: None) -> list:
        api_key=open('apiKey.txt', 'r').read()
        api_key=str(api_key)
        ticker="AAPL"
        yr=5
        list=[api_key, ticker, yr]
        return list
    def getDataIncomeStatement(var: None)->list:
        api_key=IncomeStatement().establishConnection()[0]
        ticker=IncomeStatement().establishConnection()[1]
        yr=IncomeStatement().establishConnection()[2]
        income_statement=requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit={yr}&apikey={api_key}')
        income_statement=income_statement.json()
        IncomeStatementList=list(reversed([income_statement[i]['netIncome'] for i in range(len(income_statement))]))
        return IncomeStatementList
    def plotData(var: None)->None:
        balanceSheet=IncomeStatement().getDataIncomeStatement()
        plt.plot(balanceSheet, label="Net Income")
        plt.legend(loc="upper left")
        plt.show()
IncomeStatement().plotData()
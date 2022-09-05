import requests
import matplotlib.pyplot as plt
class CashFlowStatement():
    def establishConnection(var: None):
        api_key=open('apiKey.txt', 'r').read()
        api_key=str(api_key)
        ticker="AAPL"
        yr=5
        list=[api_key, ticker, yr]
        return list
    def getDataCashFlow(var: None):
        api_key=CashFlowStatement().establishConnection()[0]
        ticker=CashFlowStatement().establishConnection()[1]
        yr=CashFlowStatement().establishConnection()[2]
        cf_statement=requests.get(f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?limit={yr}&apikey={api_key}')

        cf_statement=cf_statement.json()

        cashflow=list(reversed([cf_statement[i]['operatingCashFlow'] for i in range(len(cf_statement))]))
        return cashflow

    def plotData(var: None):
        cashflow=CashFlowStatement().getDataCashFlow()
        plt.xlim(0, CashFlowStatement().establishConnection()[2])
        plt.plot(cashflow, label="Cashflow")
        plt.legend(loc="upper left")
        plt.xlabel('Year')
        plt.ylabel('Millions')
        plt.title(CashFlowStatement().establishConnection()[1]) 

        plt.show()
CashFlowStatement().plotData()



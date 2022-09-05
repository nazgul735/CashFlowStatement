import requests
import matplotlib.pyplot as plt


api_key=open('apiKey.txt', 'r').read()
api_key=str(api_key)
ticker="AAPL"
yr=10
cf_statement=requests.get(f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?limit={yr}&apikey={api_key}')

cf_statement=cf_statement.json()

cashflow=list(reversed([cf_statement[i]['operatingCashFlow'] for i in range(len(cf_statement))]))

plt.plot(cashflow, label="Cashflow")
plt.show()


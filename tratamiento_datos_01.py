

import requests
symbol="DIS"
url =f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
user_agent = {'User-agent': 'Mozilla/5.0'}
r=requests.get(url, headers = user_agent)
result=r.json()
#clarprint(result)

my_data_selection = {
    "nombre": r.json()["quoteSummary"]["result"][0]["price"]["shortName"],
    "ticker": r.json()["quoteSummary"]["result"][0]["price"]["symbol"],
    "precio": r.json()["quoteSummary"]["result"][0]["summaryDetail"]["previousClose"]["raw"]
}
print(my_data_selection)



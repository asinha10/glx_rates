# Get Foreign exchange rate from Currency Layer API
# Write the data into Azure SQL database table.

import requests
import datetime as dt
import pymssql

conn = pymssql.connect(server='asinha.database.windows.net', user='asinha01@asinha.database.windows.net', password='auG@2016a', database='azdatabase')

glx_endpoint = "http://api.currencylayer.com/live"
subs_key = "26a200fd315f63f022495a1157d7f640"
parameters = {
    "access_key": subs_key,
    "source": 'USD'
}

response = requests.get(glx_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
data_df = data['quotes']

# data_df = {'USDAED': 3.672904,
#         'USDAFN': 90.662356,
#         'USDALL': 104.889665,
#         'USDAMD': 478.83623,
#         'USDANG': 1.794058}


# print(currency_list)
# print(amount)

cursor = conn.cursor()

date_dt = dt.datetime.utcnow().date()
currency_list = []
rate = []

for row in data_df:
    cursor.execute("INSERT INTO dbo.gl_daily_rates (from_currency,to_currency,from_conversion_date, to_conversion_date,user_conversion_type,conversion_rate,mode_flag) values(%s,%s,%s,%s,%s,%s,%s)", ('USD', row.lstrip('USD'), date_dt, date_dt, 'CORPORATE', data_df[row],'D'))


conn.commit()

print("Data posted to table GL_DAILY_RATES in Azure database azdatabase")

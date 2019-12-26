import requests
from prettytable import PrettyTable

# Getting the Response from Razorpay.com's API
ifsc = input("Enter IFSC Code : ")
url = "https://ifsc.razorpay.com/" + ifsc
response = requests.get(url)

# Validating and Priting the Response
if response:
    json = response.json()
    table = PrettyTable(['Information', 'Details'])
    for info, d in json.items():
    	if d != "":
    		table.add_row([info, d])
    print(table)
else:
    print('An error has occurred. Please check the IFSC Code Again')
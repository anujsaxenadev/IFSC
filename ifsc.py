import requests
from prettytable import PrettyTable

# Getting the Response from Razorpay.com's API
ifsc = input("Enter IFSC Code : ")
url = "https://ifsc.razorpay.com/" + ifsc
response = requests.get(url)
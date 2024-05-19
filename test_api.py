import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    'Month': 3,
    'Age': 12,
    'Occupation': 2,
    'Annual_Income': 5000,
    'Monthly_Inhand_Salary': 4000,
    'Num_Bank_Accounts': 3,
    'Num_Credit_Card': 2,
    'Interest_Rate': 12,
    'Delay_from_due_date': 5,
    'Num_of_Delayed_Payment': 2,
    'Changed_Credit_Limit': 1,
    'Num_Credit_Inquiries': 4,
    'Credit_Mix': 1,
    'Outstanding_Debt': 20000,
    'Credit_Utilization_Ratio': 30.0,
    'Credit_History_Age': 10,
    'Payment_of_Min_Amount': 1,
    'Total_EMI_per_month': 1000,
    'Amount_invested_monthly': 500,
    'Payment_Behaviour': 2,
    'Monthly_Balance': 3000,
    'Count_Auto Loan': 0,
    'Count_Credit-Builder Loan': 0,
    'Count_Personal Loan': 1,
    'Count_Home Equity Loan': 0,
    'Count_Not Specified': 0,
    'Count_Mortgage Loan': 0,
    'Count_Student Loan': 1,
    'Count_Debt Consolidation Loan': 0,
    'Count_Payday Loan': 0
}

response = requests.post(url, json=data)
print(response.json())

import requests

url = 'https://v6.exchangerate-api.com/v6/20ee8fc68f97830c71d9871a/latest/USD'

response = requests.get(url)
data = response.json()

print("****WELCOME TO CURRENCY EXCHANGE MACHINE****")
a = float(input("Enter the amount of money you have: "))

def currency():
    print("Choose the country which it belongs to:")
    print("Select :")
    print("1. Kuwaiti Dinar (KWD) to INDIAN RUPEE(INR)")
    print("2. Bahraini Dinar (BHD) to INDIAN RUPEE(INR)")J
    print("3. Omani Rial (OMR) to INDIAN RUPEE(INR)")
    print("4.Jordanian Dinar (JOD) to INDIAN RUPEE(INR)")
    
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print(f"{a} KWD is equal to {a /data['conversion_rates']['KWD']} INR")
    elif choice == '2':
        print(f"{a} BHD is equal to {a /data['conversion_rates']['BHD']} INR")
    elif choice == '3':
        print(f"{a} OMR is equal to {a /data['conversion_rates']['OMR']} INR")
    elif choice == '4':
        print(f"{a} JOD is equal to {a /data['conversion_rates']['JOD']} INR")
    else:
        print("Invalid input")

currency()
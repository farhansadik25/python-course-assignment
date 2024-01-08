mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
            }

#Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT

i=0
while i<len(mobile_data['data']):
    mobile_name= mobile_data['data'][i]['name']
    price = mobile_data['data'][i]['price']
    made_country = mobile_data['data'][i]['made']
    rate = mobile_data['exchnage_rate']
    bdt_price = rate * float(mobile_data['data'][i]['price'].split()[0])
    print(f'{mobile_name} is made in {made_country}. The price is {price} which is almost equal to {bdt_price:.2f} BDT')
    i+=1


import urllib
from urllib import request


order = {}
order['dish_name'] = 'Pizza'
order['price'] = 200
order['quantity'] = 2
data = urllib.parse.urlencode(order)
data = data.encode('ascii')

request2 = request.Request('http://127.0.0.1:5000/Orders/1', data=data, method='POST')
try:
    response2 = request.urlopen(request2)
    print(response2.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

order = {}
order['dish_name'] = 'Pasta'
order['price'] = 150
order['quantity'] = 3
data = urllib.parse.urlencode(order)
data = data.encode('ascii')
request3 = request.Request('http://127.0.0.1:5000/Orders/2', data=data, method='POST')
try:
    response3 = request.urlopen(request3)
    print(response3.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

order = {}
order['dish_name'] = 'Coke'
order['price'] = 60
order['quantity'] = 2
data = urllib.parse.urlencode(order)
data = data.encode('ascii')
request4 = request.Request('http://127.0.0.1:5000/Orders/3', data=data, method='POST')
try:
    response4 = request.urlopen(request4)
    print(response4.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())


request5 = request.Request('http://127.0.0.1:5000/Orders/')
try:
    response5 = request.urlopen(request5)
    print(response5.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

request6 = request.Request('http://127.0.0.1:5000/Orders/1')
try:
    response6 = request.urlopen(request6)
    print(response6.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

request7 = request.Request('http://127.0.0.1:5000/Orders/2',method ='DELETE')
try:
    response7 = request.urlopen(request7)
    print(response7.read())
except urllib.error.HTTPError as e:
    print(e.code,e.read())

request8 = request.Request('http://127.0.0.1:5000/Orders/')
try:
    response8 = request.urlopen(request8)
    print(response8.read())
except urllib.error.HTTPError as e:
    print(e.code,e.read())

order = {}
order['dish_name'] = "Pepsi"
order['quantity'] = 2
data = urllib.parse.urlencode(order)
data = data.encode('ascii')
request9 = request.Request('http://127.0.0.1:5000/Orders/3', data=data, method='PUT')
try:
    response9 = request.urlopen(request9)
    print(response9.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())
    
request10 = request.Request('http://127.0.0.1:5000/Orders/')
try:
    response10 = request.urlopen(request10)
    print(response10.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())                  

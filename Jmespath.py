import jmespath
import json

f = open('order-data.json')
data = json.load(f)

# print(data) #{'orders': [{'order_id': 3944, 'customer': {'email': 'cbritch@comcast.net', 'first_name': '
search_string = "orders[0].order_id"
print(jmespath.search(search_string, data)) # 3944
search_string = "orders[0].customer.email"
print(jmespath.search(search_string, data)) # cbritch@comcast.net
search_string = "orders[0].customer.country"
print(jmespath.search(search_string, data)) # United States

search_string = "orders[*].order_id"
print(jmespath.search(search_string, data)) # [3944, 1598, 2999]

search_string = "orders[?customer.country == 'United States'].customer.email"
print(jmespath.search(search_string, data)) # ['cbritch@comcast.net']
search_string = "orders[?customer.country == 'United States'].[customer.first_name,customer.email]"
print(jmespath.search(search_string, data)) # [['Cori', 'cbritch@comcast.net']]
search_string = "orders[?item.name == 'Pants'].[customer.first_name,item.size]"
print(jmespath.search(search_string, data)) # [['Lol', 'Small']]
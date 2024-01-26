from Data_operations import json_fail, from_new

data = json_fail()
for opiration in from_new(data)[0:5]:
    if opiration.get('from'):
        print(f'{opiration['date']} {opiration["description"]}\n{opiration['from']} -> {opiration['to']}\n'
              f'{opiration["operationAmount"]["amount"]} {opiration["operationAmount"]["currency"]["name"]}\n')
    else:
        print(f'{opiration['date']} {opiration["description"]}\n{opiration['to']}\n'
              f'{opiration["operationAmount"]["amount"]} {opiration["operationAmount"]["currency"]["name"]}\n')
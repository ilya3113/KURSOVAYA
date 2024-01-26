import json


def json_fail():
    with open('operations.json', "r", encoding="utf-8") as operations_bank:
        return json.load(operations_bank)


def data_new(data):
    date_new = []
    data_operations = sort_and_executed(data)
    for data_bank in data_operations:
        if data_bank.get("date"):
            data_new_bank = data_bank["date"]
            data_new_bank = data_new_bank[8:10] + "." + data_new_bank[5:7] + "." + data_new_bank[0:4]
            data_bank["date"] = data_new_bank
            date_new.append(data_bank)
    return date_new


def to_new(data):
    score = data_new(data)
    new_to = []
    for score_bank in score:
        if score_bank.get("to"):
            bank = score_bank["to"]
            if bank[0:4] == "Счет":
                bank = "Счет **" + bank[-4:]
                score_bank["to"] = bank
                new_to.append(score_bank)
            else:
                bank = bank[::-16] + bank[-16:-12] + " " + bank[-12:-10] + "** **** " + bank[-4:]
                score_bank["to"] = bank
                new_to.append(score_bank)
    return new_to


def from_new(data):
    new_from = []
    score = to_new(data)
    for score_bank in score:
        if score_bank.get("from"):
            bank = score_bank["from"]
            if bank[0:4] == "Счет":
                bank = "**" + bank[-4:]
                score_bank["from"] = bank
                new_from.append(score_bank)
            else:
                bank = bank[0:-16] + bank[-16:-12] + " " + bank[-12:-10] + "** **** " + bank[-4:]
                score_bank["from"] = bank
                new_from.append(score_bank)
        else:
            new_from.append(score_bank)
    return new_from


def sort_and_executed(data):
    new_item = []
    for item in data:
        if item.get('state') == 'EXECUTED':
            new_item.append(item)
    new_item.sort(key=lambda x: x.get('date'), reverse=True)
    return new_item

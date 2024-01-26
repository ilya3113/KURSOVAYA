from scr import Data_operations


def test_data_new():
    """
    Тест оформления даты
    """
    sample_data = [
        {
            "date": "2022-01-01T04:27:37.904916",
            "state": "EXECUTED"
        },
    ]
    expected_result = [
        {
            "date": "01.01.2022",
            "state": "EXECUTED"
        },
    ]
    assert Data_operations.data_new(sample_data) == expected_result


def test_to_new():
    """
    Тест скрытия номера карты или счета отправителя
    """
    sample_to = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
    ]
    expected_result = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "26.08.2019",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет **9589"
        },
    ]
    assert Data_operations.to_new(sample_to) == expected_result


def test_from_new():
    """
    Тест скрытия номера карты или счета получателя
    """
    sample_to = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
    ]
    expected_result = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "26.08.2019",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596 83** **** 5199",
            "to": "Счет **9589"
        },
    ]
    assert Data_operations.from_new(sample_to) == expected_result

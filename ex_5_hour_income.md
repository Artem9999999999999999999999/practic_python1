# practic_python


+ [Hour income](#Hour-income)
  
  
# Calculate hour salary

## Hour income

Создать сервис для расчета своей почасовой ставки.

Большинство наемных сотрудников имеют фиксированную оплачиваемую ставку. Как-то раз стало интересно, сколько случайно выбранный сотрудник получает в час. Почасовая ставка отличается из-за праздников и разных выходных от года к году.

Сервис должен возвращать ответ в формате JSON вида:

{
  "year": 2016,
  "month": "JULY",
  "salary": 1000000,
  "hour_income": 49950.87
}

Округление почасовой ставки должно быть до копеек
Покрыть тестами код

```python

import json
from random import randint


class RandomNumber:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def get_number(self):
        return randint(20, 23)


def get_hour_income(name_file='input.json'):
    with open(name_file, "r") as read_file:
        data = json.load(read_file)
        hour_in_month = RandomNumber(data['year'], data['month']).get_number()
        data['hour_income'] = round(data['salary'] / hour_in_month, 2)
    return data


def write_in_file(data, /, out_name_file='output.json'):
    with open(out_name_file, 'w') as outfile:
        json.dump(data, outfile)


write_in_file(get_hour_income())

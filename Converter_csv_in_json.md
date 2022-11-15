# practic_python4

Университетский курс по Питону. Задачи, которые могут быть полезны на собеседовании


+ [Converter](#converter)
+ [Class Converter](#class-converter)
+ [Test converter](#test-converter)
+ [Class Converter two](#class-converter-two)

# Converter

## Converter

Реализация конвертера следующего вида:


input.csv


id,name,birth,salary,department

1,Ivan,1980,150000,1

2,Alex,1960,200000,5

3,Ivan,,130000,8

->//

output.json

[
 {
   id: 1,
   
   name: Ivan,
   
   birth: 1980,
   
   salary: 150000,
   
   department: 1
 },
 
 {
   id: 2,
   
   name: Alex,
   
   birth: 1960,
   
   salary: 200000,
   
   department: 5
 },
 
 {
   id: 3,
   
   name: Ivan,
   
   birth: null,
   
   salary: 130000,
   
   department: 8
	}
]

```python

import csv
import json


def open_csv_file_and_convert(csv_file):
    data_dict = {}
    with open(csv_file, encoding='utf-8') as csv_file_handler:  # open a csv file handler
        csv_reader = csv.DictReader(csv_file_handler)
        for rows in csv_reader:     # convert each row into a dictionary
            key = rows['id']        # and add the converted data to the data_variable
            data_dict[key] = rows
        return data_dict


def open_json_file_and_write_into(json_file, data_dict):
    with open(json_file, 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent=4))


def csv_to_json(csv_file, json_file):
    open_json_file_and_write_into(json_file, open_csv_file_and_convert(csv_file))


if __name__ == "__main__":
    csv_file = "input.csv"
    json_file = "output.json"
    csv_to_json(csv_file, json_file)

```

## Class Converter 
 
Реализация класса конвертер:

```python
import csv
import json



class Converter:
    def __init__(self):
        self.__data = None


    def open_csv_file_and_convert(self, csv_file):
        data_dict = {}
        with open(csv_file, encoding='utf-8') as csv_file_handler:
            self.__data = csv.DictReader(csv_file_handler)
            if self.__data:
                for rows in self.__data:
                    key = rows['id']
                    data_dict[key] = rows
            return data_dict

    def open_json_file_and_write_into(self, json_file, data_dict):
        with open(json_file, 'w', encoding='utf-8') as json_file_handler:
            json_file_handler.write(json.dumps(data_dict, indent=4))


def main():
    conv = Converter()
    dict = conv.open_csv_file_and_convert(csv_file)
    conv.open_json_file_and_write_into(json_file, dict)


if __name__ == "__main__":
    csv_file = "input.csv"
    json_file = "output.json"
    main()
```

## Class Converter two
 
Реализация класса конвертер, который выдает ошибку, в случае, когда отсутствует заголовок в файле .csv:

```python
import csv
import json


def open_json_file_and_write_into(json_file, data_dict):
    with open(json_file, 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent=4))


class Converter:
    def __init__(self):
        self.__data = None

    def open_csv_file_and_convert(self, csv_file):
        data_dict = {}
        with open(csv_file, encoding='utf-8') as csv_file_handler:
            self.__data = csv.DictReader(csv_file_handler)
            if self.__data:
                for rows in self.__data:
                    if 'id' in rows:
                        key = rows['id']
                        data_dict[key] = rows
                    else:
                        return 'Error not title in the csv file'
            return data_dict

    def open_json_file_and_write_into(self, json_file, data_dict):
        with open(json_file, 'w', encoding='utf-8') as json_file_handler:
            json_file_handler.write(json.dumps(data_dict, indent=4))
            return


def main():
    conv = Converter()
    dict = conv.open_csv_file_and_convert(csv_file)
    conv.open_json_file_and_write_into(json_file, dict)


if __name__ == "__main__":
    csv_file = "input.csv"
    json_file = "output.json"
    main()
```


# Test

## Test converter

Тест работы конвертера: на нормальный файл, на файл с пропущенными сведениями, на файл только с заголовком, 

```python
from csv_json_convert import Converter
import json


def connect(json_doc):
    with open(json_doc) as json_file:
        test_data = json.load(json_file)
        return test_data


def test1_file_data_normal():
    db = Converter()
    dict_data = db.open_csv_file_and_convert('test1.csv')
    db.open_json_file_and_write_into('test1.json', dict_data)
    test1_data = connect('test1.json')
    print(test1_data)
    assert test1_data["1"]["id"] == "1"
    assert test1_data["1"]["name"] == "Ivan"
    assert test1_data["1"]["birth"] == "1980"
    assert test1_data["1"]["salary"] == "150000"
    assert test1_data["1"]["department"] == "1"


def test2_file_data_missing_element():
    db = Converter()
    dict_data = db.open_csv_file_and_convert('test2.csv')
    db.open_json_file_and_write_into('test2.json', dict_data)
    test2_data = connect('test2.json')
    assert test2_data["1"]["id"] == "1"
    assert test2_data["1"]["name"] == "Ivan"
    assert test2_data["1"]["birth"] == ""
    assert test2_data["1"]["salary"] == "150000"
    assert test2_data["1"]["department"] == "1"


def test3_file_data_missing_all_elements():
    db = Converter()
    dict_data = db.open_csv_file_and_convert('test3.csv')
    db.open_json_file_and_write_into('test3.json', dict_data)
    test3_data = connect('test3.json')
    expected3 = {}
    assert expected3 == test3_data


def test4_file_data_missing_title():
    db = Converter()
    dict_data = db.open_csv_file_and_convert('test4.csv')
    db.open_json_file_and_write_into('test4.json', dict_data)
    test4_data = connect('test4.json')
    expected4 = 'Error not title in the csv file'
    assert expected4 == test4_data

```

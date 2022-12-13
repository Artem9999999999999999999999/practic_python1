# practic_python4

+ [Class Converter with library](#class-converter-with-library)
+ [Class Converter](#class-converter)
+ [Test converter](#test-converter)

# Converter

## Class Converter with library
 
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


class Converter:
    def __init__(self):
        self.__data = None

    def convert_csv_in_pretty_json(self, csv_file, json_file):
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
        with open(json_file, 'w', encoding='utf-8') as json_file_handler:
            json_file_handler.write(json.dumps(data_dict, indent=4))
            return


def main():
    conv = Converter()
    conv.convert_csv_in_pretty_json(csv_file, json_file)


if __name__ == "__main__":
    csv_file = "input.csv"
    json_file = "output.json"
    main()

```

# Converter manual

## Class Converter 

```python
class ManualCsvConverter:

    def __init__(self, csv_data):
        self.title = csv_data[0]
        self.values = csv_data[1:]

    def prepare_title(self):
        title = self.title.strip().split(',')
        return title

    def prepare_row_values(self):
        values = [row.strip().split(',') for row in self.values]
        return values

    def convert_row_to_json(self, data):
        formatted_values = ",".join([""""{}":
                                             {}""".format(key, value) for key, value in data.items()])
        pretty_line = """{{
         {}
        }}""".format(formatted_values)
        return pretty_line

    def to_json(self):
        title = self.prepare_title()
        row_values = self.prepare_row_values()

        self.check_data(title, row_values)

        result = [self.convert_row_to_json(dict(zip(title, row))) for row in row_values]
        return "[{}]".format(",".join(result))

    def check_data(self, title, row_values):
        for row in row_values:
            assert len(title) == len(row), "Column count is not equals value count"

```



# Test

## Test converter

Тест работы конвертера two: на нормальный файл, на файл с пропущенными сведениями, на файл только с заголовком, 

```python
from csv_json_convert import Converter
import json


def connect(json_doc):
    with open(json_doc) as json_file:
        test_data = json.load(json_file)
        return test_data


def test1_file_data_normal():
    db = Converter()
    db.convert_csv_in_pretty_json('test1.csv', 'test1.json')
    test1_data = connect('test1.json')
    print(test1_data)
    assert test1_data["1"]["id"] == "1"
    assert test1_data["1"]["name"] == "Ivan"
    assert test1_data["1"]["birth"] == "1980"
    assert test1_data["1"]["salary"] == "150000"
    assert test1_data["1"]["department"] == "1"


def test2_file_data_missing_element():
    db = Converter()
    db.convert_csv_in_pretty_json('test2.csv', 'test2.json')
    test2_data = connect('test2.json')
    assert test2_data["1"]["id"] == "1"
    assert test2_data["1"]["name"] == "Ivan"
    assert test2_data["1"]["birth"] == ""
    assert test2_data["1"]["salary"] == "150000"
    assert test2_data["1"]["department"] == "1"


def test3_file_data_missing_all_elements():
    db = Converter()
    db.convert_csv_in_pretty_json('test3.csv', 'test3.json')
    test3_data = connect('test3.json')
    expected3 = {}
    assert expected3 == test3_data


def test4_file_data_missing_title():
    db = Converter()
    db.convert_csv_in_pretty_json('test4.csv', 'test4.json')
    test4_data = connect('test4.json')
    expected4 = 'Error not title in the csv file'
    assert expected4 == test4_data


```

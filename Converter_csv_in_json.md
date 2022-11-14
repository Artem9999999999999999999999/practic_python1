# practic_python4

Университетский курс по Питону. Задачи, которые могут быть полезны на собеседовании


+ [Converter](#converter)
+ [Test converter](#test-converter)

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


# Test

## Test converter

Тест работы конвертера:

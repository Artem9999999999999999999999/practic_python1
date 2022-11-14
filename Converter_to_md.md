# practic_python2

Университетский курс по Питону. Задачи, которые могут быть полезны на собеседовании


+ [Converter to md](#Converter-to-md)

# Converter

## Converter to md

Конвертер в оформленные для Git'а md файлы 


```python

INPUT_CODE_DELIMITER = "# ---end----"

def read_data(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content

def write_data(file_name, data):
    file = open(file_name, 'a+')
    file.write('\n')
    file.write(data)
    file.close()

def prepare_md_titles(data):
    title, description = None, None

    for line in data.split('\n'):
        if line.startswith('# title'):
            title = line.replace('# title ', '')
        elif line.startswith('# description'):
            description = line.replace('# description ', '')

    return title, description

def prepare_md_format(title, description, source_code):
    md_link = '-'.join(title.lower().split())

    template = """+ [{}](#{})
    
    ## {}
    
    {}
    
    ```python
    {}
    ```"""

    return template.format(title, md_link, title, description, source_code.lstrip())


def convert_data(data):
    titles, source_code = data.split(INPUT_CODE_DELIMITER)
    title, description = prepare_md_titles(titles)
    result_md = prepare_md_format(title, description, source_code)
    return result_md


def main():
    content = read_data('solution.py')
    result = convert_data(content)
    write_data('out.md', result)




if __name__ == "__main__":
    main()



```

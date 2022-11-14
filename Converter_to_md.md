# practic_python

Университетский курс по Питону. Задачи, которые могут быть полезны на собеседовании


+ [Converter to md](#Converter-to-md)

# Converter

## Converter to md

Конвертер в оформленные для Git'а md файлы 


```python

INPUT_CODE_DELIMETR = '# ---end---'
MD_CONTENT_DELIMETER = '<!---md_file_delimeter>'

def read_data (file_name):
    start_file = open(file_name)
    content = start_file.read()
    start_file.close()
    return content


def write_data (file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def prepare_md_titles(data):
    title = description = None

    for line in data.split('\n'):
        if line.startswith('# title'):
            title = line.replace('# title ', '')
        elif line.startswith('# description '):
            description = line.replace('# description ', '')
    return title, description


def prepare_md_format(title, description, source_code):
    template = """## {}

{}

``` python
{}
```"""

    return template.format(title, description, source_code.lstrip())
    
    
def prepare_md_link(title):
    md_link = '-'.join(title.lower().split())
    template = '+ [{}](#{})'
    return template.format(title, md_link);


def prepare_new_md_content(new_md_link, new_md_code, old_md_content):
    old_md_link, old_md_code = old_md_content.split(MD_CONTENT_DELIMETER)
    result_md = f"{old_md_link}{new_md_link}\n{MD_CONTENT_DELIMETER}{old_md_code}\n\n{new_md_code}"
    return result_md


def convert_data(data, old_md_content):
    titles, source_code = data.split(INPUT_CODE_DELIMETR)
    title, description = prepare_md_titles(titles)
    new_md_code = prepare_md_format(title, description, source_code)
    new_md_link = prepare_md_link(title)
    return prepare_new_md_content(new_md_link, new_md_code, old_md_content)
    

def main():
    content = read_data('sum_diagonal.py')
    old_md_content = read_data('matrix.md')
    result = convert_data(content, old_md_content)
    print(result)
    write_data('matrix.md', result)


if __name__ == "__main__":
    main()
```

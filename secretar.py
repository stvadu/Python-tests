documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    name_in = False
    for numbers1 in documents:
        if doc_number == numbers1["number"]:
            name = numbers1["name"]
            name_in = True
    if name_in:
        return name
    else:
        return "Документ не найден"


def get_directory(doc_number):
    n_in = False
    for numbers2 in directories:
        if doc_number in directories.get(numbers2):
            shelf_n = numbers2
            n_in = True
    if n_in:
        return shelf_n
    else:
        return "Полки с таким документом не найдено"


def add(document_type, number, name, shelf_number):
    documents_add = {"type": document_type, "number": number, "name": name}
    documents.append(documents_add)
    directories[shelf_number] = number
    return True

if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))
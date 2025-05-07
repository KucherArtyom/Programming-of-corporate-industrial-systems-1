# Programming-of-corporate-industrial-systems-1
## Кучер Артем Сергеевич ЭФМО-02-24
### Практика 1 
### Анализатор текстовых файлов (Python)
### Пример использования
```
1.Открыть файл
2.Закончить программу
Выберите действие: 1
Укажите путь к текстовому файлу: D://text.txt
1.Найти слово в файле
2.Закрыть файл
Выберите действие: 1
Введите слово для поиска: и
Общее количество слов в файле: 149
Количество повторений слова 'и': 4
1.Найти слово в файле
2.Закрыть файл
Выберите действие: 2
1.Открыть файл
2.Закончить программу
Выберите действие: 2
```
### Код программы
```
class File_Text_Analysis:
    def __init__(self, file_path, search_word):
        self.file_path = file_path
        self.search_word = search_word
        self.content = None
        self.word_count = 0
        self.search_word_count = 0

    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
                self.word_count = len(self.content.split())
        except FileNotFoundError:
            print("Ошибка: Файл не найден.")
            return False
        return True

    def count_search_word(self):
        if self.content is not None:
            words = self.content.split()
            cleaned_words = [word.strip('.,!?;:"').lower() for word in words]
            self.search_word_count = cleaned_words.count(self.search_word.strip('.,!?;:"').lower())

    def display_results(self):
        print(f"Общее количество слов в файле: {self.word_count}")
        print(f"Количество повторений слова '{self.search_word}': {self.search_word_count}")

def main():
    while(True):
        selection1 = int(input("1.Открыть файл\n2.Закончить программу\nВыберите действие: "))
        match selection1:
            case 1:
                filepath = input("Укажите путь к текстовому файлу: ")
                while (True):
                    selection2 = int(input("1.Найти слово в файле\n2.Закрыть файл\nВыберите действие: "))
                    match selection2:
                        case 1:
                            search_word = input("Введите слово для поиска: ")
                            file_analyzer = File_Text_Analysis(filepath, search_word)
                            if file_analyzer.read_file():
                                file_analyzer.count_search_word()
                                file_analyzer.display_results()
                        case 2:
                            break
            case 2:
                break

if __name__ == "__main__":
    main()
```

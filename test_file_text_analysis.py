import unittest


from file_text_analysis import File_Text_Analysis

class TestFileTextAnalysis(unittest.TestCase):
    def setUp(self):
        self.test_content = "Это тест. Этот тест нужен для тестирования функции поиска слова."
        self.file_path = "test_file.txt"

        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(self.test_content)

    def tearDown(self):
        import os
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_count_search_word(self):
        search_word = "тест"
        file_analyzer = File_Text_Analysis(self.file_path, search_word)

        file_analyzer.read_file()
        file_analyzer.count_search_word()

        self.assertEqual(file_analyzer.search_word_count, 2)
        self.assertEqual(file_analyzer.word_count, len(self.test_content.split()))

if __name__ == "__main__":
    unittest.main()
# Описываем класс для работы со строками

# Нам понадобится функционал очистки от лишник пробелов и правильной расстановки точек

"""
!pip3 install deeppavlov==0.15.0
!pip3 install fuzzywuzzy==0.18.0
!pip3 install langdetect
!pip3 install razdel
!pip3 install transliterate==1.10.2
"""

from deeppavlov.models.tokenizers.nltk_moses_tokenizer import NLTKMosesTokenizer
from transliterate import translit, get_available_language_codes
from razdel import sentenize, tokenize
from langdetect import detect
from fuzzywuzzy import process  ##
from fuzzywuzzy import fuzz

class FuzzyCompare:
    '''
    Методы обрадотки и сравнения строк
    '''

    def __init__(self, stop_words=None, stop_countries=None):

        # инициализируем детокинайзер
        self.detokenizer = NLTKMosesTokenizer('en').detokenizer
        self.stop_words = stop_words
        self.stop_countries = stop_countries

    def norm_ref_items(self, txt):
        """
        Нормализация строки из датасета: приводим заники препинани к правильной структуре
        :param txt: исходная строка
        :return: преобразованная строка
        """
        if detect(txt) == 'ru':
            # производим транслитерацию на латиницу
            txt = translit(txt, language_code='ru', reversed=True)

        # расстановка пробелов и знаков препинания поправилам аббривеатур и разделителей
        tokens = self.detokenizer.detokenize([' '.join([_.text for _ in tokenize(txt)])])
        return ''.join(tokens).strip()

    def estimate(self, txt_1, txt_2, normalize=True):
        '''
        Подсчет меры близости двух строк
        :param txt_1: строка 1
        :param txt_2: строка 2
        :return: значение меры близости в пронтах
        '''
        if normalize:
            _txt_1 = self.norm_ref_items(txt_1)
            _txt_2 = self.norm_ref_items(txt_2)
        return process.extract(_txt_1, [_txt_2], scorer=fuzz.token_sort_ratio)[0][-1]

    def estimate_df(self, txt_tuple, normalize=True):
        '''
        Запуск сравнения для дадафрэйма: разбиваем значение по разделителю и производим сравнение
        '''
        t1, t2 = txt_tuple.split('|')
        return self.estimate(t1, t2)

    def clear_punctuation(self, txt_1, to_lower=True):
        '''
        Удаление пунктуации и перевод в нижний регистр
        '''
        valids = re.sub(r"[^\w ]*", '', txt_1)
        if to_lower:
            return ' '.join(valids.split()).lower()
        else:
            return ' '.join(valids.split())

    def translit(self, txt_1):
        '''
        Удаление пунктуации и перевод в нижний регистр
        '''
        return translit(txt_1, language_code='ru', reversed=True)

    def remove_stopcountries(self, text):
        '''
        Removes Stop Words (also capitalized) from a string, if present

        Args:
            text (str): String to which the function is to be applied, string

        Returns:
            Clean string without Stop Words
        '''
        # check in lowercase
        t = [token for token in text.split() if process.extractOne(token.lower(),
                                                                   self.stop_countries,
                                                                   scorer=fuzz.token_sort_ratio)[-1] <= 80]
        text = ' '.join(t)
        return text

    def remove_stopwords(self, text):
        '''
        Removes Stop Words (also capitalized) from a string, if present

        Args:
            text (str): String to which the function is to be applied, string

        Returns:
            Clean string without Stop Words
        '''
        # check in lowercase
        t = [token for token in text.split() if token.lower() not in self.stop_words]
        text = ' '.join(t)
        return text

if __name__ == '__main__':
    # stop_words -читаем из csv
    # stop_countries -читаем из csv
    fz = FuzzyCompare(stop_words, stop_countries)
    fz.remove_stopwords('Iko Industries Ltd')
    fz.remove_stopcountries('Iko Industries Ltd')

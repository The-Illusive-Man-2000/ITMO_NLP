### ITMO_NLP
$~~~~~~~~~$

__Описание папок и файлов репозитория:__

$~~~~~~~~~$

__Папка tfidfvectorizer:__

NLP_tfidfvectorizer_embeddings_(words).ipynb $~~~~~~~~~~~~~~~~~~~~~~$ _Создание эмбеддингов названий с помощью tfidfvectorizer (слова) и их последующее сравнение через косинусное сходство._

NLP_tfidfvectorizer_embeddings_(3-gram)  $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Создание эмбеддингов названий с помощью tfidfvectorizer (3 грамы) и их последующее сравнение через косинусное сходство._

NLP_Make_embeddings_for_companies.ipynb  $~~~~~~~~~~~~~~~~~~~~~~~~~$ _Создание эмбеддингов названий компаний с помощью tfidfvectorizer (3 грамы) и их сохранение._

NLP_Inference.ipynb  $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Загрузка tfidfvectorizer, сохранённых эмбеддингов названий компаний, списка компаний и поиск топ-5 похожих названий (через косинусное сходство). Время обработки каждого запроса около 11 секунд. Долго потому что идёт сравнение с 18022 эбеддингами. Инференс был на старом пк, процессор core i5 760._

vectorizer_2.pickle  $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Сохранённый tfidfvectirizer (3 грамы)._

companies_name_unic.pickle    $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Уникальные названия компаний._

stop_countries.csv      $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Стоп слова-страны._

stop_words.csv     $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Стоп слова-названия форм собственности._

$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$
$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$

Сравнение методов. Сравнение проводилось через косинусное сходство эмбеддингов с порогом 0.3 (если больше либо равно 0.3 значит эмбеддинги считаем похожими, если меньше 0.3, то непохожими). Сравнивались доли найденных несхожих пар среди несхожих и схожих среди схожих. Tfidfvectorizer (words ) продемонстрировал результаты лучше, чем Tfidfvectorizer (з-grams). Но в итоге для инференса решил оставить  Tfidfvectorizer (з-grams) потому что он давал эмбеддинги для незнакомых слов.

Метод                              | Доля несхожих среди несхожих пар  | Доля схожих среди схожих пар   
:----------------------------------|:---------------------------------:|--------------------:
Tfidfvectorizer (з-grams)          |  0.67                             | 0.85 
Tfidfvectorizer (words )           |  0.96                             | 0.928
Glove (Twitter)                    |  0.985                            | 0.02
Word2vec (google news)             |  0.407                            | 0.786

Цифры из таблички можно увидеть в конце соответствующих ноутбуков.
Также проводились эксперименты с Fasttext и DistillBert, но не пошло.


***
requirements.txt   $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Список используемых модулей._

***
https://drive.google.com/file/d/1ui-r1csI77qP7S3-40fsM4eK9keAQ7L5/view?usp=sharing   $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$_Ссылка на сохраненные эмбеддинги (tfidfvectorizer 3 грамы) для названий компаний._

***
$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$
$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$

__Папка Glove:__

NLP_glove_embeddings.ipynb     $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Эксперименты с созданием эмбеддингов с помощью Glove, обученного на текстах из Твиттера и их последующее сравнение через косинусное сходство._

***

__Папка word2vec:__

NLP_word2vec_embeddings.ipynb  $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$   _Эксперименты с созданием эмбеддингов с помощью word2vec, обученного на новостях (google news) и их последующее сравнение через косинусное сходство._

***

__Папка USE:__

Brand_identity_USE_testing.ipynb  $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Эксперименты с созданием эмбеддингов с помощью universal sentence encoder._
NLP_Inference_USE.ipynb   $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Инференс с помощью universal sentence encoder. Сравнение названий. Время обработки поиска 0.1-0.3 секунды. Инференс был на старом пк, процессор core i5 760._

***

__Папка itmo_duplicate_detection:__

Эксперименты с выявлением дубликатов с помощью FuzzyWuzzy, LogReg, LinearSVC. 

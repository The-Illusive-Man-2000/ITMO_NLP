### ITMO_NLP
$~~~~~~~~~$

__Описание папок и файлов репозитория:__

$~~~~~~~~~$

__Папка tfidfvectorizer:__

NLP_tfidfvectorizer_embeddings_(words).ipynb $~~~~~~~~~~~~~~~~~~~~~~$ _Создание эмбеддингов названий с помощью tfidfvectorizer (слова) и их последующее сравнение через косинусное сходство._

NLP_tfidfvectorizer_embeddings_(3-gram)  $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Создание эмбеддингов названий с помощью tfidfvectorizer (3 грамы) и их последующее сравнение через косинусное сходство._

NLP_Make_embeddings_for_companies.ipynb  $~~~~~~~~~~~~~~~~~~~~~~~~~$ _Создание эмбеддингов названий компаний с помощью tfidfvectorizer (3 грамы) и их сохранение._

NLP_Inference.ipynb  $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Загрузка tfidfvectorizer, сохранённых эмбеддингов названий компаний, списка компаний и поиск похожих названий (через косинусное сходство)._

vectorizer_2.pickle  $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Сохранённый tfidfvectirizer (3 грамы)._

companies_name_unic.pickle    $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Уникальные названия компаний._

stop_countries.csv      $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Стоп слова-страны._

stop_words.csv     $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Стоп слова-названия форм собственности._

***
https://drive.google.com/file/d/1ui-r1csI77qP7S3-40fsM4eK9keAQ7L5/view?usp=sharing   $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$_Ссылка на сохраненные эмбеддинги (tfidfvectorizer 3 грамы) для названий компаний._

***
$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$
$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$
$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$
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
NLP_Inference_USE.ipynb   $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Инференс с помощью universal sentence encoder. Сравнение названий._

***

__Папка itmo_duplicate_detection:__

Эксперименты с выявлением дубликатов с помощью FuzzyWuzzy, LogReg, LinearSVC. 

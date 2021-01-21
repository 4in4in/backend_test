# Тестовый скрипт для работы с опросниками

### Установка зависимостей:
1. Установить [python](https://www.python.org/downloads/) 
2. Скачать [репозиторий](https://github.com/tolstoy92/backend_test) проекта
3. В командной строке перейти в корневую папку проекта
4. Установить зависимости из requirements.txt: `pip install -r requirements.txt`

### Работа с бэком
1. В командной строке перейти в корневую папку проекта
2. Запустить сервер: `python main.py`

### Ручки
1. Получение списка вопросов:<br>
 url: `http://localhost:5000/api/questionnaries/get_questionnary`<br>
 method: get<br>
 aruments: `questionnary_name` - название опросника (для теста используй только "test_questionnary")<br> 
 возвращает json вида:
 ```json
 {
     "name": "Название опросника",
     "questions": {
         "номер вопроса": "текст вопроса",
         "номер вопроса": "текст вопроса",
         "номер вопроса": "текст вопроса"
         .
         .
         .
         "номер вопроса": "текст вопроса"
     }
 }
 ``` 

 2. Отправка ответов на вопросы: <br>
 url: `http://localhost:5000/api/qustionnaries/dump_qustionnary_answers`<br>
 method: post<br>
 данные для отправки:
 ```json
{
    "questionnary_name": "Имя опросника",
    "answers": {
        "1": "10", // номер вопроса: ответ на вопрос
        "2": "3",
        "3": "5",
        "4": "1",
        "5": "2",
        "6": "8"
    }
}
 ```

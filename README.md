## Описание
Первое приложение на Flask.

### Требования к ПО
- Инструменты pyenv и poetry.
- Python 3.10

### Установка и запуск
1. Устанавливаем виртуальное окружение и зависимости проекта:
```bash
poetry install
```

2. Запускаем виртуальное окружение
```bash
poetry shell
```

3. Запускаем проект
```bash
python app.py
```
### Примеры тестовых запросов
```bash
1. http://127.0.0.1:5000/candidates/1
2. http://127.0.0.1:5000/candidates/500
3. http://127.0.0.1:5000/
4. http://127.0.0.1:5000/skills/PyThOn
5. http://127.0.0.1:5000/skills/PyThOn345
```

## Задание
Сохраните данные из раскрывашки ниже в JSON файл candidates.json.
```json
[
  {
    "id": 1,
    "name": "Adela Hendricks",
    "picture": "https://picsum.photos/200",
    "position": "Go разработчик",
    "gender": "female",
    "age": 40,
    "skills": "go, python"
  },
  {
    "id": 2,
    "name": "Sheri Torres",
    "picture": "https://picsum.photos/200",
    "position": "Delphi developer",
    "gender": "female",
    "age": 26,
    "skills": "Delphi, pascal, fortran, basic"
  },
  {
    "id": 3,
    "name": "Burt Stein",
    "picture": "https://picsum.photos/200",
    "position": "Team lead",
    "gender": "male",
    "age": 33,
    "skills": "делегирование, пользоваться календарем, обсуждать важные вопросы"
  },
  {
    "id": 4,
    "name": "Bauer Adkins",
    "picture": "https://picsum.photos/200",
    "position": "CTO",
    "gender": "male",
    "age": 37,
    "skills": "very important face"
  },
  {
    "id": 5,
    "name": "Day Holloway",
    "picture": "https://picsum.photos/200",
    "position": "HR manager",
    "gender": "male",
    "age": 35,
    "skills": "LinkedIn, telegram, spam, spam, spam"
  },
  {
    "id": 6,
    "name": "Austin Cochran",
    "picture": "https://picsum.photos/200",
    "position": "python-develop",
    "gender": "male",
    "age": 26,
    "skills": "python, html"
  },
  {
    "id": 7,
    "name": "Sheree Love",
    "picture": "https://picsum.photos/200",
    "position": "Django developer",
    "gender": "female",
    "age": 33,
    "skills": "Python, Django, flask"
  }
]
```

**Шаг 1**

Создайте представление для роута `/` (главная страница).
Выведите список в таком формате (тег `<pre>` - преформатирование)
```
<pre>
  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую

  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую

  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую
<pre>
```

**Шаг 2**

Создайте представление для роута `candidates/<x>`.
Который бы выводил данные про кандидата так:
```
<img src="(ссылка на картинку)">

<pre>
  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую
</pre>
```

**Шаг 3**

Создайте представление `/skills/<x>` для поиска по навыкам.
Выведите тех кандидатов, в списке навыков у которых содержится `skill`.
```
<pre>
  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую

  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую

  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую
<pre>
```

**Критерии выполнения домашнего задания:**

- [x]  Фласк установлен и работает
- [x]  Роуты без параметра применены корректно.
- [x]  Роуты с параметром применены корректно.
- [x]  При запросе на `GET/` выводится список кандидатов
- [x]  При запросе на `GET` `candidate/<x>` выводится один кандидат
- [x]  При запросе на `GET` `skills/<x>` выводятся кандидаты обладающие навыком
- [x]  При поиске не учитывается регистр

**Как сдавать задание**

- [x]  Загрузить весь проект в публичный репозиторий на Github
- [x]  Скопируйте ссылку на репозиторий
- [x]  Сдайте ее на платформе Skypro

---
[SkyPro](https://sky.pro) - [Python Developer](https://sky.pro/courses/programming/python-web-course)

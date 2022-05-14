# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Установите необходимые библиотеки командой `python3 -m pip install -r requirements.txt`
- Добавьте данные согласно [примеру](#пример-данных) в файл `wine.xlsx` или укажите путь к другому файлу в формате `xlsx` в ключе аргумента `--winedata`
- Запустите сайт командой `python3 main.py` или же `python3 main.py --winedata <путь_до_файла_с_данными>`. Также доступна помощь по ключу `--help` или `-h`
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

## Пример данных

|  Категория     |  Название             |  Сорт             |  Цена  |  Картинка                  |  Акция                 |
|----------------|-----------------------|-------------------|--------|----------------------------|------------------------|
|  Белые вина    |  Белая леди           |  Дамский пальчик  |  399   |  belaya_ledi.png           |  Выгодное предложение  |
|  Напитки       |  Коньяк классический  |                   |  350   |  konyak_klassicheskyi.png  |                        |
|  Белые вина    |  Ркацители            |  Ркацители        |  499   |  rkaciteli.png             |                        |
|  Красные вина  |  Черный лекарь        |  Качич            |  399   |  chernyi_lekar.png         |                        |
|  Красные вина  |  Хванчкара            |  Александраули    |  550   |  hvanchkara.png            |                        |
|  Белые вина    |  Кокур                |  Кокур            |  450   |  kokur.png                 |                        |
|  Красные вина  |  Киндзмараули         |  Саперави         |  550   |  kindzmarauli.png          |                        |
|  Напитки       |  Чача                 |                   |  299   |  chacha.png                |  Выгодное предложение  |
|  Напитки       |  Коньяк кизиловый     |                   |  350   |  konyak_kizilovyi.png      |                        |

Обязательно должны присутствовать все столбцы из примера, однако необязательно, чтобы в соответствующих полях были данные.
В поле "Картинка" должен быть указан путь (абсолютный либо относительный) к файлу с изображением вина

На данный момент на месте поля "Акция" может быть указано только "Выгодное предложение"

# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Установите зависимости командой 
``` pip install -r requirements.txt ```
- Укажите в переменных окружения (файл `.env`):
  - `YEAR_OF_FOUNDATION` - год основания компании-заказчика
  - `PATH_TO_XLSX_DB` - путь до "БД" - Excel-файла, содержащего сведения для размещения на сайте. Файл с примером, оформленный в необходимом формате размещен в данном репозитории - `wine.xlsx`
  - `SHEET` - наименование страницы в Excel-файле БД
- Запустите сайт командой ```python3 main.py```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

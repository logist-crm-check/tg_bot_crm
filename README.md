# tg_bot_crm
Касается GIT BASH
$ cd /d переход в другой диск d
$ echo "# tg_bot_crm" >> README.md запись текста в файл
$ cat README.md просмотр содержимого файла 
$ ls список папок
$ ls -a список папок со скрытыми файлами (с точкой в названии)
$ mkdir logist-crm-check создать папку
git init инициализация нового репозитория
$ ls -la вывести в столбик
$ git add README.md добавил новый 
$ git status показывает состояние репозитория локального
$ git push отправляет в GH
$ git add . - добавить всю папку
$ git fetch origin - получить информацию о состоянии репозитория из гитхаба
$ git checkout 1-create-telegram-skeleton перешли на эту ветку, чтобы в ней делать задачу

$ python -m venv .venv создать локальное виртуальное окружение - запусти -m (модуль) и его параметры .venv название папки
$ source .venv/Scripts/activate активация виртуального окружения

Важный момент про библиотеку python-telegram-bot, которую вы будете использовать для написания своего бота: вам нужна версия 12.7 этой библиотеки. На видео Миша её устанавливает командой pip install python telegram-bot, а вы вместо неё выполняйте pip install python-telegram-bot==12.7

No module named 'urllib3' Установите зависимую библиотеку urllib3 через команду pip install urllib3==1.26.20 Важно! Здесь так же зафиксирована конкретная версия библиотеки для бесшовной работы с установленной версией telegram-bot. В случае возникновения иных трудностей, обязательно сообщите куратору - он поможет! - эта версия библиотеки urllib3==1.26.20 работает только с python-telegram-bot==12.7
## Туториал

###Подготовка к работе

Сначала надо склонировать себе проект и настроить окружение у себя на машине.

####Git
Потребуется:
- установить консольный клиент git на машину: https://git-scm.com/downloads
- залогиниться в ваш профиль:
> git config --global user.name "Your name here"

> git config --global user.email "your_email@example.com"

> git config --global color.ui true 

последнее нужно для подсветки синтаксиса, опционально
- склонировать репозиторий и расположить его по удобному вам пути LOCAL_PATH
> git clone https://github.com/sst-tiffany/lpr_site.git LOCAL_PATH

> cd LOCAL_PATH

- предлагаю сразу уйти в свою ветку (я свою назвала tanya)
> git checkout your-branch-name

<br>

####Venv
Я советую создать виртуальное окружение (делается один раз перед началом работы), это позволит изолировать настройки питона и библиотек для этого проекта от прочих проектов на вашей машине.

Для этого нужно выполнить следующие команды:
> PATH_TO_PYTHON -m venv venv

тут PATH_TO_PYTHON - путь к питону на вашей машине, этот питон будет взять в качестве питона для окружения; например, Кате я советую использовать /usr/local/bin/python3.8, а не питон из анаконды

Далее виртуальное окружение надо активировать
> source venv/bin/activate

И поставить в него нужные библиотеки (у нас она пока одна - django, указана в requirements.txt)
> pip install -r requirements.txt

Теперь должно быть можно пробовать запускать проект.

###Начало работы с django-проектом
Для формирования django-проекта я выполнила следующие команды:
> django-admin startproject lpr_site - создало корневую структуру

Далее я сформировала директории для некоторых разделов будущего сайта:
> python manage.py startapp info - создало директорию info, я ее сделала под страницу с информацией о направлении (можно потом совместить с главной, наверное)

> python manage.py startapp news - создало директорию news, я ее сделала под страницу с новостями

> python manage.py startapp persons_and_courses - создало директорию persons_and_courses, эта страница уже готова

Это уже сделано, это больше делать не нужно, указала просто FYI

####Пробный запуск
Для запуска django проекта нужно выполнить
> python manage.py runserver

это даст вот такого вида вывод
```
Django version 3.2.3, using settings 'lpr_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Сайт поднимется на локальной машине, открыть его можно будет в браузере по адресу из вывода выше или по localhost:8000.

Пока на главной там ничего интересного, пока можно пользоваться только
> localhost:8000/persons-and-courses/ 

и админка (об админке в конце).

Чтоб погасить сайт нужно, находясь в том терминале, в котором вы выполняли runserver, прожать Ctrl+C.

Для редактирования сайта не обязательно его гасить, редактировать код можно и тогда, когда сайт поднят, а для применения написанных вами изменений достаточно обновить страницу. 

###Заведение раздела
Я уже писала выше, что сделала задел для разделов новостей и информации. 

Вот что нужно для их редактирования.

####Settings

####Urls

####Views

####Models

#####Migrations


###Редактирование контента (админка)
В админке можно добавлять, изменять и удалять сущности для нашего сайта, например, я делала вкладку с людьми и курсами,
и для нее в админке можно редактировать список людей и курсов. Интерфейс комментировать не буду, там все очевидно. Логин и пароль к админке в чате в тележке. Админка доступна по адресу (когда поднят сайт с помощью runserver).
> localhost:8000/admin



###Заливка вашего кода в удаленный репозиторий
> git add -A

> git commit -m 'your commit message here'

> git push origin your-branch-name

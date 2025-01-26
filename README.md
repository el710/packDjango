# packDjango
1. Download Python
   1.1 Setup
   1.2 Check
   ```
   > python --version
   ```
2. Make virtual environment
   2.1 install pipenv
   ```
   > pip install pipenv
   ```
   >
   2.2 Set variable in system PATH
   ```
    PATH = ....; PIPENV_VENV_IN_PROJECT=venv
   ```
   >
   2.3 setup
   ```
   > pipenv shell
   ```
   >
   2.3 choose python interpreter (in VScode: ctrl + shift + p)
   .venv/Scripts/python.exe
   >
   2.4 restart terminal
3. Get Django
   3.1 Install
   ```
   pip install django
   ```
   >
   3.2 Check
   ```
   django-admin --version
   ```
4. Make project directory
```
django-admin startproject <name>
```
5. Make application
   5.1 come in project directory
   5.2 check project
   ```
   python manage.py runserver
   ```
   5.3 start migration
   ```
   python manage.py migrate
   ```
   5.5 Start develop
   ```
   python manage.py startapp <name>
   ```
   5.6 check
   ```
   python manage.py check
   ```
6. Setup application
   6.1 In project file settings.py add project in INSTALLED_APPS list
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_project',
    ....
]
```
>
   6.2 For html-templates make directory 'templates' in project directory
   and set template directory in settings
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR/'templates/fourth_task',
        ...
```
>
   6.3 Add static directory in settings
   ```
   STATICFILES_DIRS = [                            ## hard url added
    os.path.join(BASE_DIR, 'static')
]
   ``` 
>
   6.4 Make handler-functions of user's requests for html pages in views.py
> 
   6.5 In urls.py add urls for html pages

# cmd: django-admin startproject mysite
- start project name=mysite
    manage.py: file, manage project: run server, migrate database
- create main app name=projectname
    mysite/mysite/__init__.py: convert folder to python package
    mysite/mysite/settings.py: config project: database, installed app, template
    mysite/mysite/urls.py: urls's project
    mysite/mysite/asgi.py: entry point of ASGI server (async server)
    mysite/mysite/wsgi.py: Entry point of WSGI server (use with other server: Gunicorn, uWSGI). 

# cmd: python manage.py startapp news
- create an app name=news
    mysite/news/migrations/: contain migration file of database.
    mysite/news/admin.py: define model show in Django Admin.
    mysite/news/apps.py: config news app in Django.
    mysite/news/models.py: create model define (database table).
    mysite/news/views.py: logic handle request (controller).\
    mysite/news/tests.py: create test case for news app.
    mysite/news/urls.py (manual create): urls route for app.

# add more folder:
- mysite/templates/: contain HTML templates.
- mysite/static/: contain CSS, JS, static image.
- mysite/media/: contain upload file (must config MEDIA_URL and MEDIA_ROOT).
- mysite/logs/: contain log file .
- mysite/env/: Virtual environment.

# cmd: python manage.py migrate
- create database

# cmd: python manage.py createsuperuser
- create superuser: admin accounts

# config mysql in mysite/mysite/settings.py

# add below code in to mysite/mysite/__init__.py after config mysql : new django version required
    import pymysql
    pymysql.version_info=(1, 4, 3, "final", 0)
    pymysql.install_as_MySQLdb()

# config mysite/mysite/news/apps.py in mysite/mysite/settings.py to active mysite/mysite/news/models.py
    INSTALLED_APPS = [
        'news.apps.NewsConfig'
    ]

    run cmd: python manage.py makemigrations news to create define model in models.py of news app

# add models to admin site: mysite/mysite/news/admin.py to crud model
    admin.site.register(Category, CategoryAdmin)

# define CategoryAdmin in mysite/mysite/news/admin.py to config model view in admin
    class CategoryAdmin(admin.ModelAdmin)

# mysite/mysite/static/my_admin/js generate slug with vietnames

# config static file in mysite/mysite/settings.py
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

# tinymce allow to change html content models HTMLFeild
    - add 'tinymce' to mysite/mysite/settings.py on INSTALL_APP
    - add path('tinymce/', include('tinymce.urls')), to mysite/mysite/urls.py to include lib

# manage static image
    - config in mysite/mysite/settings.py
    - add config in mysite/mysite/urls.py
    - config in model: upload_to = 'image/'
    - delete old image when upload new image:
        + add 'django_cleanup.apps.CleanupConfig' to mysite/mysite/settings.py on INSTALL_APP

# add rest_framework to INSTALL_APP to use rest API on mysite/mysite/settings.py

# define serializer model will help to convert object to JSON when use API on mysite/news/serializers.py

# define viewset to support auto CRUD API on mysite/news/views.py





<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Find & Download</title>
</head>
<body>
    <h2>Nhập Label ID:</h2>
    <input type="text" id="labelId" placeholder="Nhập ID...">
    <button onclick="findData()">Find</button>

    <h2>Chọn giá trị:</h2>
    <label for="dropdown1">Option 1:</label>
    <select id="dropdown1"></select>

    <label for="dropdown2">Option 2:</label>
    <select id="dropdown2"></select>

    <label for="dropdown3">Option 3:</label>
    <select id="dropdown3"></select>

    <br><br>
    <button onclick="downloadFile()">Download</button>

    <script>
        function findData() {
            let labelId = document.getElementById("labelId").value;
            fetch(`/api/get-data/?id=${labelId}`)
                .then(response => response.json())
                .then(data => {
                    fillDropdown("dropdown1", data.key1);
                    fillDropdown("dropdown2", data.key2);
                    fillDropdown("dropdown3", data.key3);
                })
                .catch(error => console.error("Lỗi:", error));
        }

        function fillDropdown(dropdownId, values) {
            let dropdown = document.getElementById(dropdownId);
            dropdown.innerHTML = "";
            values.forEach(value => {
                let option = document.createElement("option");
                option.value = value;
                option.textContent = value;
                dropdown.appendChild(option);
            });
        }

        function downloadFile() {
            let selected1 = document.getElementById("dropdown1").value;
            let selected2 = document.getElementById("dropdown2").value;
            let selected3 = document.getElementById("dropdown3").value;

            let params = new URLSearchParams({
                option1: selected1,
                option2: selected2,
                option3: selected3
            });

            window.location.href = `/api/download/?${params.toString()}`;
        }
    </script>
</body>
</html>

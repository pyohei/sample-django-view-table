# Sample application of django-view-table

This is sample application of `django-view-table` plugin.  
You can use its plugin under the below database.  

* SQLite
* MySQL
* Postgresql

## Usage

Please install python library with pip or your favarite python plugin manager.  

```bash
pip install -r requirements.txt
```

If you want to run mysql or postgresql, please execute docker-compose.  

```bash
docker-compose up
```  

and, you need to edit `django_sample/settings.py`.  
Change `default` of `DATABASES` your database engine.  

This is because, `django-view-table` plugin can not use `database` option.  

After that, run command as follows:

```bash
python manage.py migrate
python manage.py loaddata book.json
python manage.py createviewtable
python manage.py runserver
```

You can confirm your view table to access `http://127.0.0.1:8000/polls/`.  

# License

MIT
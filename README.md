# Django Backend Test (with PyMySQL)
Created to test if the database connector has any issue with Django ORM.

## Known issues with PyMySQL

Solved) [Duplicate keyword '_binary' failure when using BinaryField in Django](https://github.com/PyMySQL/PyMySQL/issues/549)

WIP) [Compatibility with Django 2.2](https://github.com/PyMySQL/PyMySQL/issues/790)

### 1. Modify database connection.
```
(1) Open ./django_backend_test/settings.py
(2) Modify line 80-95
```

### 2. Create test database server (using Docker)
```
docker run -d -e MYSQL_ROOT_PASSWORD=eavictor -e MYSQL_DATABASE=DJANGO_BACKEND_TEST -e MYSQL_USER=eavictor -e MYSQL_PASSWORD=mysql_password -p 3306:3306 mariadb:latest --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --max_connect_errors=4294967695 --expire_logs_days=1
```

### 3. Install required packages (Django, PyMySQL/MySQLClient, pillow)
```
sudo pip3 install -Ur req_pymysql.txt --no-cache-dir
```
```
sudo pip3 install -Ur req_mysqlclient.txt --no-cache-dir
```

### 4. Create Database migration
```
python3 manage.py makemigrations
```

### 5. Run test
```
python3 manage.py test
```
It will create a test database automatically, then delete it after all tests are complete.


### List of test fields:
Auto Increment
```
AutoField  # default in models, no need to write this test case
BigAutoField
```

Boolean
```
BooleanField
NullBooleanField
```
Number
```
IntegerField
BigIntegerField
FloatField
DecimalField
```
DateTime
```
DateField
TimeField
DateTimeField
```
String
```
CharField
TextField
```
File related
```
FileField
FilePathField   # Might raise DataError (1406, "Data too long for column 'value' at row 1")
ImageField
```
Binary object
```
BinaryField
```

### Where to find test code:

Database Models:
```
/django_backend_test/test_backend/models.py
```

Test Cases:
```
/django_backend_test/test_backend/tests.py
```

# Django Backend Test (with PyMySQL)
For testing if the database connector works with Django ORM.

### 1. Modify database connection.
```
(1) Open /django_backend_test/django_backend_test/settings.py
(2) Modify line 80-95
```

### 2. Create a test database by using docker
```
docker run -d -e MYSQL_ROOT_PASSWORD=eavictor -e MYSQL_DATABASE=DJANGO_BACKEND_TEST -e MYSQL_USER=eavictor -e MYSQL_PASSWORD=mysql_password -p 3306:3306 mariadb:latest
```

[Duplicate keyword '_binary' failure when using BinaryField in Django](https://github.com/PyMySQL/PyMySQL/issues/549)

### 3. Install required packages (Django, PyMySQL, pillow)
```
sudo pip3 install -Ur requirements.txt --no-cache-dir
```

### 4. Run test
```
python3 manage.py test
```
It will create a test database automatically, then delete it after all tests are complete.


### List of tested fields:
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
FilePathField
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

Tests:
```
/django_backend_test/test_backend/tests.py
```

# Django backend test
For testing if the database connector works with Django ORM.

### 1. Modify database connection.
```
(1) Open /django_backend_test/django_backend_test/settings.py
(2) Modify line 76-92
```

### 2. Uncomment BinaryField test (if not using PyMySQL)
Reason for disable BinaryField test by default:

[Duplicate keyword '_binary' failure when using BinaryField in Django](https://github.com/PyMySQL/PyMySQL/issues/549)

### 3. Install required packages (Django, PyMySQL, pillow)
```
sudo pip3 --no-cache-dir install -Ur requirements.txt
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
Binary object (ignored by default)
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

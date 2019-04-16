from django.db import models
import os
from django_backend_test.settings import BASE_DIR


# Create your models here.
class ModelBigAutoField(models.Model):
    id = models.BigAutoField(primary_key=True)


class ModelBoolean(models.Model):
    value = models.BooleanField()


class ModelNullBoolean(models.Model):
    value = models.NullBooleanField()


class ModelInteger(models.Model):
    value = models.IntegerField()


class ModelBigInteger(models.Model):
    value = models.BigIntegerField()


class ModelFloat(models.Model):
    value = models.FloatField()


class ModelDecimal(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=3)


class ModelDate(models.Model):
    value = models.DateField(auto_now_add=True)


class ModelTime(models.Model):
    value = models.TimeField(auto_now_add=True)


class ModelDateTime(models.Model):
    value = models.DateTimeField(auto_now_add=True)


class ModelChar(models.Model):
    value = models.CharField(max_length=100)


class ModelText(models.Model):
    value = models.TextField()


class ModelFile(models.Model):
    value = models.FileField(upload_to='file/')


class ModelFilePath(models.Model):
    value = models.FilePathField(path=os.path.join(BASE_DIR, 'trashcan', 'file_path'))


class ModelImage(models.Model):
    value = models.ImageField(upload_to='image/', default=os.path.join(BASE_DIR, 'test_backend', 'files', '2B.jpg'))


class ModelBinary(models.Model):
    value = models.BinaryField()

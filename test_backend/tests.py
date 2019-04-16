import os
from django.test import TestCase
from decimal import Decimal
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django_backend_test.settings import BASE_DIR
from test_backend.models import \
    ModelBoolean,\
    ModelNullBoolean,\
    ModelInteger,\
    ModelBigInteger,\
    ModelFloat,\
    ModelDecimal,\
    ModelDate,\
    ModelTime,\
    ModelDateTime,\
    ModelChar,\
    ModelText,\
    ModelFile,\
    ModelFilePath,\
    ModelImage,\
    ModelBinary


# Create your tests here.
class BooleanFieldTestCase(TestCase):
    def setUp(self):
        _boolean = ModelBoolean.objects.create(value=True)
        self.id = _boolean.id

    def test_boolean_1_query(self):
        self.assertEquals(ModelBoolean.objects.get(id=self.id).value, True)

    def test_boolean_2_update(self):
        ModelBoolean.objects.filter(id=self.id).update(value=False)
        self.assertEquals(ModelBoolean.objects.get(id=self.id).value, False)

    def test_boolean_3_delete(self):
        ModelBoolean.objects.get(id=self.id).delete()
        self.assertEquals(ModelBoolean.objects.all().count(), 0)


class NullBooleanFieldTestCase(TestCase):
    def setUp(self):
        _null_boolean = ModelNullBoolean.objects.create(value=None)
        self.id = _null_boolean.id

    def test_null_boolean_1_query(self):
        self.assertEquals(ModelNullBoolean.objects.get(id=self.id).value, None)

    def test_null_boolean_2_update(self):
        ModelNullBoolean.objects.filter(id=self.id).update(value=True)
        self.assertEquals(ModelNullBoolean.objects.get(id=self.id).value, True)

    def test_null_boolean_3_delete(self):
        ModelNullBoolean.objects.get(id=self.id).delete()
        self.assertEquals(ModelNullBoolean.objects.all().count(), 0)


class IntegerFieldTestCase(TestCase):
    def setUp(self):
        _integer = ModelInteger.objects.create(value=0)
        self.id = _integer.id

    def test_integer_1_query(self):
        self.assertEquals(ModelInteger.objects.get(id=self.id).value, 0)

    def test_integer_2_update(self):
        ModelInteger.objects.filter(id=self.id).update(value=1)
        self.assertEquals(ModelInteger.objects.get(id=self.id).value, 1)

    def test_integer_3_delete(self):
        ModelInteger.objects.get(id=self.id).delete()
        self.assertEquals(ModelInteger.objects.all().count(), 0)


class BigIntegerFieldTestCase(TestCase):
    def setUp(self):
        _big_integer = ModelBigInteger.objects.create(value=0)
        self.id = _big_integer.id

    def test_big_integer_1_query(self):
        self.assertEquals(ModelBigInteger.objects.get(id=self.id).value, 0)

    def test_big_integer_2_update(self):
        ModelBigInteger.objects.filter(id=self.id).update(value=1)
        self.assertEquals(ModelBigInteger.objects.get(id=self.id).value, 1)

    def test_big_integer_3_delete(self):
        ModelBigInteger.objects.get(id=self.id).delete()
        self.assertEquals(ModelBigInteger.objects.all().count(), 0)


class FloatFieldTestCase(TestCase):
    def setUp(self):
        _float = ModelFloat.objects.create(value=0.1)
        self.id = _float.id

    def test_float_1_query(self):
        self.assertEquals(ModelFloat.objects.get(id=self.id).value, 0.1)

    def test_float_2_update(self):
        ModelFloat.objects.filter(id=self.id).update(value=9.487)
        self.assertEquals(ModelFloat.objects.get(id=self.id).value, 9.487)

    def test_float_3_delete(self):
        ModelFloat.objects.get(id=self.id).delete()
        self.assertEquals(ModelFloat.objects.all().count(), 0)


class DecimalFieldTestCase(TestCase):
    def setUp(self):
        _decimal = ModelDecimal.objects.create(value=Decimal('12.34'))
        self.id = _decimal.id

    def test_decimal_1_query(self):
        self.assertEquals(ModelDecimal.objects.get(id=self.id).value, Decimal('12.34'))

    def test_decimal_2_update(self):
        ModelDecimal.objects.filter(id=self.id).update(value=Decimal('56.78'))
        self.assertEquals(ModelDecimal.objects.get(id=self.id).value, Decimal('56.78'))

    def test_decimal_3_delete(self):
        ModelDecimal.objects.get(id=self.id).delete()
        self.assertEquals(ModelDecimal.objects.all().count(), 0)


class DateFieldTestCase(TestCase):
    def setUp(self):
        _date = ModelDate.objects.create()  # auto_now_add=True
        self.id = _date.id
        self.date = _date.value

    def test_date_1_query(self):
        self.assertEquals(ModelDate.objects.get(id=self.id).value, self.date)

    def test_date_2_update(self):
        now = timezone.now().date()
        ModelDate.objects.filter(id=self.id).update(value=now)
        self.assertEquals(ModelDate.objects.get(id=self.id).value, now)

    def test_date_3_delete(self):
        ModelDate.objects.get(id=self.id).delete()
        self.assertEquals(ModelDate.objects.all().count(), 0)


class TimeFieldTestCase(TestCase):
    def setUp(self):
        _time = ModelTime.objects.create()  # auto_now_add=True
        self.id = _time.id
        self.time = _time.value

    def test_time_1_query(self):
        self.assertEquals(ModelTime.objects.get(id=self.id).value, self.time)

    def test_time_2_update(self):
        now = timezone.now().time()
        ModelTime.objects.filter(id=self.id).update(value=now)
        self.assertEquals(ModelTime.objects.get(id=self.id).value, now)

    def test_time_3_delete(self):
        ModelTime.objects.get(id=self.id).delete()
        self.assertEquals(ModelTime.objects.all().count(), 0)


class DateTimeFieldTestCase(TestCase):
    def setUp(self):
        _datetime = ModelDateTime.objects.create()  # auto_now_add=True\
        self.id = _datetime.id
        self.datetime = _datetime.value

    def test_datetime_1_query(self):
        self.assertEquals(ModelDateTime.objects.get(id=self.id).value, self.datetime)

    def test_datetime_2_update(self):
        now = timezone.now()
        ModelDateTime.objects.filter(id=self.id).update(value=now)
        self.assertEquals(ModelDateTime.objects.get(id=self.id).value, now)

    def test_datetime_3_delete(self):
        ModelDateTime.objects.get(id=self.id).delete()
        self.assertEquals(ModelDateTime.objects.all().count(), 0)


class CharFieldTestCase(TestCase):
    def setUp(self):
        _char = ModelChar.objects.create(value='https://github.com/eavictor')
        self.id = _char.id

    def test_char_1_query(self):
        self.assertEquals(ModelChar.objects.get(id=self.id).value, 'https://github.com/eavictor')

    def test_char_2_update(self):
        _char = ModelChar.objects.filter(id=self.id).update(value='https://twitter.com/eavictor')
        self.assertEquals(ModelChar.objects.get(id=self.id).value, 'https://twitter.com/eavictor')

    def test_char_3_delete(self):
        ModelChar.objects.get(id=self.id).delete()
        self.assertEquals(ModelChar.objects.all().count(), 0)


class TextFieldTestCase(TestCase):
    def setUp(self):
        _text = ModelText.objects.create(value='https://github.com/eavictor')
        self.id = _text.id

    def test_text_1_query(self):
        self.assertEquals(ModelText.objects.get(id=self.id).value, 'https://github.com/eavictor')

    def test_text_2_update(self):
        ModelText.objects.filter(id=self.id).update(value='https://twitter.com/eavictor')
        self.assertEquals(ModelText.objects.get(id=self.id).value, 'https://twitter.com/eavictor')

    def test_text_3_delete(self):
        ModelText.objects.get(id=self.id).delete()
        self.assertEquals(ModelText.objects.all().count(), 0)


class FileFieldTestCase(TestCase):
    def setUp(self):
        file_2b = open(os.path.join(BASE_DIR, 'test_backend', 'files', '2B.jpg'), 'rb')
        _file = ModelFile.objects.create(value=SimpleUploadedFile(name='2B.jpg',
                                                                  content=file_2b.read(),
                                                                  content_type='image/jpeg'
                                                                  )
                                         )
        file_2b.close()
        self.id = _file.id
        self.file = _file.value

    def test_file_1_query(self):
        _file = ModelFile.objects.get(id=self.id)
        self.assertEquals(_file.value, self.file)

    def test_file_2_update(self):
        file_2b_9s = open(os.path.join(BASE_DIR, 'test_backend', 'files', '2B_9S.jpg'), 'rb')
        _file = ModelFile.objects.get(id=self.id)
        _file.value = SimpleUploadedFile(name='2B_9S.jpg', content=file_2b_9s.read(), content_type='image/jpeg')
        _file.save()
        file_2b_9s.close()
        _verify = ModelFile.objects.get(id=self.id)
        self.assertEquals(_verify.value, _file.value)

    def test_file_3_delete(self):
        _file = ModelFile.objects.get(id=self.id)
        _file.delete()
        count = ModelFile.objects.all().count()
        self.assertEquals(count, 0)


class FilePathFieldTestCase(TestCase):
    def setUp(self):
        _file_path = ModelFilePath.objects.create(value=os.path.join(BASE_DIR, 'test_backend', 'files', '2B.jpg'))
        _file_path.save()
        self.id = _file_path.id

    def test_file_path_1_query(self):
        self.assertEquals(ModelFilePath.objects.get(id=self.id).value,
                          os.path.join(BASE_DIR, 'test_backend', 'files', '2B.jpg')
                          )

    def test_file_path_2_update(self):
        path = os.path.join(BASE_DIR, 'test_backend', 'files', '2B_9S.jpg')
        ModelFilePath.objects.filter(id=self.id).update(value=path)
        self.assertEquals(ModelFilePath.objects.get(id=self.id).value, path)

    def test_file_path_3_delete(self):
        ModelFilePath.objects.get(id=self.id).delete()
        self.assertEquals(ModelFilePath.objects.all().count(), 0)


class ImageFieldTestCase(TestCase):
    def setUp(self):
        image_2b = open(os.path.join(BASE_DIR, 'test_backend', 'files', '2B.jpg'), 'rb')
        simple_uploaded_file = SimpleUploadedFile(name='2B.jpg',
                                                  content=image_2b.read(),
                                                  content_type='image/jpeg'
                                                  )
        _image = ModelImage.objects.create(value=simple_uploaded_file)
        image_2b.close()
        self.id = _image.id
        self.image = _image.value

    def test_image_1_query(self):
        self.assertEquals(ModelImage.objects.get(id=self.id).value, self.image)

    def test_image_2_update(self):
        image_2b_9s = open(os.path.join(BASE_DIR, 'test_backend', 'files', '2B_9S.jpg'), 'rb')
        simple_uploaded_file = SimpleUploadedFile(name='2B_9S.jpg',
                                                  content=image_2b_9s.read(),
                                                  content_type='image/jpeg'
                                                  )
        image_2b_9s.close()
        _image = ModelImage.objects.filter(id=self.id).update(value=simple_uploaded_file)
        self.assertEquals(ModelImage.objects.get(id=self.id).value, simple_uploaded_file)

    def test_image_3_delete(self):
        ModelImage.objects.get(id=self.id).delete()
        self.assertEquals(ModelImage.objects.all().count(), 0)


class BinaryFieldTestCase(TestCase):
    def setUp(self):
        _binary = ModelBinary.objects.create(value=b'https://github.com/eavictor')
        self.id = _binary.id

    def test_binary_1_query(self):
        self.assertEquals(ModelBinary.objects.get(id=self.id).value, b'https://github.com/eavictor')

    def test_binary_2_update(self):
        _binary = ModelBinary.objects.filter(id=self.id).update(value=b'https://twitter.com/eavictor')
        self.assertEquals(ModelBinary.objects.get(id=self.id).value, b'https://twitter.com/eavictor')

    def test_binary_3_delete(self):
        ModelBinary.objects.get(id=self.id).delete()
        self.assertEquals(ModelBinary.objects.all().count(), 0)

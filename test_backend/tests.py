from django.test import TestCase
import os
from decimal import Decimal
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django_backend_test.settings import BASE_DIR
from .models import \
    ModelBoolean,\
    ModelNullBoolean,\
    ModelInteger,\
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
        _boolean.save()
        self.id = _boolean.id

    def test_boolean_1_query(self):
        _boolean = ModelBoolean.objects.get(id=self.id)
        self.assertEquals(_boolean.value, True)

    def test_boolean_2_update(self):
        _boolean = ModelBoolean.objects.get(id=self.id)
        _boolean.value = False
        _boolean.save()
        _verify = ModelBoolean.objects.get(id=self.id)
        self.assertEquals(_verify.value, _boolean.value)

    def test_boolean_3_delete(self):
        _boolean = ModelBoolean.objects.get(id=self.id)
        _boolean.delete()
        count = ModelBoolean.objects.all().count()
        self.assertEquals(count, 0)


class NullBooleanFieldTestCase(TestCase):
    def setUp(self):
        _null_boolean = ModelNullBoolean.objects.create(value=None)
        _null_boolean.save()
        self.id = _null_boolean.id

    def test_null_boolean_1_query(self):
        _null_boolean = ModelNullBoolean.objects.get(id=self.id)
        self.assertEquals(_null_boolean.value, None)

    def test_null_boolean_2_update(self):
        _null_boolean = ModelNullBoolean.objects.get(id=self.id)
        _null_boolean.value = True
        _null_boolean.save()
        _verify = ModelNullBoolean.objects.get(id=self.id)
        self.assertEquals(_verify.value, _null_boolean.value)

    def test_null_boolean_3_delete(self):
        _null_boolean = ModelNullBoolean.objects.get(id=self.id)
        _null_boolean.delete()
        count = ModelNullBoolean.objects.all().count()
        self.assertEquals(count, 0)


class IntegerFieldTestCase(TestCase):
    def setUp(self):
        _integer = ModelInteger.objects.create(value=0)
        _integer.save()
        self.id = _integer.id

    def test_integer_1_query(self):
        _integer = ModelInteger.objects.get(id=self.id)
        self.assertEquals(_integer.value, 0)

    def test_integer_2_update(self):
        _integer = ModelInteger.objects.get(id=self.id)
        _integer.value = 1
        _integer.save()
        _verify = ModelInteger.objects.get(id=self.id)
        self.assertEquals(_verify.value, _integer.value)

    def test_integer_3_delete(self):
        _integer = ModelInteger.objects.get(id=self.id)
        _integer.delete()
        count = ModelInteger.objects.all().count()
        self.assertEquals(count, 0)


class FloatFieldTestCase(TestCase):
    def setUp(self):
        _float = ModelFloat.objects.create(value=0.1)
        _float.save()
        self.id = _float.id

    def test_float_1_query(self):
        _float = ModelFloat.objects.get(id=self.id)
        self.assertEquals(_float.value, 0.1)

    def test_float_2_update(self):
        _float = ModelFloat.objects.get(id=self.id)
        _float.value = 9.487
        _float.save()
        _verify = ModelFloat.objects.get(id=self.id)
        self.assertEquals(_verify.value, _float.value)

    def test_float_3_delete(self):
        _float = ModelFloat.objects.get(id=self.id)
        _float.delete()
        count = ModelFloat.objects.all().count()
        self.assertEquals(count, 0)


class DecimalFieldTestCase(TestCase):
    def setUp(self):
        _decimal = ModelDecimal.objects.create(value=12.34)
        _decimal.save()
        self.id = _decimal.id

    def test_decimal_1_query(self):
        _decimal = ModelDecimal.objects.get(id=self.id)
        self.assertEquals(_decimal.value, Decimal('12.34'))

    def test_decimal_2_update(self):
        _decimal = ModelDecimal.objects.get(id=self.id)
        _decimal.value = Decimal('56.78')
        _decimal.save()
        _verify = ModelDecimal.objects.get(id=self.id)
        self.assertEquals(_verify.value, _decimal.value)

    def test_decimal_3_delete(self):
        _decimal = ModelDecimal.objects.get(id=self.id)
        _decimal.delete()
        count = ModelDecimal.objects.all().count()
        self.assertEquals(count, 0)


class DateFieldTestCase(TestCase):
    def setUp(self):
        _date = ModelDate.objects.create()  # auto_now_add=True
        _date.save()
        self.id = _date.id
        self.date = _date.value

    def test_date_1_query(self):
        _date = ModelDate.objects.get(id=self.id)
        self.assertEquals(_date.value, self.date)

    def test_date_2_update(self):
        _date = ModelDate.objects.get(id=self.id)
        _date.value = timezone.now().date()
        _date.save()
        _verify = ModelDate.objects.get(id=self.id)
        self.assertEquals(_verify.value, _date.value)

    def test_date_3_delete(self):
        _date = ModelDate.objects.get(id=self.id)
        _date.delete()
        count = ModelDate.objects.all().count()
        self.assertEquals(count, 0)


class TimeFieldTestCase(TestCase):
    def setUp(self):
        _time = ModelTime.objects.create()  # auto_now_add=True
        _time.save()
        self.id = _time.id
        self.time = _time.value

    def test_time_1_query(self):
        _time = ModelTime.objects.get(id=self.id)
        self.assertEquals(_time.value, self.time)

    def test_time_2_update(self):
        _time = ModelTime.objects.get(id=self.id)
        _time.value = timezone.now().time()
        _time.save()
        _verify = ModelTime.objects.get(id=self.id)
        self.assertEquals(_verify.value, _time.value)

    def test_time_3_delete(self):
        _time = ModelTime.objects.get(id=self.id)
        _time.delete()
        count = ModelTime.objects.all().count()
        self.assertEquals(count, 0)


class DateTimeFieldTestCase(TestCase):
    def setUp(self):
        _datetime = ModelDateTime.objects.create()  # auto_now_add=True
        _datetime.save()
        self.id = _datetime.id
        self.datetime = _datetime.value

    def test_datetime_1_query(self):
        _datetime = ModelDateTime.objects.get(id=self.id)
        self.assertEquals(_datetime.value, self.datetime)

    def test_datetime_2_update(self):
        _datetime = ModelDateTime.objects.get(id=self.id)
        _datetime.value = timezone.now()
        _datetime.save()
        _verify = ModelDateTime.objects.get(id=self.id)
        self.assertEquals(_verify.value, _datetime.value)

    def test_datetime_3_delete(self):
        _datetime = ModelDateTime.objects.get(id=self.id)
        _datetime.delete()
        count = ModelDateTime.objects.all().count()
        self.assertEquals(count, 0)


class CharFieldTestCase(TestCase):
    def setUp(self):
        _char = ModelChar.objects.create(value='https://github.com/eavictor')
        _char.save()
        self.id = _char.id

    def test_char_1_query(self):
        _char = ModelChar.objects.get(id=self.id)
        self.assertEquals(_char.value, 'https://github.com/eavictor')

    def test_char_2_update(self):
        _char = ModelChar.objects.get(id=self.id)
        _char.value = 'https://twitter.com/eavictor'
        _char.save()
        _verify = ModelChar.objects.get(id=self.id)
        self.assertEquals(_verify.value, _char.value)

    def test_char_3_delete(self):
        _char = ModelChar.objects.get(id=self.id)
        _char.delete()
        count = ModelChar.objects.all().count()
        self.assertEquals(count, 0)


class TextFieldTestCase(TestCase):
    def setUp(self):
        _text = ModelText.objects.create(value='https://github.com/eavictor')
        _text.save()
        self.id = _text.id

    def test_text_1_query(self):
        _text = ModelText.objects.get(id=self.id)
        self.assertEquals(_text.value, 'https://github.com/eavictor')

    def test_text_2_update(self):
        _text = ModelText.objects.get(id=self.id)
        _text.value = 'https://twitter.com/eavictor'
        _text.save()
        _verify = ModelText.objects.get(id=self.id)
        self.assertEquals(_verify.value, _text.value)

    def test_text_3_delete(self):
        _text = ModelText.objects.get(id=self.id)
        _text.delete()
        count = ModelText.objects.all().count()
        self.assertEquals(count, 0)


class FileFieldTestCase(TestCase):
    def setUp(self):
        file_2b = open(os.path.join(BASE_DIR, 'test_backend', 'files', '2B.jpg'), 'rb')
        _file = ModelFile.objects.create(value=SimpleUploadedFile(name='2B.jpg',
                                                                  content=file_2b.read(),
                                                                  content_type='image/jpeg'
                                                                  )
                                         )
        _file.save()
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
        _file_path = ModelFilePath.objects.get(id=self.id)
        self.assertEquals(_file_path.value, os.path.join(BASE_DIR, 'test_backend', 'files', '2B.jpg'))

    def test_file_path_2_update(self):
        _file_path = ModelFilePath.objects.get(id=self.id)
        _file_path.path = os.path.join(BASE_DIR, 'test_backend', 'files', '2B_9S.jpg')
        _file_path.save()
        _verify = ModelFilePath.objects.get(id=self.id)
        self.assertEquals(_verify.value, _file_path.value)

    def test_file_path_3_delete(self):
        _file_path = ModelFilePath.objects.get(id=self.id)
        _file_path.delete()
        count = ModelFilePath.objects.all().count()
        self.assertEquals(count, 0)


class ImageFieldTestCase(TestCase):
    def setUp(self):
        image_2b = open(os.path.join(BASE_DIR, 'test_backend', 'files', '2B.jpg'), 'rb')
        _image = ModelImage.objects.create(value=SimpleUploadedFile(name='2B.jpg',
                                                                    content=image_2b.read(),
                                                                    content_type='image/jpeg'
                                                                    )
                                           )
        _image.save()
        self.id = _image.id
        self.image = _image.value
        image_2b.close()

    def test_image_1_query(self):
        _image = ModelImage.objects.get(id=self.id)
        self.assertEquals(_image.value, self.image)

    def test_image_2_update(self):
        image_2b_9s = open(os.path.join(BASE_DIR, 'test_backend', 'files', '2B_9S.jpg'), 'rb')
        _image = ModelImage.objects.get(id=self.id)
        _image.image = SimpleUploadedFile(name='2B_9S.jpg',
                                          content=image_2b_9s.read(),
                                          content_type='image/jpeg'
                                          )
        _image.save()
        image_2b_9s.close()
        _verify = ModelImage.objects.get(id=self.id)
        self.assertEquals(_verify.value, _image.value)

    def test_image_3_delete(self):
        _image = ModelImage.objects.get(id=self.id)
        _image.delete()
        count = ModelImage.objects.all().count()
        self.assertEquals(count, 0)


class BinaryFieldTestCase(TestCase):
    def setUp(self):
        _binary = ModelBinary.objects.create(value=b'https://github.com/eavictor')
        _binary.save()
        self.id = _binary.id

    def test_binary_1_query(self):
        _binary = ModelBinary.objects.get(id=self.id)
        self.assertEquals(_binary.value, b'https://github.com/eavictor')

    def test_binary_2_update(self):
        _binary = ModelBinary.objects.get(id=self.id)
        _binary.value = b'https://twitter.com/eavictor'
        _binary.save()
        _verify = ModelBinary.objects.get(id=self.id)
        self.assertEquals(_verify.value, _binary.value)

    def test_binary_3_delete(self):
        _binary = ModelBinary.objects.get(id=self.id)
        _binary.delete()
        count = ModelBinary.objects.all().count()
        self.assertEquals(count, 0)

from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField, DateField


class Shop(models.Model):
    # 1번 방식 - models.OOO
    shop_id = models.IntegerField(primary_key=True)

    # 2번 방식 - 미리 import 한 이후 사용
    shop_name = CharField(max_length=100, null=True)
    shop_desc = CharField(max_length=100, null=True)
    rest_date = CharField(max_length=100, null=True)
    parking_info = CharField(max_length=100, null=True)
    img_path = CharField(max_length=255, null=True)

    class Meta:
        db_table = 'shop'  # 옵션이 없으면 thirdapp_shop 테이블 생성
        app_label = 'thirdapp'
        managed = False

class JejuOlle(models.Model):
  course = CharField(max_length=10)
  course_name = CharField(max_length=20)
  distance = FloatField()
  time_info = CharField(max_length=10)
  start_end_info = CharField(max_length=30)
  cre_date = DateField()

  class Meta:
    db_table = 'jeju_olle'
    managed = False

class Owner(models.Model):
  name = models.CharField(max_length=50, null=True)
  
  class Meta:
    db_table = 'owner'
    managed = False

class Animal(models.Model):
  name = models.CharField(max_length=50, null=True)
  age = models.IntegerField(null=True)
  owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
#  owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)

  class Meta:
    db_table = 'animal'
    managed = False

class Playground(models.Model):
  name = models.CharField(max_length=50, null=True)
  address = models.CharField(max_length=50, null=True)
  tel = models.CharField(max_length=20, null=True)
  animals = models.ManyToManyField(Animal, null=True)

  class Meta:
    db_table = 'playground'
    managed = False

class Warranty(models.Model):
  model_nm = models.CharField(max_length=50, null=True)
  period = models.IntegerField(null=True)

  class Meta:
    db_table = 'warranty'
    managed = False

class Product(models.Model):
  name = models.CharField(max_length=50, null=True)
  price = models.IntegerField(null=True)
  animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)
  warranty = models.OneToOneField(Warranty, on_delete=models.SET_NULL, null=True)

  class Meta:
    db_table = 'product'
    managed = False
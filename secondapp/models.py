from django.db import models

class ArmyShop(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.TextField()
    name = models.TextField()

    class Meta:
        db_table = 'army_shop'
        managed = False

# 1. 클래스
# 2. 모델 상속
# 3. 속성 => 변수 = OOOField 대입
class Course(models.Model):
    # Integer BigInteger
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()
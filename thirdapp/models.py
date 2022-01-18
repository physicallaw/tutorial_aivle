from django.db import models
from django.db.models.fields import CharField, IntegerField
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
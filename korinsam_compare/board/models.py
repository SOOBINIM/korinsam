from django.db import models

class Board(models.Model):
    no = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=128, verbose_name='상품명')
    standard = models.CharField(max_length=64, verbose_name='규격')
    stock = models.IntegerField(blank=True, null=True)
    stock_status = models.CharField(max_length=64, verbose_name='재고상태')

    def __str__(self):
        return self.product_name

    class Meta:
        # db_table = 'korinsam_stockList'
        verbose_name = '고려인삼 재고리스트'
        verbose_name_plural = '고려인삼 재고리스트'

# class Product(models.Model):
#     product_name = models.CharField(max_length=128)

#     def __str__(self):
#         return self.product_name

# class Client(models.Model):
#     product = models.ForeignKey(Product, on_delete = models.CASCADE)
#     client_name = models.CharField(max_length=50, null = True, default='고객사입력')    
    
    
# class Price(models.Model):
#     client = models.ForeignKey(Client, on_delete = models.CASCADE)
#     selling_price = models.IntegerField(blank = True, null = True)  # 판매가     
#     supply_price = models.IntegerField(blank = True, null = True)  # 공급가
#     setteld_price = models.IntegerField(blank = True, null = True)  # 정산가
#     shipping_price = models.IntegerField(blank = True, null = True) # 배송비
#     fee = models.IntegerField(blank = True, null = True)    # 수수료
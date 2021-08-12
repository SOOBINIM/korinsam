from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_subject = models.CharField(max_length=32)
    product_stock = models.IntegerField(blank= True, null= True)

    def __str__(self):
        return self.product_name

# class Client(models.Model):
#     product = models.ForeignKey(Product, on_delete = models.CASCADE)
#     client_name = models.CharField(max_length=50, null = True, default='고객사입력')
       
#     def __str__(self):
#         return self.client_name    
    
    
# class Price(models.Model):
#     client = models.ForeignKey(Client, on_delete = models.CASCADE)
#     selling_price = models.IntegerField(blank = True, null = True)  # 판매가     
#     supply_price = models.IntegerField(blank = True, null = True)  # 공급가
#     setteld_price = models.IntegerField(blank = True, null = True)  # 정산가
#     shipping_price = models.IntegerField(blank = True, null = True) # 배송비
#     fee = models.IntegerField(blank = True, null = True)    # 수수료
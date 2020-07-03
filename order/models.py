from django.db import models

from menu.models import Drink


class Order(models.Model):
    #drink, stack, cup, ice, sugar, pearl, price
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name='order')
    stock = models.PositiveIntegerField()       #양수
    cup = models.IntegerField()     # 0: 레귤러, 1: 점보
    ice = models.IntegerField(default=100)      #0, 50, 100, 150%
    sugar = models.IntegerField(default=100)    #0, 50, 100, 150%
    price = models.IntegerField()

    def __str__(self):
        return f'{self.drink}, 개수: {self.stock}, 컵사이즈: {self.cup}, 얼음량: {self.ice}, 당도: {self.sugar}, 가격: {self.price}'
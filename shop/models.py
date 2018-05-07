from django.db import models


class Catalog(models.Model):
    title = models.CharField('Каталог', max_length=60)


class Shop(models.Model):
    name = models.CharField('Название', max_length=60)
    description = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='shop/', blank=True)
    cost = models.PositiveIntegerField('Цена')
    catalog = models.ForeignKey('Catalog', on_delete=models.CASCADE)

    def get_image_url(self):
        if self.image.url is None:
            return 'media/shop/default.jpg'

from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True', 'Hawa'),
        ('False','Yok'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=255, choices=STATUS)

    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    create_at =  models.DateTimeField(auto_now_add = True)
    update_at =  models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'Hawa'),
        ('False','Yok'),
    )
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at =  models.DateTimeField(auto_now_add = True)
    update_at =  models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title    

    def image_tag(self):
        return mark_safe('<img src="{}" height="78"/>'.format(self.image.url))
    image_tag.short_description= 'Image'  



class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=50, blank=True)  #BLANK    TRUE BOLSA BOS GECMEGINE RUGSAT BERYAR
    image=models.ImageField(blank=True, upload_to = 'uploads')  
    def __str__(self):
        return self.title
  
    def image_tag(self):
        return mark_safe('<img src="{}" height="28"/>'.format(self.image.url))
    image_tag.short_description= 'Image'    
from django.db import models
from django.utils.html import mark_safe

# Create your models here.


class Settings(models.Model):
    STATUS = (
        ('True', 'Hawa'),
        ('False','Yok'),
    )
    title = models.CharField(blank=True,max_length=30)
    instagram = models.CharField(blank=True,max_length=30)
    facebook = models.CharField(blank=True,max_length=30)
    imo = models.CharField(blank=True,max_length=30)
    twitter = models.CharField(blank=True,max_length=30)
    aboutus = models.TextField(blank=True,)
    references = models.CharField(blank=True,max_length=30)
    fax = models.CharField(blank=True,max_length=30)
    phone = models.CharField(blank=True,max_length=30)
    address = models.CharField(blank=True,max_length=30)
    company = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    smtpserver = models.CharField(max_length=30)
    smtpemail = models.CharField(blank=True,max_length=30)
    smtppassword = models.CharField(blank=True,max_length=30)
    smtpport = models.CharField(blank=True,max_length=30)
    keywords = models.CharField(blank=True,max_length=255)
    description = models.TextField(blank=True,)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    create_at =  models.DateTimeField(auto_now_add = True)
    update_at =  models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title  

    def image_tag(self):
        return mark_safe('<img src="{}" height="56"/>').format(self.image.url)
    image_tag.short_description= 'Image'
   
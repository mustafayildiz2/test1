from django.db import models
from blog.models import YazilarModel
from django.contrib.auth.models import User


class YorumModel(models.Model):
    yorum = models.TextField()
    olusturma_tarihi=models.DateField(auto_now_add=True)
    guncellenme_tarihi=models.DateField(auto_now=True)
    yazi=models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorum')
    yazan=models.ForeignKey(User, on_delete= models.CASCADE, related_name='yorumlar')

    class Meta:
        db_table = 'yorum'
        verbose_name_plural='Yorumlar'
        verbose_name='Yorum'

    def __str__ (self):
        return self.yazan.username
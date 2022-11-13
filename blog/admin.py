from django.contrib import admin
from blog.models import KategoriModel, YazilarModel, YorumModel


admin.site.register(KategoriModel)


class YazilarAdmin (admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = ('baslik', 'olusturma_tarihi', 'duzenleme_tarihi')

admin.site.register(YazilarModel, YazilarAdmin)

class YorumlarAdmin (admin.ModelAdmin):
    search_fields = ('yazan.username', 'yorum')
    list_display = ('yorum', 'olusturma_tarihi', 'guncellenme_tarihi')

admin.site.register(YorumModel, YorumlarAdmin)
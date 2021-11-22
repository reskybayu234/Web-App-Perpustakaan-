from django.contrib import admin
from .models import Buku
from .models import Kelompok
# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul','penulis','penerbit','jumlah_buku']
    search_fields = ['judul','penulis','penerbit']
    list_filter = ('kelompok_id',)
    list_per_page = 4


admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)
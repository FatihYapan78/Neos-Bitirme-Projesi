from django.contrib import admin
from .models import *


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('title','category_list')
    list_filter = ('title',)
    search_fields = ('title',)
    prepopulated_fields= {"slug":('title',),}
    ordering = ('title',)

    def category_list(self, obj):
        html=''
        for category in obj.categorys.all():
            html += category.category + ' '
        return html
@admin.register(Favori)
class FavoriAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('user',)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('category','card_count')

    def card_count(self, obj):
        return obj.card_set.count()
    
@admin.register(SepetUrun)
class SepetUrunAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('user','toplamFiyat','adet')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('user','card','date_now','star','id')

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):

    list_display = ('user','phone_number','id')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name','email','title','id')

@admin.register(Beden)
class BedenAdmin(admin.ModelAdmin):

    list_display = ('title','id')

@admin.register(EBeden)
class EBedenAdmin(admin.ModelAdmin):

    list_display = ('user','card','price','stok','beden','id')

@admin.register(Numara)
class NumaraAdmin(admin.ModelAdmin):

    list_display = ('title','id')
    
@admin.register(ANumara)
class ANumaraAdmin(admin.ModelAdmin):

    list_display = ('user','card','price','stok','beden','id')



from django.contrib import admin


from .models import Ruler, Material, Nominal, Coin, MD, MCM, Redkost

#admin.site.register(Ruler)
admin.site.register(Material)
admin.site.register(Nominal)
#admin.site.register(Coin)
admin.site.register(MD)
admin.site.register(MCM)
admin.site.register(Redkost)

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ('bitkin', 'nominal', 'year', 'material', 'ruler', 'md', 'mcm', 'nalichie', 'tirazh', 'note', 'redkost',)
    #fields = ['nominal', 'year', ('bitkin')]
    #inlines = [CoinsInline]


@admin.register(Ruler)
class RulerAdmin(admin.ModelAdmin):

    list_display = ('name', 'year_of_rule')
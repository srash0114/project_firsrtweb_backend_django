from django.contrib import admin
from .models import *
# Register your models here.
class thitruongAdmin(admin.ModelAdmin):
    list_display=('id_thitruong', 'id_caytrong', 'ten_caytrong','ten_thitruong','ten_nguoiban','gia')
    search_fields=['ten_caytrong']

admin.site.register(thitruong,thitruongAdmin)
admin.site.register(thitruong_ban)

admin.site.register(Product)
admin.site.register(Season)
admin.site.register(Land)
admin.site.register(Plant)
admin.site.register(Contact)
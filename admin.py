from django.contrib import admin

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper
    
    
  class MyAdmin(admin.ModelAdmin):

    list_filter = (('my_field', custom_titled_filter('My custom title'))

admin.site.register(MyAdminModel, MyAdmin)

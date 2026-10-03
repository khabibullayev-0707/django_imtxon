from django.contrib import admin
from .models import Student, Reja
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('ism','yosh','kurs')
    search_fields=('ism',)
    list_filter=('kurs',)
    list_display_links=('ism',)
@admin.register(Reja)
class RejaAdmin(admin.ModelAdmin):
    list_display=('sarlavha','student','sana','bajarildi')
    search_fields=('sarlavha','student__ism')
    list_filter=('bajarildi',)
    list_display_links=('sarlavha',)
    autocomplete_fields=('student',)

from django.contrib import admin
from people.models import Person

# Register your models here.

class PersonInline(admin.StackedInline):
    model = Person
    extra = 1

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'count_following', 'count_followers']

admin.site.register(Person, PersonAdmin)

from django.contrib import admin
from people.models import Person

# Register your models here.

class FollowingInline(admin.TabularInline):
    model = Person.following.through
    fk_name = 'from_person'


class FollowersInline(admin.TabularInline):
    model = Person.following.through
    fk_name = 'to_person'


class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fields = ('id', 'name',)
    list_display = ('id', 'name', 'count_following', 'count_followers',)
    inlines = (FollowingInline, FollowersInline,)


admin.site.register(Person, PersonAdmin)

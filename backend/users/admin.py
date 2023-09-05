from django.contrib import admin
from users.models import Subscribe, User


class UserAdmin(admin.ModelAdmin):
    """Управление пользователями."""
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
    )
    search_fields = ('username', 'email',)
    list_filter = (
        'first_name',
        'email',
    )
    empty_value_display = '-пусто-'


class SubscribeAdmin(admin.ModelAdmin):
    """Управление подписками."""
    list_display = (
        'id',
        'user',
        'author'
    )
    search_fields = ('user',)


admin.site.register(User, UserAdmin)
admin.site.register(Subscribe, SubscribeAdmin)

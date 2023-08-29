from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientInRecipe, Recipe,
                     ShoppingCart, Tag)


class TagAdmin(admin.ModelAdmin):
    """Управление тегами."""
    list_display = (
        'name',
        'color',
        'slug'
    )
    search_fields = ('name', 'color',)


class IngredientAdmin(admin.ModelAdmin):
    """Управление ингредиентами."""
    list_display = (
        'name',
        'measurement_unit'
    )
    search_fields = ('name',)
    list_filter = ('name',)


class IngredientInline(admin.TabularInline):
    model = IngredientInRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    """Управление рецептами."""
    list_display = (
        'id',
        'name',
        'author',
        'added_in_favorites',
        'pub_date',
    )
    fields = (
        (
            'name',
            'cooking_time',
        ),
        (
            'author',
            "tags",
        ),
        ('text',),
        ('image',),
    )
    search_fields = (
        'name',
        'author__username',
        'tags__name'
    )
    list_filter = ('name', 'author__username', 'tags__name')
    inlines = (IngredientInline,)
    empty_value_display = '-пусто-'
    readonly_fields = ('added_in_favorites',)
    filter_horizontal = ('tags',)

    def added_in_favorites(self, obj):
        return obj.favorites.count()

    added_in_favorites.short_description = 'Количество добавлений в избранное'


class FavoriteAdmin(admin.ModelAdmin):
    """Управление избранными рецептами."""
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user', 'recipe')


class ShoppingCartAdmin(admin.ModelAdmin):
    """Управление рецептами в корзине."""
    list_display = ('recipe', 'user')
    search_fields = ('user', 'recipe')


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)

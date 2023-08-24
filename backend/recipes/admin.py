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
    extra = 2


class RecipeAdmin(admin.ModelAdmin):
    """Управление рецептами."""
    list_display = (
        'name',
        'author',
        'added_in_favorites',
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
        return obj.favorites.all().count()

    added_in_favorites.short_description = 'Количество добавлений в избранное'


class IngredientInRecipeAdmin(admin.ModelAdmin):
    """Управление ингридиентами в рецептах."""
    list_display = (
        'ingredient',
        'amount',
    )
    list_filter = ('ingredient',)


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
admin.site.register(IngredientInRecipe, IngredientInRecipeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)

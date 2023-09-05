from datetime import datetime

from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from recipes.models import IngredientInRecipe


def create_shoping_list(user):
    if not user.shopping_cart.exists():
        return Response(status=HTTP_400_BAD_REQUEST)
    ingredients = IngredientInRecipe.objects.filter(
            recipe__shopping_cart__user=user
    ).values(
            'ingredient__name',
            'ingredient__measurement_unit'
    ).annotate(amount=Sum('amount'))
    today = datetime.today()
    shoping_list = (
        f'Список покупок в "Пятерочку".\n\n'
        f'Дата: {today:%Y-%m-%d}\n\n'
    )
    shoping_list += '\n'.join([
        f'- {ingredient["ingredient__name"]} '
        f'({ingredient["ingredient__measurement_unit"]})'
        f' - {ingredient["amount"]}'
        for ingredient in ingredients
    ])
    shoping_list += f'\n\nFoodgram ({today:%Y})'
    return shoping_list

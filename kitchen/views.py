from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from kitchen.models import Cook, DishType, Dish


@login_required
def index(request):
    """View function for home page of site."""
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()

    context = {
        'num_cooks': num_cooks,
        'num_dish_types': num_dish_types,
        'num_dishes': num_dishes,
    }

    return render(
        request,
        "kitchen/index.html",
        context = context
    )

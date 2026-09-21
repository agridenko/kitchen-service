from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

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
        context=context
    )


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = 'dish_type_list'
    template_name = 'kitchen/dishtype_list.html'
    paginate_by = 5


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    context_object_name = 'dish_list'
    template_name = 'kitchen/dish_list.html'
    paginate_by = 5


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    context_object_name = 'cook_list'
    template_name = 'kitchen/cook_list.html'
    paginate_by = 5

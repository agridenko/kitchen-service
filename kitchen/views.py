from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
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


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy('kitchen:dish_type_list')


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy('kitchen:dish_type_list')


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy('kitchen:dish_type_list')


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    context_object_name = 'dish_list'
    template_name = 'kitchen/dish_list.html'
    paginate_by = 5


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy('kitchen:dish_list')


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy('kitchen:dish_list')


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy('kitchen:dish_list')


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    context_object_name = 'cook_list'
    template_name = 'kitchen/cook_list.html'
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy('kitchen:cook_list')


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy('kitchen:cook_list')


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy('kitchen:cook_list')

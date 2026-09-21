from django.urls import path

from kitchen.views import (index,
                           DishTypeListView,
                           DishListView,
                           DishDetailView,
                           CookListView,
                           DishTypeCreateView)

urlpatterns = [
    path("", index, name="index"),
    path("dish_type/", DishTypeListView.as_view(), name="dish_type_list"),
    path("dish_type/create/", DishTypeCreateView.as_view(), name="dish_type_create"),

    path("dish/", DishListView.as_view(), name="dish_list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path("cook/", CookListView.as_view(), name="cook_list"),
]

app_name = "kitchen"

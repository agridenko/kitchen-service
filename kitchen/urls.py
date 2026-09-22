from django.urls import path

from kitchen.views import (index,
                           DishTypeListView,
                           DishListView,
                           DishDetailView,
                           CookListView,
                           DishTypeCreateView,
                           DishTypeUpdateView,
                           DishTypeDeleteView,
                           DishCreateView,
                           CookDetailView,
                           CookCreateView)

urlpatterns = [
    path("", index, name="index"),
    path("dish_type/", DishTypeListView.as_view(), name="dish_type_list"),
    path(
        "dish_type/create/",
        DishTypeCreateView.as_view(),
        name="dish_type_create"
    ),
    path(
        "dish_type/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_type_update"
    ),
    path(
        "dish_type/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_type_delete"
    ),

    path("dish/", DishListView.as_view(), name="dish_list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish_create"),

    path("cook/", CookListView.as_view(), name="cook_list"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook_detail"),
    path("cook/create/", CookCreateView.as_view(), name="cook_create"),
]

app_name = "kitchen"

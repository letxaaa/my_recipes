from django.urls import path
from . import views


urlpatterns = [
  path('', views.index),
  path('add_recipes', views.add_recipes),
  path('<int:recipe_id>', views.recipe_details),
  path('fav/<int:recipe_id>', views.fav),
  path('un_favorite/<int:recipe_id>', views.un_favorite),
  path('update_recipe/<int:recipe_id>', views.update_recipe),
  path('delete_recipe/<int:recipe_id>', views.delete_recipe)
]
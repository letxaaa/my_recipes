from django.shortcuts import render, redirect
from login.models import User
from recipes.models import Recipe
from django.contrib import messages

# Create your books views here.
def index(request):
  context = {
    'users': User.objects.all(),
    'recipes': Recipe.objects.all(),
    'current_user': User.objects.get(id=request.session['user_id'])
  }
  if 'user_id' not in request.session:
    return redirect('/')
  else:

    return render(request, 'recipes/index.html', context)
    
#add new recipe
def add_recipes(request):
  errors = User.objects.validate_recipes(request.POST)
  recipe_uploader = User.objects.get(id=request.session['user_id'])

  if errors:
    for value in errors.values():
      messages.error(request, value)
    return redirect('/recipes')

  else:
    new_recipe = Recipe.objects.create(title = request.POST['title'],
    description = request.POST['des'],
    ingredients = request.POST['In'],
    instructions = request.POST['instruc'],
    servings = request.POST['ser'],
    prep_time = request.POST['prep'],
    cook_time = request.POST['cook'],
    uploader = recipe_uploader,
    )
    likers = recipe_uploader.liked_recipes.add(new_recipe)
    return redirect('/recipes')
  
#recipe details
def recipe_details(request, recipe_id):
  current_recipe = Recipe.objects.get(id=recipe_id)
  context = {
    'cur_recipe': current_recipe
  }
  if 'user_id' not in request.session:
      return redirect('/')
  else:
      return render(request, 'recipes/recipe.html', context)

def fav(request, recipe_id):
  fav_recipe = Recipe.objects.get(id=recipe_id)
  who_fav = User.objects.get(id=request.session['user_id'])
  who_fav.liked_recipes.add(fav_recipe)
  return redirect('/recipes')

def un_favorite(request, recipe_id):
  dislike_recipe = Recipe.objects.get(id=recipe_id)
  user_disliking = User.objects.get(id=request.session['user_id'])
  user_disliking.liked_recipes.remove(dislike_recipe)
  return redirect('/recipes')

def update_recipe(request, recipe_id):
  recipe_to_update = Recipe.objects.get(id=recipe_id)
  errors = User.objects.validate_recipes(request.POST)

  if len(errors) >0:
    for values in errors.values():
      messages.error(request, values)
    return redirect(f'/recipes/{recipe_to_update.id}')
  else:
    recipe_to_update.title = request.POST['title']
    recipe_to_update.description = request.POST['des']
    recipe_to_update.ingredients = request.POST['In']
    recipe_to_update.instructions = requets.POST['instruc']
    recipe_to_update.servings = request.POST['ser']
    recipe_to_update.prep_time = request.POST['prep']
    recipe_to_update.cook_time = request.POST['cook']
    recipe_to_update.save()
    return redirect('/recipes')
  
def delete_recipe(request, recipe_id):
  recipe_to_destroy = Recipe.objects.get(id=recipe_id)
  if recipe_to_destroy.uploader.id == request.session['user_id']:
    recipe_to_destroy.delete()
    return redirect('/recipes')
  else:
    return redirect('/')
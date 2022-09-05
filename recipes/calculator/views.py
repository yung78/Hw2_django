from django.http import HttpResponse
from django.shortcuts import render, reverse



DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'sandwich': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

# Add 'home' from 1st homework
def home_view(request):
    template_name = 'home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Ингредиенты омлет ': reverse('omlet'),
        'Ингредиенты паста ': reverse('pasta'),
        'Ингредиенты бутерброд ': reverse('sandwich')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def omlet_view(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'яйца, шт': 2*servings,
            'молоко, л': 0.1*servings,
            'соль, ч.л.': 0.5*servings,
        }
    }
    return render(request, template_name, context)


def pasta_view(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'макароны, г': 0.3*servings,
            'сыр, г': 0.05*servings,
        }

    }
    return render(request, template_name, context)


def sandwich_view(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'хлеб, ломтик': 1*servings,
            'колбаса, ломтик': 1*servings,
            'сыр, ломтик': 1*servings,
            'помидор, ломтик': 1*servings,
        }

    }
    return render(request, template_name, context)

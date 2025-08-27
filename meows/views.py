from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import MeowForm, CustomUserCreationForm
from .models import Meow

# Home (landing page) mostrando todos los maullidos
def home_view(request):
    meows = Meow.objects.all().select_related('author').order_by('-created_at')
    context = {'meows': meows}

    # Mensajes de bienvenida central
    if 'welcome_message' not in context and request.user.is_authenticated:
        context['welcome_message'] = f"Bienvenido, {request.user.username} 🐱"

    # Usuarios conectados para la columna lateral (excepto el actual)
    if request.user.is_authenticated:
        online_users = User.objects.filter(is_active=True).exclude(id=request.user.id)
        context['online_users'] = online_users

    return render(request, 'home.html', context)


# Registro
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


# Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Credenciales inválidas. Intenta de nuevo.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# Logout
def logout_view(request):
    logout(request)
    # Redirigir a plantilla de logout específica
    return render(request, 'logout.html')


# Perfil de usuario
def profile_view(request, username):
    try:
        profile_user = User.objects.get(username=username)
    except User.DoesNotExist:
        return render(request, 'profile.html', {
            'not_found': True,
            'username': username
        })

    meows = (
        Meow.objects
        .filter(author=profile_user)
        .select_related('author')
        .order_by("-created_at")
    )

    # Permitir crear maullidos solo si es su propio perfil
    if request.user.is_authenticated and request.user == profile_user:
        if request.method == 'POST':
            form = MeowForm(request.POST)
            if form.is_valid():
                meow = form.save(commit=False)
                meow.author = request.user
                meow.save()
                messages.success(request, "Tu maullido fue publicado.")
                return redirect('profile', username=username)
        else:
            form = MeowForm()
    else:
        form = None

    return render(request, 'profile.html', {
        'not_found': False,
        'profile_user': profile_user,
        'meows': meows,
        'form': form,
    })


# Búsqueda de usuarios
def user_search_view(request):
    query = request.GET.get('q', '')
    users = User.objects.filter(username__icontains=query)
    return render(request, 'user_search.html', {'query': query, 'users': users})

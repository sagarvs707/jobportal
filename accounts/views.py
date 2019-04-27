from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.shortcuts import render
from django.http import JsonResponse
from.forms import LoginForm, RegisterForm

@csrf_exempt
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = '/login/'

def Home_view(request):
    return render(request, "home.html")
    # if request.method == 'POST':


"""This is custom login view pleas dont delete it"""

@csrf_exempt
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "from": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'code':'200', 'message':'log in successfully'})
        else:
            return JsonResponse({'status': 'fail', 'code':'401', 'message':'Invalid email id and password'})
    return render(request, "login.html", context)



""" This custom registration view
don't delete"""
# User = get_user_model()
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         "form":form
#     }
#     if form.is_valid():
#         form.save()
#     return render(request, "accounts/register.html", context)
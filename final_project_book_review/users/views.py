from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("users:login")

    context = {
        "form": form
    }
    return render(request, "authentication/register.html", context)


class CustomLoginView(LoginView):
    template_name="authentication/login.html"

    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully.")
        return super().form_valid(form)
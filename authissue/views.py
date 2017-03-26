# coding:utf-8
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView


class AuthView(FormView):
    """
    """
    template_name = "auth/auth.html"
    form_class = AuthenticationForm

    def form_valid(self, form):
        """
        """
        user = form.get_user()
        if not user or not user.is_active:
            return redirect("/")

        login(self.request, user)
        return redirect("index")

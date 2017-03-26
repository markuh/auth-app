# coding:utf-8
from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import FormView

from authissue.forms import AuthForm


class AuthView(FormView):
    """
    """
    template_name = "auth/auth.html"
    form_class = AuthForm

    def form_valid(self, form):
        """
        """
        user = form.get_user()
        if not user or not user.is_active:
            return redirect("/")

        login(self.request, user)
        return redirect("index")

from django.views.generic import ListView, CreateView, DetailView
from .models import Bio, ContactInfo, CV, SocialLink, Project
from django import forms
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import Socials_Create
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()

class StartPageView(ListView):
    template_name = "portfolio/index.html"
    model = Bio

class Bio_Create(CreateView):
    template_name = "portfolio/bio_create.html"
    model = Bio
    fields = ['first_name', 'last_name', 'about_me', 'profile_picture']
    success_url = reverse_lazy(
        "create_socials"
    )  # Redirect to profile page or any appropriate URL

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Socials_Create(FormView):
    template_name = "portfolio/socials_create.html"
    form_class = Socials_Create
    success_url = reverse_lazy("profile")  # Redirect to an appropriate page

    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)


class ProfileView(DetailView):
    model = User
    template_name = "portfolio/profile.html"
    context_object_name = "user_profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()

        # Retrieve related models
        context["bio"] = Bio.objects.get(user=user)

        try:
            context["contact_info"] = ContactInfo.objects.get(user=user)
        except ContactInfo.DoesNotExist:
            context["contact_info"] = None

        try:
            context["social_links"] = SocialLink.objects.get(user=user)
        except SocialLink.DoesNotExist:
            context["social_links"] = None

        try:
            context["cv"] = CV.objects.get(user=user)
        except CV.DoesNotExist:
            context["cv"] = None
        
        try:
            context["projects"] = Project.objects.filter(user=user)
        except Project.DoesNotExist:
            context["projects"] = None
        return context

from django.forms import BaseModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Bio, ContactInfo, CV, SocialLink, Project, Stack, Services, work_exp
from django.urls import reverse, reverse_lazy
from .forms import (
    Socials_Create,
    UpdateProfileForm,
    StackForm,
    ServiceForm,
    SocialLinkForm,
    ContactInfoForm,
    SocialLinkFormSet,
    WorkexpForm,
)
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


User = get_user_model()


class StartPageView(ListView):
    template_name = "portfolio/index.html"
    model = Bio


class Bio_Create(CreateView):
    template_name = "portfolio/bio_create.html"
    model = Bio
    fields = ["first_name", "last_name", "about_me", "profile_picture"]
    success_url = reverse_lazy(
        "create_socials"
    )  # Redirect to profile page or any appropriate URL

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Socials_Create(FormView):
    template_name = "portfolio/socials_create.html"
    form_class = Socials_Create

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)


class StackCreateView(FormView):
    template_name = "portfolio/stack.html"
    form_class = StackForm
    # Redirect to the profile page after successful form submission

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)


class ServiceCreateView(FormView):
    template_name = "portfolio/service.html"
    form_class = ServiceForm
    # Redirect to the profile page after successful form submission

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)


class AddSocialLinkView(CreateView):
    model = SocialLink
    form_class = SocialLinkForm
    template_name = "portfolio/socials_create.html"

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        social_link = form.save(commit=False)
        social_link.user = self.request.user
        social_link.save()
        return super().form_valid(form)

class AddWorkExp(CreateView):
    model = work_exp
    template_name = "portfolio/work_exp.html"
    form_class = WorkexpForm

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectUpload(CreateView):
    model = Project
    template_name = "portfolio/projectupload.html"
    fields = ["name", "description", "link", "project_picture"]

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateProfile(UpdateView):
    model = Bio
    form_class = UpdateProfileForm
    template_name = "portfolio/profile_update.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class CvUpload(UpdateView):
    model = CV
    template_name = "portfolio/cvupload.html"
    fields = ["file"]

    def get_object(self, queryset=None):
        obj, created = CV.objects.get_or_create(user=self.request.user)
        return obj

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectEdit(UpdateView):
    model = Project
    template_name = "portfolio/projectedit.html"
    fields = ["name", "description", "link", "project_picture"]

    def get_object(self, queryset=None):
        # Ensure that we get the project for the current user
        return Project.objects.get(pk=self.kwargs["pk"], user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ServiceUpdate(UpdateView):
    model = Services
    template_name = "portfolio/service_edit.html"
    fields = ["name", "description"]

    def get_object(self, queryset=None):
        return Services.objects.get(pk=self.kwargs["pk"], user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        return super().form_valid(form)

class StackUpdate(UpdateView):
    model = Stack
    template_name = "portfolio/stack_edit.html"
    fields = ["name", "mastery_level", "experience_years"]

    def get_object(self, queryset=None):
        return Stack.objects.get(pk=self.kwargs["pk"], user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        return super().form_valid(form)


class UpdateWorkExp(UpdateView):
    model = work_exp
    template_name = "portfolio/work_exp_edit.html"
    fields = ["Company", "work_done", "start_date", "end_date"]

    def get_object(self, queryset=None):
        return work_exp.objects.get(pk=self.kwargs["pk"], user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
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

        context["social_links"] = SocialLink.objects.filter(user=user)

        try:
            context["cv"] = CV.objects.get(user=user)
        except CV.DoesNotExist:
            context["cv"] = None

        context["stacks"] = Stack.objects.filter(user=user)
        context["services"] = Services.objects.filter(user=user)
        context["work_exps"] = work_exp.objects.filter(user=user)
        context["projects"] = Project.objects.filter(user=user)

        return context


class PortfolioView(DetailView):
    model = User
    template_name = "portview/index.html"
    context_object_name = "user_index"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()

        # Retrieve related models
        context["bio"] = Bio.objects.get(user=user)

        try:
            context["contact_info"] = ContactInfo.objects.get(user=user)
        except ContactInfo.DoesNotExist:
            context["contact_info"] = None

        context["social_links"] = SocialLink.objects.filter(user=user)
        try:
            context["cv"] = CV.objects.get(user=user)
        except CV.DoesNotExist:
            context["cv"] = None

        context["stacks"] = Stack.objects.filter(user=user)
        context["services"] = Services.objects.filter(user=user)
        context["projects"] = Project.objects.filter(user=user)
        context["work_exps"] = work_exp.objects.filter(user=user)

        # Add the icons list to the context
        context["icons"] = [
            "bi-briefcase",
            "bi-card-checklist",
            "bi-bar-chart",
            "bi-binoculars",
            "bi-calendar-check",
        ]

        return context

def ContactInfoUpdate(request):
    user = request.user

    # Get or create the user's contact info
    contact_info, created = ContactInfo.objects.get_or_create(user=user)

    if request.method == "POST":
        contact_form = ContactInfoForm(request.POST, instance=contact_info)
        social_link_formset = SocialLinkFormSet(
            request.POST, queryset=SocialLink.objects.filter(user=user)
        )

        if contact_form.is_valid() and social_link_formset.is_valid():
            contact_form.save()
            social_links = social_link_formset.save(commit=False)
            for social_link in social_links:
                social_link.user = user
                social_link.save()
            # Delete any removed social links
            for social_link in social_link_formset.deleted_objects:
                social_link.delete()
            return redirect("profile", pk=user.pk)
    else:
        contact_form = ContactInfoForm(instance=contact_info)
        social_link_formset = SocialLinkFormSet(
            queryset=SocialLink.objects.filter(user=user)
        )

    return render(
        request,
        "portfolio/contact_info_update.html",
        {
            "contact_form": contact_form,
            "social_link_formset": social_link_formset,
        },
    )

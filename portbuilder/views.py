from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Bio, ContactInfo, CV, SocialLink, Project
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import Socials_Create, UpdateForm
from django.contrib.auth import get_user_model

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


class Socials_Create(CreateView):
    template_name = "portfolio/socials_create.html"
    form_class = Socials_Create

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.request.user.pk})

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


class UpdateProfile(UpdateView):
    model = Bio
    form_class = UpdateForm
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


class CvUpload(UpdateView):
    model = CV
    template_name = "portfolio/cvupload.html"
    fields = ["file"]  # Assuming you only want to upload the CV file

    def get_object(self, queryset=None):
        # Get the CV object for the current user, or create a new one if it doesn't exist
        obj, created = CV.objects.get_or_create(user=self.request.user)
        return obj

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpload(CreateView):
    model = Project
    template_name = "portfolio/projectupload.html"
    fields = ["name", "description", "link"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})

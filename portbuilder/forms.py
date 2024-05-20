from django import forms
from .models import ContactInfo, SocialLink, Bio, CV


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ["email", "phone_number", "address"]


class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ["linkedin", "github", "twitter"]


class Socials_Create(forms.Form):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=255, required=False)
    linkedin = forms.URLField(required=False)
    github = forms.URLField(required=False)
    twitter = forms.URLField(required=False)

    def save(self, user):
        contact_info, created = ContactInfo.objects.update_or_create(
            user=user,
            defaults={
                "email": self.cleaned_data["email"],
                "phone_number": self.cleaned_data["phone_number"],
                "address": self.cleaned_data["address"],
            },
        )

        social_link, created = SocialLink.objects.update_or_create(
            user=user,
            defaults={
                "linkedin": self.cleaned_data["linkedin"],
                "github": self.cleaned_data["github"],
                "twitter": self.cleaned_data["twitter"],
            },
        )

        return contact_info, social_link


class UpdateForm(forms.ModelForm):
    linkedin = forms.URLField(required=False)
    github = forms.URLField(required=False)
    twitter = forms.URLField(required=False)

    class Meta:
        model = Bio
        fields = ["first_name", "last_name", "about_me", "profile_picture"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if self.user:
            social_link, created = SocialLink.objects.get_or_create(user=self.user)
            self.fields["linkedin"].initial = social_link.linkedin
            self.fields["github"].initial = social_link.github
            self.fields["twitter"].initial = social_link.twitter

    def save(self, commit=True):
        bio = super().save(commit=False)
        if commit:
            bio.save()
        social_link, created = SocialLink.objects.get_or_create(user=self.user)
        social_link.linkedin = self.cleaned_data["linkedin"]
        social_link.github = self.cleaned_data["github"]
        social_link.twitter = self.cleaned_data["twitter"]
        social_link.save()
        return bio

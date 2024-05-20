from django import forms
from .models import ContactInfo, SocialLink


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

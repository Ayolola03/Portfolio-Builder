from django import forms
from .models import ContactInfo, SocialLink, Bio, CV


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ["email", "phone_number", "address"]


class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ["url1", "url2", "url3"]


class Socials_Create(forms.Form):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=255, required=False)
    url1 = forms.URLField(required=False)
    url2 = forms.URLField(required=False)
    url3 = forms.URLField(required=False)

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
                "url1": self.cleaned_data["url1"],
                "url2": self.cleaned_data["url2"],
                "url3": self.cleaned_data["url3"],
            },
        )

        return contact_info, social_link


class UpdateForm(forms.ModelForm):
    url1 = forms.URLField(required=False)
    url2 = forms.URLField(required=False)
    url3 = forms.URLField(required=False)

    class Meta:
        model = Bio
        fields = ["first_name", "last_name", "about_me", "profile_picture"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if self.user:
            social_link, created = SocialLink.objects.get_or_create(user=self.user)
            self.fields["url1"].initial = social_link.url1
            self.fields["url2"].initial = social_link.url2
            self.fields["url3"].initial = social_link.url3

    def save(self, commit=True):
        bio = super().save(commit=False)
        if commit:
            bio.save()
        social_link, created = SocialLink.objects.get_or_create(user=self.user)
        social_link.url1 = self.cleaned_data["url1"]
        social_link.url2 = self.cleaned_data["url2"]
        social_link.url3 = self.cleaned_data["url3"]
        social_link.save()
        return bio

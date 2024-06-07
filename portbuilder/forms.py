from django import forms
from .models import ContactInfo, SocialLink, Bio, CV, Services, Stack
from django.forms import modelformset_factory


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ["email", "phone_number", "address"]


class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ["platform", "url"]


class Socials_Create(forms.Form):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=255, required=False)
    platform1 = forms.ChoiceField(choices=SocialLink.PLATFORM_CHOICES, required=False)
    url1 = forms.URLField(required=False)
    platform2 = forms.ChoiceField(choices=SocialLink.PLATFORM_CHOICES, required=False)
    url2 = forms.URLField(required=False)
    platform3 = forms.ChoiceField(choices=SocialLink.PLATFORM_CHOICES, required=False)
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

        # Delete old links
        SocialLink.objects.filter(user=user).delete()

        # Create new links
        for i in range(1, 4):
            platform = self.cleaned_data.get(f"platform{i}")
            url = self.cleaned_data.get(f"url{i}")
            if platform and url:
                SocialLink.objects.create(user=user, platform=platform, url=url)

        return contact_info, SocialLink.objects.filter(user=user)


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Bio
        fields = [
            "profile_picture",
            "first_name",
            "last_name",
            "about_me",
            "role",
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)


class StackForm(forms.Form):
    # Fields for Stack
    stack_name = forms.CharField(max_length=100, label="Stack Name")
    mastery_level = forms.ChoiceField(
        choices=Stack.MASTERY_CHOICES, label="Mastery Level"
    )
    experience_years = forms.IntegerField(label="Years of Experience")
    
    def save(self, user):
        # Save Stack data
        stack, created = Stack.objects.update_or_create(
            user=user,
            name=self.cleaned_data["stack_name"],
            defaults={
                "mastery_level": self.cleaned_data["mastery_level"],
                "experience_years": self.cleaned_data["experience_years"],
            },
        )

        
        return stack

class ServiceForm(forms.Form):
    # Fields for Service
    service_name = forms.CharField(max_length=100, label="Service Name")
    service_description = forms.CharField(
        widget=forms.Textarea, label="Service Description", required=False
    )

    def save(self, user):
        # Save Service data
        service, created = Services.objects.update_or_create(
            user=user,
            name=self.cleaned_data["service_name"],
            defaults={
                "description": self.cleaned_data["service_description"],
            },
        )

        return service

SocialLinkFormSet = modelformset_factory(SocialLink, form=SocialLinkForm, extra=1)

# Portbuilder urls.py
from django.urls import path, include

from .views import StartPageView, Bio_Create, Socials_Create, ProfileView, UpdateProfile, CvUpload, ProjectUpload, PortfolioView, StackCreateView, ServiceCreateView, ProjectEdit, AddSocialLinkView, ContactInfoUpdate, ServiceUpdate, StackUpdate, UpdateWorkExp, AddWorkExp

urlpatterns = [
    # PortfolioBuilder
    path("", StartPageView.as_view(), name="index"),
    path("create/bio", Bio_Create.as_view(), name="create_bio"),
    path("create/socials", Socials_Create.as_view(), name="create_socials"),
    path("stacks/", StackCreateView.as_view(), name="stacks"),
    path("stacks/update/<int:pk>", StackUpdate.as_view(), name="update_stacks"),
    path("services/", ServiceCreateView.as_view(), name="services"),
    path("services/update/<int:pk>", ServiceUpdate.as_view(), name="update_services"),
    path("working_exp/", AddWorkExp.as_view(), name="working_exp_create"),
    path("working_exp/update/<int:pk>", UpdateWorkExp.as_view(), name="update_working_exp"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path("profile/update/<int:pk>/", UpdateProfile.as_view(), name="profile_update"),
    path("cv/upload/", CvUpload.as_view(), name="cvupload"),
    path("project/upload/", ProjectUpload.as_view(), name="projectupload"),
    path("project/edit/<int:pk>", ProjectEdit.as_view(), name="projectedit"),
    path("profile/socials/", AddSocialLinkView.as_view(), name="update_socials"),
    path("profile/contact_info/update/", ContactInfoUpdate, name="update_contact_info"),
    # PortfolioView
    path("portfolio/<int:pk>", PortfolioView.as_view(), name="port_index"),
]

# Portbuilder urls.py
from django.urls import path, include

from .views import StartPageView, Bio_Create, Socials_Create, ProfileView, UpdateProfile, CvUpload, ProjectUpload, PortfolioView, StackCreateView, ServiceCreateView, ProjectEdit

urlpatterns = [
    #PortfolioBuilder
    path("", StartPageView.as_view(), name="index"),
    path("create/bio", Bio_Create.as_view(), name="create_bio"),
    path("create/socials", Socials_Create.as_view(), name="create_socials"),
    path("stacks/", StackCreateView.as_view(), name="stacks"),
    path("services/", ServiceCreateView.as_view(), name="services"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path("profile/update/<int:pk>/", UpdateProfile.as_view(), name="profile_update"),
    path("cv/upload/", CvUpload.as_view(), name="cvupload"),
    path("project/upload/", ProjectUpload.as_view(), name="projectupload"),
    path("project/edit/<int:pk>", ProjectEdit.as_view(), name="projectedit"),


    #PortfolioView
    path("portfolio/<int:pk>", PortfolioView.as_view(), name="port_index"),
]

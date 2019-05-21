# from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart import views
from rest_framework.urlpatterns import format_suffix_patterns
# router = routers.DefaultRouter()
# router.register(r"users", views.UserViewSet)
# router.register(r"groups", views.GroupViewSet)


urlpatterns = [
    path("snippets/", views.snippet_list),
    path("snippets/<int:pk>", views.snippet_detail),
    # path('', include(router.urls)),
    # path("api-auth/", include("rest_framework.urls"), name="rest_framework")
]

urlpatterns = format_suffix_patterns(urlpatterns)
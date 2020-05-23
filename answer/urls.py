from django.urls import path

from answer import views

urlpatterns = [
    path("", views.AnsView.as_view()),
    path("<int:pk>/", views.AnsView.as_view())
]
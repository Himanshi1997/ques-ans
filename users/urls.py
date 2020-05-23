from django.urls import path

from users import views

urlpatterns = [
    path("", views.UserView.as_view()),
    path("<int:pk>/", views.UserView.as_view())

]
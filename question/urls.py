from django.urls import path

from question import views

urlpatterns = [
    path("", views.QuesView.as_view()),
    path("<int:pk>/", views.QuesView.as_view())

]






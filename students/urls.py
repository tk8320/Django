
from django.urls import path
from .views import StudentCreateListView,StudentDetailedView

urlpatterns = [
    path('', StudentCreateListView.as_view()),
    path('<int:pk>/', StudentDetailedView.as_view())

]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CustomersList, CustomerDetails, CustomerGroupsList, CustomerGroupDetails


urlpatterns = [
    path("customers/", CustomersList.as_view()),
    path("customers/<int:pk>", CustomerDetails.as_view()),
    path("customers/groups/", CustomerGroupsList.as_view()),
    path("customers/groups/<int:pk>", CustomerGroupDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)

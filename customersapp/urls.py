from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customersapp.views import CustomerList, CustomerDetail, CustomerGroupList, CustomerGroupDetail


urlpatterns = [
    path("customers/", CustomerList.as_view()),
    path("customers/<int:pk>", CustomerDetail.as_view()),
    path("customers/groups/", CustomerGroupList.as_view()),
    path("customers/groups/<int:pk>", CustomerGroupDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)

from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('risktypes/', views.RiskTypeList.as_view()),
    path('risktype/<str:code>/',views.RiskTypeItem.as_view()),
    path('',views.index)
]
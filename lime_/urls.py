from django.urls import path
from django.urls import reverse


from . import views
# from lime_.views import 

urlpatterns = [
    path('upload', views.model_form_upload, name='upload'),
    path('feature', views.feature_form, name='feature'),
    path('classname', views.class_name_form, name='classname'),
    path('parameter', views.parameter_form, name='parameter'),
    # path('result', views.result_display, name='result'),
]
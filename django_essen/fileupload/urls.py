from django.urls import path
from fileupload.views import RegularFileUploadView


urlpatterns = [
    path('uploads/',RegularFileUploadView.as_view(),name= "product_upload")
]
from django.urls import path
from fileupload.views import RegularFileUploadView,FileListView

urlpatterns = [
    path('', FileListView.as_view(), name="product_list"),
    path('upload/', RegularFileUploadView.as_view(), name="product_upload")
]                   
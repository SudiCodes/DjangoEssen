from django.shortcuts import render
from django.views.generic.edit import FormView
from fileupload.forms import RegularFileForm
from fileupload.models import RegularFile
from django.urls import reverse_lazy

# Create your views here.
class RegularFileUploadView(FormView):
    template_name = "product/index.html"
    success_url = "...."
    form_class = RegularFileForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request,self.template_name,{"form":form})
    
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(
            data=request.POST,
            files= request.FILES
        )
        
        if form.is_valid():
            form.save()
    
        return render(request,self.template_name,{"form":form})
from django.shortcuts import render
from django.views.generic.edit import FormView
from fileupload.forms import RegularFileForm
from fileupload.models import RegularFile
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView

# Create your views here.

class FileListView(ListView):
    template_name="product/list.html"
    model = RegularFile
    paginate_by=100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

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
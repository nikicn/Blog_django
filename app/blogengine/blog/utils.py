from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from .models import *



class DetailObjectMixin:
    model = None
    template = None

    def get(self, request, slug):
        # obj = Post.objects.get(slug__iexact=slug)
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj,'admin_object': obj}) 

# """ class PostDetail(View): """

class CreateObjectMixin:
    model = None
    template = None
    
    def get(self, request):
        form = self.model
        return render(request, self.template, context={'form': form})
 
    def post(self, request):
        bound_form = self.model(request.POST)   
        
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        
        return render(request, self.template, context={'form': bound_form})
    
class UdateObjectMixin:
    model = None
    template = None
    form_class = None    
    
    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_class(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_class(request.POST, instance=obj)
        
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})
    
    
class DeleteObjectMixin:
    model = None
    template = None
    redirect_url = None
    
    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
    
    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
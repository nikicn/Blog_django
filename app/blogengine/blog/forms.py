from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Post

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }
    
  
    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()
        if new_slug == 'created':
            raise ValidationError('Slug my not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug should be UNIQUE. We have "{new_slug}" already')
        return new_slug
        
    
    # def save(self):
    #     new_tag = Tag.objects.create(
    #         title = self.cleaned_data.get('title'),
    #         slug = self.cleaned_data.get('slug')
    #     )
    #     return new_tag
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
        
    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()
        if new_slug == 'created':
            raise ValidationError('Slug my not be "create"')
        return new_slug

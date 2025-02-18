from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
import random

from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 10, 'placeholder': "Enter content here"}
    ), label="Content")

class EditPageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 10, 'placeholder': "Enter content here"}
    ), label="Content")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    
    if content is None:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })
    
def search(request):
    query = request.GET.get('q')
    
    if query in util.list_entries():
        return HttpResponseRedirect(reverse('entry', args=[query]))
    else:
        entries = []
        for entry in util.list_entries():
            if query in entry:
                entries.append(entry)
        return render(request, "encyclopedia/search_result.html", {
            "entries": entries
        })

def new_page(request):
    
    if (request.method == "POST"):
        
        form = NewPageForm(request.POST)
        
        if (form.is_valid()):
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            
            if (title in util.list_entries()):
                return render(request, "encyclopedia/new_page.html", {
                    "form": form,
                    "error": "Page already exists"
                })
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse('entry', args=[title]))
        else:
            return render(request, "encyclopedia/new_page.html", {
                "form": form}
            )
    else:
        return render(request, "encyclopedia/new_page.html", {
        "form": NewPageForm()
        })
        
def edit(request, title):
    
    if (request.method == "POST"):
        
        form = EditPageForm(request.POST)
        
        if (form.is_valid()):
            
            content = form.cleaned_data["content"]
            
            util.save_entry(title, content)
            
            return HttpResponseRedirect(reverse('entry', args=[title]))
        else:
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "form": EditPageForm(initial={'content': content})
            })
    
    else:
           
        content = util.get_entry(title)
        
        form = EditPageForm(initial={'content': content})
        
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "form": form
        })

def random(request):
    entries = util.list_entries()
    
    import random
    
    randomized_number = random.randint(0, len(entries) - 1)
    
    return HttpResponseRedirect(reverse('entry', args=[entries[randomized_number]]) )
    
    
    
    
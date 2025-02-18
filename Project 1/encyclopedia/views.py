from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util


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
    
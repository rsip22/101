from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    item = Item()
    item.text = request.POST.get('item_text', '')
    # Is saving blank items for every request
    item.save()
    return render(request, 'home.html', {
        'new_item_text': item.text
    })

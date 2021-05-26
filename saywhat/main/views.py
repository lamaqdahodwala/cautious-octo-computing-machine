from django.shortcuts import render
from .forms import PostModelForm
# Create your views here.
def index(req):
    return render(req, 'index.html')

def new_post(req):
    if req.method == 'POST':
        ...
    else:
        form = PostModelForm(instance=req.user)
        return render(req, 'newpost.html')
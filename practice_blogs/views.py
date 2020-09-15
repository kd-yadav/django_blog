from django.shortcuts import render, redirect
from .models import Title, Text
from .forms import TitleForm, TextForm

# Create your views here.
def index(request):
    return render(request, 'practice_blogs/index.html', {})

def titles(request):
    titles = Title.objects.order_by('date_added')
    context = {'titles':titles}
    return render(request, 'practice_blogs/titles.html', context)

def title(request, title_id):
    title = Title.objects.get(id=title_id)
    texts = title.text_set.order_by('-date_added')
    context = {'title':title, 'texts':texts}
    return render(request, 'practice_blogs/title.html', context)

def new_title(request):
    if request.method != 'POST':
        form = TitleForm()

    else:
        form = TitleForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('practice_blogs:titles')

    context = {'form':form}
    return render(request, 'practice_blogs/new_title.html', context)

def new_text(request, title_id):
    title = Title.objects.get(id=title_id)

    if request.method != 'POST':
        form = TextForm()

    else:
        form = TextForm(data = request.POST )
        if form.is_valid():
            new_text = form.save(commit = False)
            new_text.title = title
            new_text.save()
            return redirect('practice_blogs:title', title_id=title_id)

    context = {'title':title, 'form':form}
    return render(request, 'practice_blogs/new_text.html', context)

def edit_text(request, tx_id):
    desc = Text.objects.get(id=tx_id)
    title = desc.title   

    if request.method != 'POST':
        form = TextForm(instance = desc)

    else:
        form = TextForm(instance = desc, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('practice_blogs:title', title_id = title.id)

    context = {'title':title, 'desc':desc, 'form':form}
    return render(request, 'practice_blogs/edit_text.html', context)



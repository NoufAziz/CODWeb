from core.models import Subject, Category
from django.shortcuts import render, get_object_or_404

def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'index.html', context)

def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, category, 'show_category.html', context)

def show_subject(request, pk):
    subjects = get_object_or_404(Subject, pk=pk)
    context = {'subject': Subject}
    return render(request, 'show_subject.html', context)
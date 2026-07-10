from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm

def index(request):
    
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
    
    data = {
        'categories' : Category.objects.all(),
        'books' : Book.objects.all(),
        'form_book' : BookForm(),
        'form_category' : CategoryForm(),
        'all_books' : Book.objects.filter(active=True).count(),
        'sold_books' : Book.objects.filter(status='sold').count(),
        'available_books' : Book.objects.filter(status='available').count(),
        'rental_books' : Book.objects.filter(status='rental').count(),
    }

    return render(request, 'pages/index.html', data)

#----------------------------------------------------

def books(request):
    
    search = Book.objects.all()
    title = None

    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)


    if request.method == 'POST':
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
    
    data = {
        'categories' : Category.objects.all(),
        'books' : search,
        'form_category' : CategoryForm(),
    }
    
    return render(request, 'pages/books.html',data)

#----------------------------------------------------

def update(request, id):
    book_id = Book.objects.get(id=id)

    if request.method == 'POST':
        edit_form = BookForm(request.POST, request.FILES, instance=book_id)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/')
    else:
        edit_form = BookForm(instance=book_id)

    context = {
        'editForm': edit_form,
    }

    return render(request, 'pages/update.html', context)

#--------------------------------------------

def delete(request, id):
    delete_book = get_object_or_404(Book, id=id)   # طريقة اخرى لجلب رقم العنصر

    if request.method == 'POST':
        delete_book.delete()
        return redirect('/')

    return render(request, 'pages/delete.html')


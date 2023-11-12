from django.shortcuts import render , redirect
from .models import *
from .forms import *
# Create your views here.

#---------------------Global Context--------------------------
context = {
    'category': Category.objects.all(),
    'Books': Book.objects.all(),
    'form':BookForm(),
    'categoryForm': CategoryForm(),

    'allBooks': Book.objects.filter(active = True).count(),
    'allBooksSold': Book.objects.filter(status = 'sold').count(),
    'allBooksRented': Book.objects.filter(status = 'rented').count(),
    'allBooksAvailable': Book.objects.filter(status = 'available').count(),
}
#---------------------Global Context--------------------------




def index_page(request):
    if request.method == 'POST':
        book_data = BookForm(request.POST, request.FILES)
        if book_data.is_valid():
            book_data.save()

        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()



    return render(request , 'pages/index.html', context)








def books_page(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)


    context = {
        'Books': search,
        'category': Category.objects.all(),
        'categoryForm': CategoryForm(),
    }


    return render(request, 'pages/books.html', context)











def update_page(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'GET':
        book_form_save = BookForm(instance=book_id)
    else:
        book_form_save = BookForm(request.POST , request.FILES , instance=book_id)
        if book_form_save.is_valid():
            book_form_save.save()
            return redirect('/')



    context = {
        'form_update': book_form_save
    }
    return render(request, 'pages/update.html', context)















def delete_book(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')

    return render(request, 'pages/delete.html')
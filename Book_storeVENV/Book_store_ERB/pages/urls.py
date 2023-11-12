from django.urls import path
from . import views


app_name = 'pages'  # add the app_name when you use the {% url 'pages:pattern_name' %} tag
urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('books', views.books_page, name='books_page'),
    path('/update/<int:id>', views.update_page, name='update_page'),
    path('/delete/<int:id>', views.delete_book, name='delete_book')
]

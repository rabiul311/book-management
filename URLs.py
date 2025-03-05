# URLs
urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/new/', book_create, name='book_create'),
    path('book/edit/<int:pk>/', book_update, name='book_update'),
    path('book/delete/<int:pk>/', book_delete, name='book_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.BookListView.as_view(), name="books"),   
    path('books/<int:pk>/', views.BookDetailView.as_view(), name="book-detail"),
    path("book/create/", views.BookCreate.as_view(), name="book-create"),
    path("book/<int:pk>/update/", views.BookUpdate.as_view(), name="book-update"),
    path("book/<int:pk>/delete/", views.BookDelete.as_view(), name="book-delete"),
    
    path("authors/", views.AuthorListView.as_view(), name="authors"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
    path("author/create/", views.AuthorCreate.as_view(), name="author-create"),
    path("author/<int:pk>/update/", views.AuthorUpdate.as_view(), name="author-update"),
    path("author/<int:pk>/delete/", views.AuthorDelete.as_view(), name="author-delete"),   
    
    path("bookinstances/", views.BookInstanceListView.as_view(), name="bookinstances"),
    path("bookinstance/<uuid:pk>/", views.BookInstanceDetailView.as_view(), name="bookinstance-detail"),
    path("bookinstance/create/", views.BookInstanceCreate.as_view(), name="bookinstance-create"),
    path("bookinstance/<uuid:pk>/update/", views.BookInstanceUpdate.as_view(), name="bookinstance-update"),
    path("bookinstance/<uuid:pk>/delete/", views.BookInstanceDelete.as_view(), name="bookinstance-delete"),
    
    path("languages/", views.LanguageListView.as_view(), name="languages"),
    path("language/<int:pk>/", views.LanguageDetailView.as_view(), name="language-detail"),
    path("language/create/", views.LanguageCreate.as_view(), name="language-create"),
    path("language/<int:pk>/update/", views.LanguageUpdate.as_view(), name="language-update"),
    path("language/<int:pk>/delete/", views.LanguageDelete.as_view(), name="language-delete"),
    
    path("genres/", views.GenreListView.as_view(), name="genres"),
    path("genre/<int:pk>/", views.GenreDetailView.as_view(), name="genre-detail"),
    path("genre/create", views.GenreCreate.as_view(), name="genre-create"),
    path("genre/<int:pk>/update/", views.GenreUpdate.as_view(), name="genre-update"),
    path("genre/<int:pk>/delete/", views.GenreDelete.as_view(), name="genre-delete"),
    
    path("mybooks/", views.LoanedBooksByUserListView.as_view(), name="my-borrowed"),
    path("borrowed/", views.AllBorrowedBooksListView.as_view(), name="borrowed-books"),
    path("book/<uuid:pk>/renew", views.renew_book_librarian, name="renew-book-librarian"),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.BookListView.as_view(), name="books"),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name="book-detail"),
    path("authors", views.AuthorListView.as_view(), name="authors"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
    path("mybooks/", views.LoanedBooksByUserListView.as_view(), name="my-borrowed"),
    path("borrowed/", views.AllBorrowedBooksListView.as_view(), name="borrowed-books"),
    path("book/<uuid:pk>/renew", views.renew_book_librarian, name="renew-book-librarian"),
    path("author/create/", views.AuthorCreate.as_view(), name="author-create"),
    path("author/<int:pk>/update/", views.AuthorUpdate.as_view(), name="author-update"),
    path("author/<int:pk>/delete/", views.AuthorDelete.as_view(), name="author-delete"),
    path("book/create/", views.BookCreate.as_view(), name="book-create"),
    path("book/<int:pk>/update/", views.BookUpdate.as_view(), name="book-update"),
    path("book/<int:pk>/delete/", views.BookDelete.as_view(), name="book-delete"),
    
    path("bookinstances/", views.BookInstanceListView.as_view(), name="bookinstances"),
    path("bookinstance/<uuid:pk/", views.BookInstanceDetailView.as_view(), name="bookinstance-detail"),
    path("languages/", views.LanguageListView.as_view(), name="languages"),
    path("language/<int:pk>/", views.LanguageDetailView.as_view(), name="language-detail"),
    path("genres/", views.GenreListView.as_view(), name="genres"),
    path("genre/<int:pk>/", views.GenreDetailView.as_view(), name="genre-detail"),
    path("genre/create", views.GenreCreate.as_view(), name="genre-create"),
    path("genre/<int:pk>/update/", views.GenreUpdate.as_view(), name="genre-update"),
    path("genre/<int:pk>/delete/", views.GenreDelete.as_view(), name="genre-delete"),
]

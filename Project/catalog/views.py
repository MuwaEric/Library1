from django.shortcuts import render
from .models import Book, Genre, BookInstance, Author
from django.views import generic

# Create your views here.
def index(request):
    # generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    
    num_authors = Author.objects.count()
    
    c_genre = Genre.objects.filter(name__icontains="c").count()
    
    genre_with_word_action = Genre.objects.filter(name__icontains="action").count()
    
    book_with_word_curse = Book.objects.filter(title__icontains = "curse").count()
    
    context = {
        "num_books" : num_books,
        "num_instances" : num_instances,
        "num_instances_available" : num_instances_available,
        "num_authors" : num_authors,
        "c_genre" : c_genre, 
        "genre_with_word_action" : genre_with_word_action, 
        "book_with_word_curse" : book_with_word_curse,  
    }
    
    return render(request, "index.html", context)

class BookListView(generic.ListView):
    model = Book
    # context_object_name = "book_list"  #name to apply in the template
    # queryset = Book.objects.all()[:5]
    # template_name = "catalog/book_list.html"
    
    # adding context data to the already existing context
    def get_context_data(self, **kwargs):
        # Calling the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # additional data to add to the appliaction context
        context["new_context_data"] = "i have added some context data"
        return context
    
class BookDetailView(generic.DetailView):
    model = Book


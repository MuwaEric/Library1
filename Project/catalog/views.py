import datetime
from django.shortcuts import render
from .models import Book, Genre, BookInstance, Author, Language
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import RenewBookForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.

def index(request):
    # generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()
    
    num_visits = request.session.get("num_visits", 0)
    num_visits += 1
    request.session['num_visits'] = num_visits
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    
    num_authors = Author.objects.count()
    
    c_genre = Genre.objects.filter(name__icontains="c").count()
    
    genre_with_word_action = Genre.objects.filter(name__icontains="action").count()
    
    book_with_word_curse = Book.objects.filter(title__icontains = "curse").count()
    
    context = {
        "num_books" : num_books,
        "num_instances" : num_instances,
        "num_author": num_authors,
        "num_instances_available" : num_instances_available,
        "num_authors" : num_authors,
        "c_genre" : c_genre, 
        "genre_with_word_action" : genre_with_word_action, 
        "book_with_word_curse" : book_with_word_curse,
        "num_visits" : num_visits,
    }
    
    return render(request, "index.html", context)

class BookListView(generic.ListView):
    model = Book
    
    paginate_by = 5
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
    
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5
    
class AuthorDetailView(generic.DetailView):
    model = Author
    
class BookInstanceListView(generic.ListView):
    model = BookInstance
    paginate_by = 10
    
class BookInstanceDetailView(generic.DetailView):
    model = BookInstance
    
class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 10
    
class GenreDetailView(generic.DetailView):
    model = Genre
    
class LanguageListView(generic.ListView):
    model = Language
    paginate_by = 10
    
class LanguageDetailView(generic.DetailView):
    model = Language

    
class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 5
    
    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact="o")
            .order_by('due_back')
        )
        
class AllBorrowedBooksListView(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
# class AllBorrowedBooksListView(LoginRequiredMixin, generic.ListView):
    permission_required = "catalog.can_mark_returned"
    model = BookInstance
    template_name = "catalog/bookinstance_borrowed_all.html"
    
    def get_queryset(self):
        return (
            BookInstance.objects.filter(status__exact="o")
        )

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)
    
    # process the form data if it is POST request
    if request.method == "POST":
        
        # Creating a form instance and populating it with data from the request (binding):
        form = RenewBookForm(request.POST)
        
        if form.is_valid():
            # process the data in form.cleaned_data as required
            book_instance.due_back = form.cleaned_data["renewal_date"]
            book_instance.save()
            
            return HttpResponseRedirect(reverse('borrowed-books'))
        
    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={"renewal_date": proposed_renewal_date})
        
    context = {
        "form": form,
        "book_instance": book_instance,
    }
    
    return render(request, "catalog/book_renewal_librarian.html", context)

class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {"date_of_death": "11/11/2023"}
    permission_required = "catalog.add_author"
    
class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    # Not recommended (potential security issue if more fields added)
    fields = "__all__"
    permission_required = "catalog.change_author"

class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy("authors")
    permission_required = "catalog.delete_author"
    
    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("author-delete", kwargs={"pk": self.object.pk})
            )
            
class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = "__all__"
    permission_required = "catalog.add_book"
    
class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = "__all__"
    permission_required = "catalog.change_book"
    
class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("books")
    permission_required = "catalog.delete_book"
    
    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            reverse("book-delete", kwargs={"pk": self.object.pk})
            
class GenreCreate(PermissionRequiredMixin, CreateView):
    model = Genre
    fields = "__all__"
    permission_required = "catalog.add_genre"
    
class GenreUpdate(PermissionRequiredMixin, UpdateView):
    model = Genre
    fields = ["name"]
    permission_required = "catalog.change_genre"
    
class GenreDelete(PermissionRequiredMixin, DeleteView):
    model = Genre
    success_url = reverse_lazy("genres")
    permission_required = "catalog.delete_genre"
    
    def form_valid(self, form):
        try:
            self.object.delete()
        except Exception as e:
            reverse("genre-detail", kwargs={"pk":self.object.pk})
    
            
   

        
    
    
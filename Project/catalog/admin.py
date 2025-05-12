from django.contrib import admin
from . models import Genre, Language, Book, BookInstance, Author

# Register your models here.
class BookInLine(admin.TabularInline):
    model = Book
    
    extra = 0


@admin.register(Author) #alternative for admin.site.register(Author, AuthorAdmin)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "date_of_birth", "date_of_death"]
    
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]
    
    inlines = [BookInLine]
    

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
    
    extra = 1
       
    
@admin.register(Book)  #alternative for admin.site.register(Book, BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "display_genre"]
    
    inlines = [BookInstanceInLine]
    

@admin.register(BookInstance)  #alternative for admin.site.register(BookInstance, BookInstanceAdmin)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ["book", "status", "due_back", "id"]
    
    list_filter = ["status", "due_back"]
    
    fieldsets = [
        (None, {"fields": ('id', 'book', 'imprint')}),
        ("Availability", {"fields": ("due_back", "status")}),
    ]
    
    
    


admin.site.register(Genre)
admin.site.register(Language)

# admin.site.register(Book, BookAdmin)
# admin.site.register(BookInstance, BookInstanceAdmin)
# admin.site.register(Author, AuthorAdmin)


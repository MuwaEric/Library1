from django.test import TestCase

from catalog.models import Author

class AuthorModelTest(TestCase):
    @classmethod
    
    def setUpTestData(cls):
        # non modeified data throughout the test
        Author.objects.create(first_name="Eric", last_name="Muwanika")
        
    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, "first name")
        
    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")
    
    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("date_of_birth").verbose_name
        self.assertEqual(field_label, "date of birth")
     
    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("date_of_death").verbose_name
        self.assertEqual(field_label, "Died")
        
    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 100)
        
    def test_object_name_is_first_name_coma_last_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f"{author.first_name}, {author.last_name}"
        self.assertEqual(str(author), expected_object_name)
        
    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/catalog/authors/1/')
        























# class YourTestClass(TestCase):
#     @classmethod
    
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up unmodified data for all class methods")
#         pass
    
#     def setUp(self):
#         print("setUp: Run once for every test method to set up clean data")
#         pass
    
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)
        
#     def test_false_is_true(self):
#         print("Method: test_false_is_true")
#         self.assertTrue(False)
        
#     def one_plus_one_equals_two(self):
#         print("Method: one plus one equals two")
#         self.assertEqual(1 + 1, 2)
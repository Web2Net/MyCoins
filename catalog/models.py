from django.db import models

class Ruler(models.Model): # Model representing a book genre (e.g. Science Fiction, Non Fiction).
    
    name = models.CharField(max_length=200, help_text="Введите имя правителя, генсека, призидента..")
    year_of_rule = models.CharField(max_length=200, help_text="Введите годы правления", blank=True)
    
    def __str__(self): # String for representing the Model object (in Admin site etc.)
                
        return self.name

class Material(models.Model): # Model representing a book genre (e.g. Science Fiction, Non Fiction).
    
    material = models.CharField(max_length=200, help_text="Ведите полное название метериала (медь, серебро, золото..)")
    material_short = models.CharField(max_length=200, help_text="Ведите краткое название метериала (Cu, Ag, Au..)")
    
    def __str__(self): # String for representing the Model object (in Admin site etc.)
                
        return self.material_short

class Nominal(models.Model): # Model representing a book genre (e.g. Science Fiction, Non Fiction).
    
    nominal = models.CharField(max_length=200, help_text="Ведите номинал (полушка, 5 копеек, 10 рублей..)")
    
    def __str__(self): # String for representing the Model object (in Admin site etc.)
                
        return self.nominal

class MD(models.Model): # Model representing a book genre (e.g. Science Fiction, Non Fiction).
    
    md = models.CharField(max_length=200, help_text="Ведите монетный двор (ЕМ, АМ, КМ, СПБ..)")
    
    def __str__(self): # String for representing the Model object (in Admin site etc.)
                
        return self.md

class MCM(models.Model): # Model representing a book genre (e.g. Science Fiction, Non Fiction).
    
    mcm = models.CharField(max_length=200, help_text="")
    
    def __str__(self): # String for representing the Model object (in Admin site etc.)
                
        return self.mcm

class Gyrt(models.Model): # Model representing a book genre (e.g. Science Fiction, Non Fiction).
    
    gyrt = models.CharField(max_length=200, help_text="")
    
    def __str__(self): # String for representing the Model object (in Admin site etc.)
                
        return self.gyrt

class Redkost(models.Model): # Model representing a book genre (e.g. Science Fiction, Non Fiction).

    redkost = models.CharField(max_length=200, help_text="")
    
    def __str__(self): # String for representing the Model object (in Admin site etc.)
                
        return self.redkost


from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Coin(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    nominal = models.ForeignKey('Nominal',  on_delete=models.SET_NULL, null=True, help_text="Select a nominal for this coin")
    year = models.CharField(max_length=20, help_text="Год выпуска", default="0000")
    ruler = models.ForeignKey('Ruler', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    #language = models.ForeignKey('Language',  on_delete=models.SET_NULL, null=True, help_text="Select a language for this book")
    #summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book", blank=True)

    material = models.ForeignKey('Material',  on_delete=models.SET_NULL, null=True, help_text="Select a material for this coin")
    md = models.ForeignKey('MD',  on_delete=models.SET_NULL, null=True, help_text="Выберете монетный двор", blank=True)
    mcm = models.ForeignKey('MCM',  on_delete=models.SET_NULL, null=True, help_text="Минцмейстер", blank=True)
    gyrt = models.ForeignKey('Gyrt',  on_delete=models.SET_NULL, null=True, help_text="Гурт", blank=True)
    redkost = models.ForeignKey('Redkost',  on_delete=models.SET_NULL, null=True, help_text="Редкость", blank=True)
    tirazh = models.CharField(max_length=20, help_text="Тираж", blank=True)
    bitkin = models.CharField(max_length=20, help_text="Ведите номер по каталогу Биткина (#456)")
    nalichie = models.CharField(max_length=3, help_text="Количество в коллекции", blank=True)
    note = models.TextField(max_length=1000, help_text="Примечания", blank=True)
    #summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book", blank=True)
    #isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', blank=True)
    #genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
    
        return self.bitkin

    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('coin-detail', args=[str(self.id)])

"""
import uuid # Required for unique book instances

class BookInstance(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):
        
        return '%s (%s)' % (self.id,self.book.title)

"""

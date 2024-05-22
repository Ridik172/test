from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class View(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the type of work ")

    def __str__(self):
        return self.name

    # Model representing a work genre (e.g. Science Fiction, Non Fiction).


class Proletary(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_work = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('Proletary-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    # Model representing an Proletary.


class Work(models.Model):
    title = models.CharField(max_length=200)
    Proletary = models.ForeignKey(Proletary, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Description")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    View = models.ManyToManyField(View, help_text="Type of work")

    def __str__(self):
        return self.title

    # Model representing a work (but not a specific copy of a work).


import uuid
from django.urls import reverse


class WorkInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID work")
    work = models.ForeignKey('Work', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Work availability')

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set work as returned"),)

    def __str__(self):
        return '%s (%s)' % (self.id,self.work.title)

    # Model representing a specific copy of a work (i.e. that can be borrowed from the WorkShop).


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # Model representing a user profile including user's profile picture.



from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title





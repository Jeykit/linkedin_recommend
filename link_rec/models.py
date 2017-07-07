from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm


INDUSTRY_CHOICES = (
    ('software', 'software'),
    ('entrepreneur', 'entrepreneur'),
    ('data_science', 'data science'),
    ('research', 'research'),
    ('finance', 'finance'),
    ('medicine', 'medicine'),
)

SCHOOL_NAMES = (
    ('uoft', 'University of Toronto'),
    ('harvard', 'Harvard'),
    ('MIT', 'MIT'),
    ('waterloo', 'Univertsity of Waterloo'),
)

PROGRAM_CHOICES = (
    ('computer_science', 'Computer Science'),
    ('commerce', 'Commerce'),
    ('medicine_lifesci', 'Medicine/Lifesci/Healthsci'),
    ('math_statistics', 'Math/Statistics/Physics'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One To One Field explains the One to One link
    name = models.CharField(max_length=250, default='name')
    current_school = models.CharField(max_length=100, choices=SCHOOL_NAMES, default='uoft')
    school_program = models.CharField(max_length=100, choices=PROGRAM_CHOICES, default='computer_science')
    school_of_interest = models.CharField(max_length=100, choices=SCHOOL_NAMES, default='uoft')
    industry_of_interest = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, default='software')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ParsedProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=500)
    header = models.CharField(max_length=500)
    school = models.CharField(max_length=500)
    school_program = models.CharField(max_length=500)


class JobTitle(ParsedProfile):
    job1 = models.CharField(max_length=500)
    job2 = models.CharField(max_length=500)
    job3 = models.CharField(max_length=500)
    job4 = models.CharField(max_length=500)
    job5 = models.CharField(max_length=500)
    job6 = models.CharField(max_length=500)
    job7 = models.CharField(max_length=500)
    job8 = models.CharField(max_length=500)
    job9 = models.CharField(max_length=500)


class Location(JobTitle):
    #profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    loc1 = models.CharField(max_length=500)
    loc2 = models.CharField(max_length=500)
    loc3 = models.CharField(max_length=500)
    loc4 = models.CharField(max_length=500)
    loc5 = models.CharField(max_length=500)
    loc6 = models.CharField(max_length=500)
    loc7 = models.CharField(max_length=500)
    loc8 = models.CharField(max_length=500)
    loc9 = models.CharField(max_length=500)
    #exp10 = models.CharField(max_length=500)



#TITLE_CHOICES = (
#    ('MR', 'Mr.'),
#    ('MRS', 'Mrs.'),
#    ('MS', 'Ms.'),
#)
#
#
#class Author(models.Model):
#    name = models.CharField(max_length=100)
#    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
#    birth_date = models.DateField(blank=True, null=True)
#
#    def __str__(self):
#        return self.name
#
#
#class Book(models.Model):
#    name = models.CharField(max_length=100)
#    authors = models.ManyToManyField(Author)


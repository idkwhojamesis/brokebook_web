from django.db import models

# Create your models here.
class Book(models.Model):
    CAMPUS_CHOICES = [
        ('LC', 'Lincoln Center'),
        ('RH', 'Rose Hill'),
        ('LR', 'Both'),
    ]
    SEMESTER_CHOICES = [
        ('F', 'Fall'),
        ('S', 'Spring'),
        ('U', 'Summer'),
    ]
    # Find a way to dynamically update year list?
    YEAR_CHOICES = [
        (2017, '2017'),
        (2018, '2018'),
        (2019, '2019'),
        (2020, '2020'),
        (2021, '2021'),
    ]
    CONDITION_CHOICES = [
        (1, 'New'),
        (2, 'Mint'),
        (3, 'Used'),
        (4, 'Bad'),
        (5, 'Unusable/Missing Parts'),
    ]
    date_created= models.DateTimeField(auto_now=True, editable=False)
    post_type= models.BooleanField('Offer(T)/Ask(F)')
    book_title= models.CharField(max_length=150)
    campus= models.CharField(max_length=2, choices=CAMPUS_CHOICES)
    professor= models.CharField(max_length=20)
    class_subject= models.CharField(max_length=8)
    class_section= models.CharField(max_length=3, null=True, blank=True)
    semester= models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    year= models.SmallIntegerField(choices=YEAR_CHOICES)
    online_code= models.BooleanField(null=True, blank=True)
    edition= models.CharField(max_length=20, null=True, blank=True)
    condition= models.SmallIntegerField(choices=CONDITION_CHOICES)
    contact_info = models.TextField(max_length=200, default="Contact info not provided.")

    def get_absolute_url(self):
        return "detail/%i" % self.pk

    def __str__(self):
        return self.book_title

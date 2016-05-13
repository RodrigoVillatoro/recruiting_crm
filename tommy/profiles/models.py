from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, db_index=True)
    title = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=250, blank=True)
    phone = models.CharField(max_length=25, blank=True)
    mobile = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=2)
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    is_primary_contact = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    # company = models.ForeignKey(Company, related_name='contacts')
    # created_by = models.ForeignKey(User, related_name='created_contacts',
    #                                db_index=True)
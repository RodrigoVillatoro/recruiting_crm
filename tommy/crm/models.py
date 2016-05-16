from django.core.urlresolvers import reverse
from django.db import models
# from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(max_length=31, unique=True)

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('crm_skill_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class City(models.Model):
    geonameid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    feature_code = models.CharField(max_length=15)
    country_code = models.CharField(max_length=2, db_index=True)
    population = models.IntegerField(default=0)

    class Meta:
        ordering = ('name', 'country_code')

    def __str__(self):
        return '{}, {}'.format(self.name, self.country_code.upper())


class Company(models.Model):
    COUNTRY_CHOICES = (
        ('es', 'ES'),
    )
    STATUS_CHOICES = (
        ('n/a', 'N/A'),
        ('contacted', 'Contacted'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    )
    INDUSTRY_CHOICES = (
        ('internet', 'Internet'),
        ('gaming', 'Gaming'),
        ('other', 'Other')
    )
    name = models.CharField(max_length=100, db_index=True)
    legal_name = models.CharField(max_length=100, blank=True)
    cif = models.CharField(max_length=25, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    industry = models.CharField(max_length=15, choices=INDUSTRY_CHOICES)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    address = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    is_canonical_company = models.BooleanField(
        default=True,
        help_text='Official company, in case of duplicates',
        blank=True)
    fee = models.CharField(max_length=25, blank=True)
    nubelo_id = models.IntegerField(null=True, blank=True)
    nubelo_url = models.URLField(max_length=250, blank=True)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='n/a')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    city = models.ForeignKey(City, related_name='companies')
    skills = models.ManyToManyField(Skill, related_name='companies')
    # created_by = models.ForeignKey(User, related_name='created_companies', db_index=True)
    # owner = models.ForeignKey(User, related_name='owners', default=created_by)
    # assigned_to = models.ForeignKey(User, related_name='assigned_companies')

    class Meta:
        ordering = ('-timestamp',)
        verbose_name_plural = "companies"

    def get_absolute_url(self):
        return reverse('crm_company_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class CompanyNote(models.Model):
    ACTION_CHOICES = (
        ('phone_call', 'Phone call'),
        ('meeting', 'Meeting'),
        ('email', 'Email'),
        ('proposal_sent', 'Proposal Sent'),
        ('proposal_signed', 'Proposal Signed'),
        ('blind_cv', 'Blind CV'),
        ('other', 'Other'),
    )
    action = models.CharField(max_length=15, choices=ACTION_CHOICES)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    blind_cvs_sent = models.IntegerField(default=0)
    is_highlighted = models.BooleanField(default=False)
    document = models.FileField(
        upload_to='uploads/notes/companies/%Y/%m/%d/', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    company = models.ForeignKey(Company, related_name='company_notes')
    # created_by = models.ForeignKey(User, related_name='created_c_notes', db_index=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.action


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, db_index=True)
    title = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=250, db_index=True)
    phone = models.CharField(max_length=25, blank=True)
    mobile = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=2)
    address = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    is_primary_contact = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    company = models.ForeignKey(Company, related_name='contacts')
    city = models.ForeignKey(City, related_name='contacts')
    # created_by = models.ForeignKey(User, related_name='created_contacts', db_index=True)

    class Meta:
        ordering = ('email',)

    def __str__(self):
        return '{}: {}'.format(self.email, self.company)


class Process(models.Model):
    JOB_TYPE_CHOICES = (
        ('freelance', 'Freelance'),
        ('employee', 'Employee'),
    )
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('won', 'Won'),
        ('lost', 'Lost'),
        ('canceled_by_client', 'Canceled by Client'),
    )
    title = models.CharField(max_length=250, db_index=True)
    description = models.TextField()
    zip_code = models.CharField(max_length=10, blank=True)
    num_vacancies = models.IntegerField(default=1)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.CharField(max_length=25, blank=True)
    total_income = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    document = models.FileField(
        upload_to='uploads/docs/process/%Y/%m/%d/', blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    company = models.ForeignKey(Company, related_name='processes')
    skills = models.ManyToManyField(Skill, related_name='processes')
    city = models.ForeignKey(City, related_name='processes')
    # created_by = models.ForeignKey(User, related_name='created_processes',
    #                                db_index=True)
    # assigned_to = models.ForeignKey(User, related_name='assigned_processes')
    # fee (por defecto es el de la empresa)
    # assigned to (por defecto el owner del cliente)

    class Meta:
        ordering = ('-timestamp',)

    def get_absolute_url(self):
        return reverse('crm_process_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}: {}'.format(self.company, self.title)


class ProcessNote(models.Model):
    ACTION_CHOICES = (
        ('candidates_sent', 'Candidates Sent'),
        ('client_interviewed_candidate', 'Client Interviewed Candidate'),
        ('client_made_job_offer', 'Client Made Job Offer'),
        ('candidate_accepted_offer', 'Candidate Accepted Offer'),
        ('candidate_rejected_offer', 'Candidate Rejected Offer'),
        ('other', 'Other'),
    )
    action = models.CharField(max_length=25, choices=ACTION_CHOICES)
    action_num_candidates = models.IntegerField(default=1)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    is_highlighted = models.BooleanField(default=False)
    document = models.FileField(
        upload_to='uploads/notes/process/%Y/%m/%d/', blank=True)
    process = models.ForeignKey(Process, related_name='process_notes')
    # created_by = models.ForeignKey(User, related_name='created_p_notes', db_index=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return '{}: {}'.format(self.process, self.action)


# Reports
# Por usuario: número de llamadas, visitas, candidatos enviados, entrevistas, blind cv,
# BUSCADOR DE EMPRESAS: código postal, sector, skill, etc.
# Las notas no pueden editarse
# Sincronizar todas las empresas que esten en bbdd que no tengan mailinator.
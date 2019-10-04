from django.db import models
from django.conf import settings

# Create your models here.
class Agreement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    invoice_date = models.DateField(blank=True)
    agreement_date = models.DateField(blank=True,null=True)
    agreement_valid_upto = models.DateField(blank=True,null=True)
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=128)
    business_type = models.CharField(max_length=28)
    the_charges_are = models.PositiveIntegerField(blank=True,null=True)
    gst_no = models.PositiveIntegerField(blank=True,null=True)
    address = models.TextField()
    image = models.ImageField(upload_to='signs/',blank=True)
    tax = models.PositiveIntegerField(default=2000,blank=True)
    total = models.PositiveIntegerField(blank=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.invoice_date = self.agreement_date
        self.invoice_date = self.invoice_date.replace(month=self.invoice_date.month + 1)
        self.tax = self.the_charges_are
        self.total = self.the_charges_are + self.tax
        super().save(*args, **kwargs)

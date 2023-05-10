from django.db import models
from datetime import date

# from com_report.com_report import settings

# Create your models here.
class Report(models.Model):
    proforma_invoice = models.CharField(max_length=100)
    description = models.TextField()
    
    issue_date = models.DateField()
    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.proforma_invoice
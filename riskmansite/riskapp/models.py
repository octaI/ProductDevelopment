import datetime

from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.



class RiskTypes(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    full_risk_name = models.CharField(max_length=100)
    risk_metadata = JSONField()

    def __str__(self):
        return [self.code, self.full_risk_name, self.risk_metadata]


class RiskEntries(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.ForeignKey(RiskTypes, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    risk_data = JSONField()

    def __str__(self):
        return [self.id, self.code, self.date, self.risk_data]

from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.


class RiskTypes(models.Model):
    id = models.AutoField
    code = models.CharField(max_length=4)
    full_risk_name = models.CharField
    risk_metadata = JSONField
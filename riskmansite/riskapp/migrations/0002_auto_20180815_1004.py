from django.db import migrations


import json

def create_initial_entries(apps,schema_editor):
    RiskTypes = apps.get_model('riskapp','RiskTypes')

    RiskTypes(code='TEST', full_risk_name='This is a test entry', risk_metadata={'name': 'text', 'date': 'date'}).save()
    RiskTypes(code='CAR1', full_risk_name='Car Insurance',
              risk_metadata={'name2': 'text', 'date': 'date', 'model': 'text'}).save()

class Migration(migrations.Migration):

    dependencies = [
        ('riskapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_entries),
    ]

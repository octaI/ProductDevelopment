from django.test import TestCase
from .models import *

import json


# Create your tests here.

risktype_json = {'name': 'text', 'date': 'date'}
riskentry_json = {'name': 'Richard Test', 'date': '08-07-2018'}

class RisksTestCase(TestCase):

    def setUp(self):
        risk_type = RiskTypes(code='TEST', full_risk_name='This is a test entry', risk_metadata=json.dumps(risktype_json))
        insurer.save()
        risk_type.save()
        risk_entry = RiskEntries(code=risk_type, risk_data=json.dumps(riskentry_json))
        risk_entry.save()

    def test_correct_RiskTypes_save(self):
        q = RiskTypes.objects.get(code='TEST')
        self.assertEquals(q.code,'TEST')
        json_qdata = json.loads(q.risk_metadata)
        self.assertEquals(risktype_json['name'],json_qdata['name'])

    def test_correct_RiskEntries_save(self):
        q = RiskEntries.objects.get(code='TEST')
        json_qdata = json.loads(q.risk_data)
        self.assertEquals(riskentry_json['name'],json_qdata['name'])
        self.assertEquals(json_qdata['date'],riskentry_json['date'])

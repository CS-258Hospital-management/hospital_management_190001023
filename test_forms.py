from django.test import SimpleTestCase
from web_app.forms import SugarForm,bpForm,billing,pharm

class TestForms(SimpleTestCase):

    def test_sugar_form_valid_data(self):
        form = SugarForm(data={
            'userid' : 1,
            'testid' : 2
        })
        
        self.assertIsNone('userid')


    def test_sugar_form_no_data(self):
            form = SugarForm(data={})
            self.assertFalse(form.is_valid())
            self.assertEquals(len(form.errors),2)

    def test_bp_form_valid_data(self):
        form = bpForm(data={
            'uid' : 1,
            'tid' : 2
        })
        self.assertTrue(form.is_valid())


    def test_bp_form_no_data(self):
            form = bpForm(data={})

            self.assertFalse(form.is_valid())
            self.assertEquals(len(form.errors),2) 

    def test_billing_form_valid_data(self):
        form = billing(data={
            'userid' : 1,
            'date' : 2004-10-11,
            'amount': 200
        })
        self.assertTrue(form.is_valid())   

    def test_billing_form_no_data(self):
            form = billing(data={})
            self.assertFalse(form.is_valid())
            self.assertEquals(len(form.errors),3)  

    def test_pharmacy_form_valid_data(self):
        form = pharm(data={
            'Medicine_ID' : 1,
            'Medicine_Name' : 'paracetamol',
            'Stock_Left': 50,
            'Last_updated': 2009-11-12
        })
        self.assertTrue(form.is_valid())    

    def test_pharmacy_form_no_data(self):
            form = pharm(data={})
            self.assertFalse(form.is_valid())
            self.assertEquals(len(form.errors),4)         
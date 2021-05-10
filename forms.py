from django import forms

class SugarForm(forms.Form):
    userid = forms.IntegerField()
    testid = forms.IntegerField()

class bpForm(forms.Form):
    uid = forms.IntegerField()
    tid = forms.IntegerField()

class billing(forms.Form):
    userid = forms.IntegerField()
    date = forms.DateField()
    amount = forms.CharField(max_length=10)

class pharm(forms.Form):
    Medicine_Id = forms.IntegerField()  
    Medicine_Name = forms.CharField(max_length=50)  
    Stock_Left = forms.IntegerField() 
    Last_updated = forms.DateField()
  

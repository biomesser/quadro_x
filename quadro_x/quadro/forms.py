from django import forms

class Ins_int(forms.Form):
    def __init__(self):
        self.my_a = forms.IntegerField()
        self.my_b = forms.IntegerField()
        self.my_c = forms.IntegerField()
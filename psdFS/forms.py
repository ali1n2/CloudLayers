from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    num_merge = forms.IntegerField()
    counter = forms.IntegerField()
    merge_condition = forms.CharField()
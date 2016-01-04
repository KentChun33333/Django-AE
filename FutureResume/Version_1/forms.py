
from django import forms
from models import UploadFile, Document, Job_2




class UploadFileForm(forms.ModelForm):
    class Meta :
        model = UploadFile
        fields = '__all__' # or a list of the fields that you want to include in your form

class UploadDocForm(forms.ModelForm):
    class Meta :
        model = Document
        fields = '__all__'



class UploadFileForm_2(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class Job_2Form(forms.ModelForm):
    class Meta :
        model = Job_2
        fields = '__all__'	
        #exclude = 'etc'
   ################################################################
   # Do some self validation strategy ...
   ################################################################
   #def clean_xxx(self):
   #	xxx =self.clean_data.get('xxx')
   #	do something ...
   #	if not viariables == "some rules":
   #		raise forms.ValidationError("plz check ...some rules")
   #	return xxx
   ################################################################



class NotusemodelForm(forms.Form):
	title = forms.CharField(max_length=50)
	name = forms.CharField(max_length=50)
	file = forms.FileField()






















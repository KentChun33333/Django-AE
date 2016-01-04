1.       定义form，限制文件上传类型
class UploadFileForm(forms.Form):
    afile = forms.FileField()
    def clean_afile(self):
        data = self.cleaned_data['afile']
        file_name_suffix = os.path.splitext(data.name)[1].lower()
        if file_name_suffix !='.csv':
            raise forms.ValidationError(u"只能上传csv文件。")
        return data
2.       模板
<form action="/importAgencyCustomers/" enctype="multipart/form-data" name="form1" method="post" id="form1">  
            <fieldset class="module aligned ">
               
                <div class="form-row">
                    <div class="form-row">           
                        {{ form.afile.errors }} 
                        <label for="id_afile" class="required">&#19978;&#20256;csv&#25991;&#20214;:</label> {{form.afile}}
                    </div>           
                </div>
               
            </fieldset>
            <br>
            <div class="submit-row" >
                <input type="submit" value="&#20445;&#23384;" class="default" name="_save" onclick="save();"/><input type="submit" value="&#21462;&#28040;" class="default" name="_cancel" onclick="cancel()" />      
            </div>
        <form>
3.       读写文件
@login_required
def importAgencyCustomers(request):
    if not isCustomerAdmin(request):     
        return HttpResponseRedirect('/admin/customer/noRight/') 
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['afile'])
            addAgencyCustomers()
            return HttpResponseRedirect('/admin/app/agency/')
    else:
        form = UploadFileForm()
    t = loader.get_template('app/addAgencyCustomer.html')
    c = RequestContext(request,{'form':form})  
    return HttpResponse(t.render(c))
 
def handle_uploaded_file(f):
    destination = open('euroimmun/agency_customers.csv', 'wb+')
    print os.path.abspath('euroimmun/agency_customers.csv')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
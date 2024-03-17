from django.shortcuts import render,redirect
from django.db.models import Q
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import Patient,Records
from .forms import PatientForm , RecordForm


def home_page(request):
    
    q=request.GET.get('q')  if request.GET.get('q')!= None else ''
    patient=Patient.objects.filter(
        Q(full_name__icontains=q)|
        Q(phone__icontains=q)
        )
    patient_count=patient.count()
    context={
        'patients':patient,
        'patient_count':patient_count
    }
    return render(request,'patients/patient_list.html',context)

class Patient_create(CreateView):
    # form_class=PatientForm
    form_class=PatientForm
    template_name='patients/patient_create.html'
    context_object_name= 'form'
    
    def get_success_url(self) -> str:
        return reverse_lazy('patients:home')

class Patient_update(UpdateView):
    template_name='patients/patient_update.html'
    queryset=Patient.objects.all()
    form_class=PatientForm
    
    def get_object(self, queryset=None):
        # Access the pk value from self.kwargs and use it to retrieve the object
        pk = self.kwargs.get('pk')
        obj = super().get_object(queryset=queryset)
        return obj
    
    def get_success_url(self) -> str:
        pk=self.kwargs.get('pk')
        print('Value of the pk=',pk)
        return reverse_lazy('patients:patient-detail',kwargs={'pk':pk})
    
class Patient_delete(DeleteView):
    template_name='patients/patient_delete.html'
    queryset=Patient.objects.all()
    
    def get_success_url(self) -> str:
        return reverse_lazy('patients:home')
    
def create_record(request,pk):
    
    patient=Patient.objects.get(pk=pk)
    
    if request.method=='POST':
        form=RecordForm(request.POST)
        if form.is_valid():
            patient_cause=form.cleaned_data["patient_cause"]
            treatments=form.cleaned_data["treatments"]
            reports=form.cleaned_data["reports"]
            doctor=form.cleaned_data["doctor"]
            a=Records.objects.create(
                patient=patient,
                patient_cause=patient_cause,
                treatments=treatments,
                reports=reports,
                doctor=doctor,)
        target_url=reverse('patients:patient-detail',kwargs={'pk':pk})
        return redirect(target_url)
    else:
        form = RecordForm()
    
    context={
        'form':form,
        'patient':patient,
    }
    
    return render(request,'patients/record_create.html',context)
    
def Patient_detail(request,pk):
    try:
        patient = Patient.objects.get(pk=pk)
        records = patient.records.all().order_by('-created_on')  # Retrieve all records related to the patient
    except Patient.DoesNotExist:
        patient = None
        records = []

    context = {
        'patient': patient,
        'records': records,
    }

    return render(request, 'patients/patient_details.html', context)

def view_record(request,pk):
    record=Records.objects.get(pk=pk)
    context={
        'Records':record
    }
    return render(request,'patients/record_detail.html',context)

class Record_update(UpdateView):
    template_name='patients/record_update.html'
    queryset=Records.objects.all()
    form_class=RecordForm
    
    def get_object(self, queryset=None):
        # Access the pk value from self.kwargs and use it to retrieve the object
        pk = self.kwargs.get('pk')
        obj = super().get_object(queryset=queryset)
        return obj
    
    def get_success_url(self) -> str:
        pk=self.kwargs.get('pk')
        print('Value of the pk=',pk)
        return reverse_lazy('patients:record-detail',kwargs={'pk':pk})


class Delete_record(DeleteView):
    template_name='patients/record_delete.html'
    queryset=Records.objects.all()
    context_object_name="Records"
    
    def get_success_url(self) -> str:
        return reverse('patients:home')
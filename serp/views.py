from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from .models import Invoice, Consultation, Service, Customer
from .forms import sample_form, CustomerForm, ConsultationForm, InvoiceForm

# Create your views here.
@login_required
def index(request):
    global_search("ali")
    messages.add_message(request, messages.SUCCESS, 'Hello world.')
    return render(request, 'serp/index.html', {})

@login_required
def sample_request(request):
    if request.method == 'POST':
        form = sample_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('index')
    else:
        messages.add_message(request, messages.ERROR, 'sample message on form.')
        form = sample_form()
    return render(request, 'serp/sample_form.html', {'form': form}) 

    # get the list of invoices 
    invoices = Invoice.objects.all()

    # get only rows from invoice table
    rows = Invoice.objects.values_list('id', 'date', 'reference', 'amount', 'payment_amount', 'currency', 'consultation', 'service', 'status')

    # get only columns from invoice table
    columns = Invoice.objects.values('id', 'date', 'reference', 'amount', 'payment_amount', 'currency', 'consultation', 'service', 'status')

    messages.add_message(request, messages.SUCCESS, 'Hello world.')
    print(rows)
    return render(request, 'serp/sample_grid.html', {'invoices': invoices, 'rows': rows, 'columns': columns})

def global_search(query):
    results = []
    print("#" * 100)
    print("query: ", query)
    for model in [Invoice, Consultation, Service, Customer]:
        try:
            ct = ContentType.objects.get_for_model(model)
            fields = [field.name for field in model._meta.get_fields()]
            q_objects = []
            for field in fields:
                related_model = model._meta.get_field(field).related_model
                if related_model:
                    pass
                    #q_objects.append(Q(**{field + '__in': related_model.objects.filter(name__icontains=query)}))
                else:
                    q_objects.append(Q(**{field + '__icontains': query}))

            local_query  = q_objects.pop()
            for q_object in q_objects:
                local_query  |= q_object
            for obj in model.objects.filter(local_query):
                results.append({
                    'object': obj,
                    'model': ct.model
                })
        except Exception as e:
            print(e)
    print(results)
    return results

@login_required
def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            Customer.objects.create(**form.cleaned_data)
            messages.add_message(request, messages.SUCCESS, 'Customer added successfully.')
            return redirect('customer_list_url')
        else:
            messages.add_message(request, messages.ERROR, 'Customer could not be added.')
            return render(request, 'serp/customer_add.html', {'form': form})
    
    else:
        form = CustomerForm()
        return render(request, 'serp/customer_add.html', {'form': form})

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'serp/customer_list.html', {'customers': customers})

@login_required
def customer_edit(request, customer_id):
    
    if Customer.objects.filter(id=customer_id).count() == 0:
        messages.add_message(request, messages.ERROR, 'Customer does not exist in the system.')
        return redirect('customer_add_url')
    else:
        customer = Customer.objects.get(id=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Customer updated successfully.')
            return redirect('customer_list_url')
        else:
            messages.add_message(request, messages.ERROR, 'Customer could not be updated.')
            return render(request, 'serp/customer_edit.html', {'form': form, 'customer': customer})
    else:
        form = CustomerForm(instance=customer)
        return render(request, 'serp/customer_edit.html', {'form': form, 'customer': customer})

@login_required
def consultation_list(request):
    consultations = Consultation.objects.all()
    return render(request, 'serp/consultation_list.html', {'consultations': consultations})

@login_required
def consultation_add(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            Consultation.objects.create(**form.cleaned_data)
            messages.add_message(request, messages.SUCCESS, 'Consultation added successfully.')
            return redirect('consultation_list_url')
        else:
            messages.add_message(request, messages.ERROR, 'Consultation could not be added.')
            return render(request, 'serp/consultation_add.html', {'form': form})
    else:
        form = ConsultationForm()
        return render(request, 'serp/consultation_add.html', {'form': form})

@login_required
def consultation_edit(request, consultation_id):
    if Consultation.objects.filter(id=consultation_id).count() == 0:
        messages.add_message(request, messages.ERROR, 'Consultation does not exist in the system.')
        return redirect('consultation_add_url')
    else:
        consultation = Consultation.objects.get(id=consultation_id)

    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Consultation updated successfully.')
            return redirect('consultation_list_url')
        else:
            messages.add_message(request, messages.ERROR, 'Consultation could not be updated.')
            return render(request, 'serp/consultation_edit.html', {'form': form, 'consultation': consultation})
    else:
        form = ConsultationForm(instance=consultation)
        return render(request, 'serp/consultation_edit.html', {'form': form, 'consultation': consultation})

@login_required
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'serp/invoice_list.html', {'invoices': invoices})

@login_required
def invoice_add(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            Invoice.objects.create(**form.cleaned_data)
            messages.add_message(request, messages.SUCCESS, 'Invoice added successfully.')
            return redirect('invoice_list_url')
        else:
            messages.add_message(request, messages.ERROR, 'Invoice could not be added.')
            return render(request, 'serp/invoice_add.html', {'form': form})
    else:
        form = InvoiceForm()
        return render(request, 'serp/invoice_add.html', {'form': form})

@login_required
def invoice_edit(request, invoice_id):
    if Invoice.objects.filter(id=invoice_id).count() == 0:
        messages.add_message(request, messages.ERROR, 'Invoice does not exist in the system.')
        return redirect('invoice_add_url')
    else:
        invoice = Invoice.objects.get(id=invoice_id)

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Invoice updated successfully.')
            return redirect('invoice_list_url')
        else:
            messages.add_message(request, messages.ERROR, 'Invoice could not be updated.')
            return render(request, 'serp/invoice_edit.html', {'form': form, 'invoice': invoice})
    else:
        form = InvoiceForm(instance=invoice)
        return render(request, 'serp/invoice_edit.html', {'form': form, 'invoice': invoice})
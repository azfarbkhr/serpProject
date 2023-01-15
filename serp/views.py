from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from .models import Invoice, Consultation, Service, Customer
from .forms import sample_form, CustomerForm

# Create your views here.
@login_required
def index(request):
    global_search("ali")
    messages.add_message(request, messages.SUCCESS, 'Hello world.')
    return render(request, 'serp/index.html', {})

@login_required
def sample_request(request):
    # if request.method == 'POST':
    #     form = sample_form(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         return redirect('index')
    # else:
    #     messages.add_message(request, messages.ERROR, 'sample message on form.')
    #     form = sample_form()
    # return render(request, 'serp/sample_form.html', {'form': form}) 

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

def customer_list(request):
    customers = Customer.objects.all()
    # if none value in any field, then it will be replaced with empty string
    
    form = CustomerForm()
    return render(request, 'serp/customer_list.html', {'customers': customers, 'form': form})

def customer_edit(request, customer_id):
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
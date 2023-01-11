from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from .models import Invoice, Consultation, Service, Customer

# Create your views here.
@login_required
def index(request):
    global_search("ali")
    return render(request, 'serp/index.html')



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


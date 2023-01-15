from django.contrib import admin
from .models import Customer, Consultation, Service, Invoice

# Register your models here.
admin.site.register(Customer,
    list_display = ('first_name', 'last_name', 'city', 'province', 'address', 'postal_code', 'phone_number', 'email',),
    list_filter = ('first_name', 'last_name', 'city', 'province', 'address', 'postal_code', 'phone_number', 'email'),
    search_fields = ('first_name', 'last_name', 'city', 'province', 'address', 'postal_code', 'phone_number', 'email'),
    ordering = ('first_name',),

)

admin.site.register(Consultation,
    list_display = ('id', 'meeting_date', 'reason', 'comments', 'customer', 'status'),
    list_filter = ('meeting_date', 'customer', 'status'),
    search_fields = ('id', 'meeting_date', 'reason', 'comments', 'customer', 'status'),
    ordering = ('meeting_date', 'reason', 'comments', 'customer', 'status'),
    fields = ('meeting_date', 'status', 'customer', 'reason', 'comments', ),
)

admin.site.register(Service,
    list_display = ('code', 'name', 'status'),
    list_filter = ('status',),
    search_fields = ('code', 'name', 'status'),
    ordering = ('code', 'name', 'status'),
)

admin.site.register(Invoice,
    list_display = ('id', 'date', 'reference', 'amount', 'payment_amount', 'currency', 'consultation', 'service', 'status'),
    list_filter = ('date', 'currency', 'consultation__customer', 'consultation', 'service', 'status'), 
    search_fields = ('date', 'reference', 'amount', 'payment_amount', 'currency', 'consultation', 'service', 'status'),
    ordering = ('date', 'reference', 'amount', 'payment_amount', 'currency', 'consultation', 'service', 'status'),
)
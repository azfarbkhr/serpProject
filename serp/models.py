from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    postal_code = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.first_name


class Consultation(models.Model):
    class ConsultationStatus(models.TextChoices):
        PENDING = 'PENDING'
        IN_PROGRESS = 'PARKED'
        COMPLETED = 'COMPLETED'

    meeting_date = models.DateTimeField()
    reason = models.TextField(max_length=30, blank=True, null=True)
    comments = models.TextField(max_length=30, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=ConsultationStatus.choices, default=ConsultationStatus.PENDING)

    def __str__(self):
        return self.meeting_date.strftime('%Y-%m-%d') + ' ' + self.customer.first_name
    

class Service(models.Model):
    code = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    class InvoiceStatus(models.TextChoices):
        PENDING = 'PENDING'
        PAID = 'PAID'
        VOIDED = 'VOIDED'
        REFUNDED = 'REFUNDED'

    date = models.DateField()
    reference = models.CharField(max_length=30, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    currency = models.CharField(max_length=30, blank=True, null=True, default='CAD')
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=InvoiceStatus.choices, default=InvoiceStatus.PENDING)

    def __str__(self):
        return str(self.id) + ' ' + self.consultation.customer.first_name + ' ' + self.service.name + ' ' + self.status + ' ' + self.date.strftime('%Y-%m-%d')



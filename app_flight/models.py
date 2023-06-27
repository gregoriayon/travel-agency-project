from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class AirportModel(models.Model):
    city = models.CharField(max_length=122, null=True)
    country = models.CharField(max_length=122, null=True)
    airport = models.CharField(max_length=122, null=True)
    code = models.CharField(max_length=3, null=True)

    def __str__(self):
        return f"{self.id}- {self.code}"

    class Meta:
        verbose_name = "Airport"
        verbose_name_plural = "Airports"

        ordering = [
            '-id'
        ]

class AirplaneModel(models.Model):
    airplane_name = models.CharField(max_length=122, null=True)
    airplane_model = models.CharField(max_length=122, null=True)
    airplane_logo = models.ImageField(upload_to="airplane_logo", null=True, blank=True)

    def __str__(self):
        return f"{self.id}- {self.airplane_name}"
    
    class Meta:
        verbose_name = "Airplane"
        verbose_name_plural = "Airplanes"

        ordering = [
            '-id'
        ]


class DiscountModel(models.Model):
    discount_name = models.CharField(max_length=122, null=True)
    discount_code = models.CharField(max_length=122, null=True)
    amount = models.FloatField(null=True)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}- {self.amount} % [{self.created_at}]"

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

        ordering = [
            '-id'
        ]


class AirPlaneTicketModel(models.Model):
    FLGHT_TYPE_CHOICES = (
        ('Economy', 'Economy'),
        ('Business', 'Business'),
    )

    airplane = models.ForeignKey(AirplaneModel, on_delete=models.CASCADE, null=True)
    discount = models.ForeignKey(DiscountModel, on_delete=models.CASCADE, null=True, blank=True)
    flight_type =  models.CharField(max_length=122, choices=FLGHT_TYPE_CHOICES, null=True, default='Economy')
    base_adult_fare = models.FloatField(null=True)
    base_child_fare = models.FloatField(null=True)
    base_infant_fare = models.FloatField(null=True)
    adult_tax = models.FloatField(null=True)
    child_tax = models.FloatField(null=True)
    infant_tax = models.FloatField(null=True)
    baggage_cabin = models.FloatField(null=True)
    baggage_checkin = models.FloatField(null=True)

    location_from = models.ForeignKey(AirportModel, on_delete=models.CASCADE, null=True, related_name="location_from")
    location_to = models.ForeignKey(AirportModel, on_delete=models.CASCADE, null=True, related_name="location_to")

    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}- {self.airplane} ({self.flight_type})"

    class Meta:
        verbose_name = "AirPlane Ticket"
        verbose_name_plural = "AirPlane Tickets"

        ordering = [
            '-id'
        ]


class OrderFlightModel(models.Model):
    SELECT_TITLE = (
        ('MR.', 'MR.'),
        ('MS.', 'MS.'),
        ('MRS.', 'MRS.'),
        ('MASTER..', 'MASTER.'),
        ('MISS.', 'MISS.'),
    )

    select_title =  models.CharField(max_length=122, choices=SELECT_TITLE, null=True, default='MR.')
    ticket = models.ForeignKey(AirPlaneTicketModel, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=122, null=True)
    last_name = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122, null=True)
    phone = models.CharField(max_length=122, null=True)
    date_of_birth = models.DateField(auto_now=True, null=True)
    nationality = CountryField()

    def __str__(self):
        return f"{self.id}- {self.first_name} ({self.last_name}) - {self.phone}"

    class Meta:
        verbose_name = "Order Flight"
        verbose_name_plural = "Order Flights"

        ordering = [
            '-id'
        ]

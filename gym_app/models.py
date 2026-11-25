from django.db import models

# Create your models here.
class MemberDb(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.CharField(max_length=15,unique=True)
    email=models.EmailField()
    Joining_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class MembershipDb(models.Model):

    PLAN_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Yearly', 'Yearly'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Expired', 'Expired'),
    ]

    member = models.ForeignKey(
        MemberDb,
        on_delete=models.CASCADE,
        related_name='memberships'
    )

    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    def __str__(self):
        return self.member.name + " - " + self.plan

class PaymentDb(models.Model):

    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('Card', 'Card'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]

    member = models.ForeignKey(
        MemberDb,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    membership = models.ForeignKey(
        MembershipDb,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES
    )

    payment_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='Paid'
    )

    def __str__(self):
        return self.member.name + " - " + str(self.amount)
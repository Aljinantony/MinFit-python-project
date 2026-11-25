from django.contrib import admin
from gym_app.models import MemberDb,MembershipDb,PaymentDb

# Register your models here.
admin.site.register(MemberDb)
admin.site.register(MembershipDb)
admin.site.register(PaymentDb)

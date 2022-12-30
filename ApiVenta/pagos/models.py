from django.db import models

from usuarios.models import UserModel
from servicios.models import ServicesMoldel


# Create your models here.
class PaymentUserModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    service_id = models.ForeignKey(ServicesMoldel, on_delete=models.CASCADE)
    amount = models.FloatField()
    paymentDate = models.DateTimeField()
    expirationDate = models.DateTimeField()


class ExpiredPaymentsModel(models.Model):
    payment_user_id = models.ForeignKey(PaymentUserModel, on_delete=models.CASCADE)
    penalty_fee_amount = models.FloatField()
    

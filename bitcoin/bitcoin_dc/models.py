from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=160)

    def __str__(self):
        return self.address


class Transactions(models.Model):
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)
    # tid = models.CharField(max_length=64, default='tid')
    # date = models.PositiveIntegerField(default=1)
    # amount = models.PositiveIntegerField(default=1)

    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    tx_index = models.CharField(max_length=64, default='tid')
    time = models.PositiveIntegerField(default=1)
    size = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.tid

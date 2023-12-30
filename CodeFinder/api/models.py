from django.db import models
import string
import random
# Create your models here.
'''
def generate_unique_code():
    length = 8;
    while True:
        identifier = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Account.objects.filter(identifier=identifier).count() == 0:
            break
    return identifier
'''
class Account(models.Model):
    username = models.CharField(max_length = 12, unique = True)
    password = models.CharField(max_length = 12)

class Code(models.Model):
    contribution_title = models.CharField(max_length = 30)
    account = models.ForeignKey(Account, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)


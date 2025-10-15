from django.db import models
from django.contrib.auth.models import User as user

# Create your models here.
class expense(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateTimeField(auto_now_add=True)
    expense_description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.expense_amount} - {self.expense_date} - {self.expense_description} - {self.category}"
    
class category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category_name}"
    
class budget(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    planned_amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.TextField(null=True)

    def __str__(self):
        return f"{self.planned_amount} - {self.budget_amount} - {self.month}"
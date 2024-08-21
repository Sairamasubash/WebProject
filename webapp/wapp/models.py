# Import the models module from Django's database package.
from django.db import models

# Define a class named 'React' that inherits from Django's base 'Model' class.
class React(models.Model):
    
    # Define a CharField to store the employee's name.
    employee = models.CharField(max_length = 30)
    
    # Define a CharField to store the department's name or description.
    department = models.CharField(max_length = 200)
# Import the migrations and models modules from Django's database package. 
from django.db import migrations, models

# Define a class named 'Migration' that inherits from Django's 'Migration' class.
class Migration(migrations.Migration):

    # Indicate that this is the initial migration for this app. 
    initial = True

    # List of dependencies for this migration.
    dependencies = []
 
    # Define the operations that this migration will perform.
    operations = [

        # Create a new model in the database schema.
        migrations.CreateModel(

             # Specify the name of the model to be created. In this case, it's 'React'.
            name='React',
            
            # Define the fields that the 'React' model will contain.
            fields = 
            [
                # Define an 'id' field, which is an automatically incremented primary key. 
                ('id', models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')),

                # Define an 'employee' field, which is a character field with a maximum length of 30 characters.
                ('employee', models.CharField(max_length = 30)),

                # Define a 'department' field, which is a character field with a maximum length of 200 characters.
                ('department', models.CharField(max_length = 200)),
            ],
        ),
    ]
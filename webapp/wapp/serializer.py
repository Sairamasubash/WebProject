
# Import all components from Django REST framework.
from rest_framework import *
# Import all models from the current package. 
from . models import *

# Define a serializer class named 'ReactSerializer' which is a subclass of 'ModelSerializer'.
class ReactSerializer(serializers.ModelSerializer):

    # The 'Meta' class is used to specify additional options for the serializer.
    class Meta: 

        # Specifies the model that this serializer is based on. In this case, it's the 'React' model.
        model = React
        
        # Specifies the fields from the model that should be included in the serialized representation.
        fields = ['employee', 'department']
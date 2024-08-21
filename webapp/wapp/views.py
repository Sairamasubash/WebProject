# Import the render function from Django's shortcuts module, typically used to render templates. 
from django.shortcuts import render
# Import the APIView class from Django REST framework, which allows you to create class-based views that handle HTTP methods (GET, POST, DELETE, etc.).
from rest_framework.views import APIView
# Import all models from the current package. 
from . models import *
# Import all serializers from the current package. 
from . serializer import *
# Import the Response class from Django REST framework, which is used to return HTTP responses with the serialized data.
from rest_framework.response import Response

# Define a view class named 'ReactView' that inherits from 'APIView'. 
class ReactView(APIView):

    # Specify the serializer class to be used in this view. In this case, it's the 'ReactSerializer'.
    serializer_class = ReactSerializer

    # Define a method to handle GET requests. This method will be called when the client sends a GET request.
    def get(self, request):

        # Query all instances of the 'React' model from the database and create a list of dictionaries.
        output = [{"employee": output.employee, "department": output.department} for output in React.objects.all()]

        # Return the list of dictionaries as a JSON response to the client.
        return Response(output)

    # Define a method to handle POST requests. This method will be called when the client sends a POST request.
    def post(self, request):

        # Instantiate the 'ReactSerializer' with the data sent in the POST request.
        serializer = ReactSerializer(data = request.data)

        # Check if the data is valid according to the serializer's validation rules.
        if serializer.is_valid(raise_exception = True):

            # Save the validated data as a new instance of the 'React' model.
            serializer.save()

            # Return the serialized data of the newly created 'React' instance as a JSON response.
            return Response(serializer.data)

    # Define a method to handle DELETE requests. This method will be called when the client sends a DELETE request.
    def delete(self, request):

        # Delete all instances of the 'React' model from the database.
        React.objects.all().delete()  

        # Return a JSON response with a success message after all records are deleted.
        return Response({"message": "All records deleted successfully."})
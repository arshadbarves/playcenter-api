import random
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Welcome view

class WelcomeView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request):

        list_of_messages = [
            'Welcome to the API.',
            'Hurray! The API is up and running.Lets get started.',
            'Welcome to the API. Hurray! The API is up and running.Lets get started.',
            'Hurray! The API is up and running.Lets get started. Welcome to the API.',
            'Lets get started. Welcome to the API. Hurray! The API is up and running.',
            'Lets get started. Hurray! The API is up and running. Welcome to the API.',
        ]

        # return response
        return Response(
            data={
                'message': random.choice(list_of_messages)
            },
            status=status.HTTP_200_OK
        )
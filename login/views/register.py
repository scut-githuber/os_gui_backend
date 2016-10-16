from django.views.generic import View
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import Http404
import json


class RegisterView(View):
    def get(self, request):
        raise Http404()

    def post(self, request):
        try:
            result = {}

            received_json_data = json.loads(request.body.decode("utf-8"))
            username = received_json_data['_username']
            password = received_json_data['_password']
            email = received_json_data['_email']

            if User.objects.filter(username=username).exists():
                result['status'] = 'fail'
                result['reason'] = 'username_registered'
                return JsonResponse(result)

            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            result['status'] = 'success'
        except Exception as e:
            result['status'] = 'fail'
            result['reason'] = str(e)
        return JsonResponse(result)
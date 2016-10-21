from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.contrib.auth.models import User
import json


class RegisterCtrl():
    def pre_register(self, request):
        result = {}
        result['err'] = '0'
        result['csrftoken'] = get_token(request)
        return JsonResponse(result)

    def register(self, request):
        try:
            result = {}

            received_json_data = json.loads(request.body.decode("utf-8"))
            username = received_json_data['_username']
            password = received_json_data['_password']
            email = received_json_data['_email']

            if User.objects.filter(username=username).exists():
                result['err'] = '-1'
                result['msg'] = 'username_registered'
                return JsonResponse(result)

            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            result['err'] = '1'
        except Exception as e:
            result['err'] = '-3'
            # result['reason'] = str(e)
            result['msg'] = "sql_exception"
        return JsonResponse(result)

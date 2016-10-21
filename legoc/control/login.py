from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from django.http import JsonResponse
import json


class LoginCtrl():
    def pre_login(request):
        result = {}
        if request.user.is_authenticated():
            result['err'] = '2'
        else:
            result['err'] = '0'
            result['csrftoken'] = get_token(request)
        return JsonResponse(result)

    def login(request):
        try:
            result = {}
            received_json_data = json.loads(request.body.decode("utf-8"))
            username = received_json_data['_username']
            password = received_json_data['_password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    result['err'] = '1'
                else:
                    result['err'] = '-1'
                    result['msg'] = 'account_disabled'
            else:
                result['err'] = '-2'
                result['msg'] = 'wrong_password'
        except Exception as e:
            result['err'] = '-3'
            # result['reason'] = str(e)
            result['msg'] = "sql_exception"
        return JsonResponse(result)

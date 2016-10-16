from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.shortcuts import Http404
import json


class LoginView(View):
    def get(self, request):
        raise Http404()

    def post(self, request):
        try:
            result = {}
            received_json_data = json.loads(request.body.decode("utf-8"))
            username = received_json_data['_username']
            password = received_json_data['_password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    result['status'] = 'success'
                    result['csrftoken'] = get_token(request)
                else:
                    result['status'] = 'fail'
                    result['reason'] = 'account_disabled'
            else:
                result['status'] = 'fail'
                result['reason'] = 'wrong_password'
        except Exception as e:
            result['status'] = 'fail'
            result['reason'] = str(e)
        return JsonResponse(result)

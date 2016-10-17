from django.views.generic import View
from django.contrib.auth import logout
from django.http import JsonResponse
from .loginrequired import LoginRequiredMixin


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            result = {}
            logout(request)
            result['err'] = '1'
        except Exception as e:
            result['err'] = '-3'
            # result['reason'] = str(e)
            result['msg'] = "sql_exception"
        return JsonResponse(result)

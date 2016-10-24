from django.contrib.auth import logout
from django.http import JsonResponse


class LogoutCtrl():
    def logout(request):
        try:
            result = {}
            logout(request)
            result['err'] = '1'
        except Exception as e:
            result['err'] = '-3'
            # result['reason'] = str(e)
            result['msg'] = "sql_exception"
        return JsonResponse(result)

from django.views.generic import View
from django.contrib.auth import logout
from django.http import JsonResponse
from .loginrequired import LoginRequiredMixin


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            result = {}
            logout(request)
            result['status'] = 'success'
        except Exception as e:
            result['status'] = 'fail'
            result['reason'] = str(e)
        return JsonResponse(result)
    def post(self, request):
    	raise Http404()
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
from django.views.decorators.csrf import csrf_exempt

from legoc.control.node import child, brother, parent
from legoc.control.login import LoginCtrl
from legoc.control.logout import LogoutCtrl
from legoc.control.register import RegisterCtrl
from django.contrib.auth.decorators import login_required
from legoc.util import json_helper


@csrf_exempt
def node_child(request, node_id):
    """获取用例子结点信息"""
    node_list = child(node_id)
    if node_list is not None:
        return HttpResponse(json_helper.dumps_err(0, node_list))
    else:
        return HttpResponse(json_helper.dump_err_msg(-1, '返回错误'))


@csrf_exempt
def node_brother(request, node_id):
    """获取用例兄弟结点信息，默认传入的都是左结点"""
    node_list = brother(node_id)
    if node_list is not None:
        return HttpResponse(json_helper.dumps_err(0, node_list))
    else:
        return HttpResponse(json_helper.dump_err_msg(-1, '返回错误'))


@csrf_exempt
def node_parent(request, node_id):
    """获取用例父母结点信息"""
    node_list = parent(node_id)
    if node_list is not None:
        return HttpResponse(json_helper.dumps_err(0, node_list))
    else:
        return HttpResponse(json_helper.dump_err_msg(-1, '返回错误'))



def login(request):
    if request.method == 'GET':
        return LoginCtrl.pre_login(request)
    else:
        return LoginCtrl.login(request)


@login_required
def logout(request):
    return LogoutCtrl.logout(request)


def register(request):
    if request.method == 'GET':
        return RegisterCtrl.pre_register(request)
    else:
        return RegisterCtrl.register(request)

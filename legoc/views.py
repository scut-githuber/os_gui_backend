from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
from django.views.decorators.csrf import csrf_exempt

from legoc.control import tree
from legoc.control.node import child, brother, parent, ref_valid, xmls2nodes
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


@csrf_exempt
def node_connect(request, node_id_a, node_id_b, ref_type):
    ret, node_a, node_b = tree.ref_valid(node_id_a, node_id_b, ref_type)
    if ret:
        tree.node_join(node_a, node_b, ref_type)
        return HttpResponse(json_helper.dump_err_msg(0, 'success'))
    else:
        return HttpResponse(json_helper.dump_err_msg(-1, 'not exist or unable to connect'))


@csrf_exempt
def create_node(request, root_id, node_type):
    ret = tree.new_node(root_id, node_type)
    return HttpResponse(json_helper.dump_err_msg(0, ret))

@csrf_exempt
def remove_node(request, project_id, id_on_tree):
    ret = tree.delete_node(project_id, id_on_tree)
    return HttpResponse(json_helper.dump_err_msg(0, ret))

@csrf_exempt
def alter_node(request, node_id_alter, node_id_connect, ref_type):
    ret, node_alter, node_connect = tree.ref_valid(node_id_alter, node_id_connect, ref_type)
    if ret:
        tree.move_node(node_alter, node_connect, ref_type)
        return HttpResponse(json_helper.dump_err_msg(0, 'success'))
    else:
        return HttpResponse(json_helper.dump_err_msg(-1, 'not exist or unable to connect with another node'))

@csrf_exempt
def new_project(request, name, root_type, user_id):
    # 返回project id和根节点id
    ret = tree.new_project(name, root_type, user_id)
    return HttpResponse(json_helper.dump_err_msg(0, ret))


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


def init_rel(request):
    xmls2nodes()
    return HttpResponse('init success')

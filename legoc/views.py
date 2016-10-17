from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
from django.views.decorators.csrf import csrf_exempt

from legoc.control.node import child
from legoc.util import json_helper


@csrf_exempt
def node_child(request):
    """获取用例子结点信息"""
    node_id = request.GET['Node_id']
    node_list = child(node_id)
    if node_list is not None:
        return HttpResponse(json_helper.dumps_err(0, node_list))
    else:
        return HttpResponse(json_helper.dump_err_msg(-1, '返回错误'))



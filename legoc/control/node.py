from legoc.models import LGNode, NodeRef


def child(id):
    src_node = LGNode.objects.filter(pk=id)
    src_childs = NodeRef.objects.filter(node_right=src_node, ref=0)
    children = []
    for src_child in src_childs:
        children.append({
            'id': src_child.id,
            'name': src_child.node_left.name,
            'desp': src_child.node_left.desp
        })
    return children


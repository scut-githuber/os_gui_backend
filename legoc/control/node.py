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


def brother(id):
    src_node = LGNode.objects.filter(pk=id)
    src_brothers = NodeRef.objects.filter(node_left=src_node, ref=1)
    brothers = []
    for src_brother in src_brothers:
        brothers.append({
            'id': src_brother.id,
            'name': src_brother.node_right.name,
            'desp': src_brother.node_right.desp
        })
    return brothers


def parent(id):
    src_node = LGNode.objects.filter(pk=id)
    src_parents = NodeRef.objects.filter(node_left=src_node, ref=0)
    parents = []
    for src_parent in src_parents:
        parents.append({
            'id': src_parent.id,
            'name': src_parent.node_right.name,
            'desp': src_parent.node_right.desp
        })
    return parents


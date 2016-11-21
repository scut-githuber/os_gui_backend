from django.shortcuts import get_object_or_404

from legoc.models import LGNode, NodeRef


# import xmltodict
from legoc.util.xmls import travel_xml_file


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


def ref_valid(id1, id2, ref):
    ref_cnt = NodeRef.objects.filter(
        node_left=get_object_or_404(LGNode, id1), node_right=get_object_or_404(LGNode, id2), ref=ref
    ).count()
    return ref_cnt >= 1


def xml2node(xml_path):
    def on_node(node, current_parent, current_brother):
        if node.tag == 'name' or node.tag == 'description':
            return None
        new_node = LGNode()

        has_child = len(node)
        if has_child <= 0:
            # no children, a leaf node，必须要有一个code_path属性
            for (k, v) in node.attrib.items():
                if k == 'path':
                    new_node.code_path = v
                    break
        if len(node.attrib.items()) <= 0:
            # no attribute, use tag for name, use text for description
            new_node.name = node.tag
            new_node.desp = node.text
        else:
            attrib_cnt = 0
            for (k, v) in node.attrib.items():
                if k == 'name':
                    new_node.name = v
                    attrib_cnt += 1
                if k == 'description':
                    new_node.desp = v
                    attrib_cnt += 1
            if attrib_cnt < 2:
                for node_child in node:
                    if node_child.tag == 'name':
                        new_node.name = node.text
                    if node_child.tag == 'description':
                        new_node.desp = node.text

        if current_parent is not None:
            ref = NodeRef(ref=0, node_left=current_parent, node_right=new_node)
            ref.save()
        if current_brother is not None:
            ref = NodeRef(ref=1, node_left=current_brother, node_right=new_node)
            ref.save()
        return new_node

    travel_xml_file(xml_path, on_node)


def xmls2nodes():
    xml2node('test_data/application.xml')
    xml2node('test_data/player.xml')
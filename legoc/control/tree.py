from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from legoc.control import node
from legoc.models import Project, ProjectNodes
from legoc.util.data import pickle_save, pickle_load


class LGTree(object):
    def __init__(self, node_id, lg_node_id):
        """
        generate a lgtree
        :param node_id: id on tree, generated one by one
        :param lg_node_id: id of lg node, the type of node, different node on the tree may have the same lg node value
        """
        self.node_id = node_id
        self.data = lg_node_id
        self.parent = None
        self.children = list()
        self.store_path = 'tnode%d.pickle' % self.node_id

    def add_child(self, tnode):
        self.children.append(tnode)
        tnode.parent = self

    def rm_child(self, tnode):
        try:
            self.children.remove(tnode)
        except ValueError:
            pass

    def left(self):
        if self.parent is None:
            return None
        idx = self.parent.index(self)
        if idx == -1 or idx == 0:
            return None
        else:
            return self.parent[idx - 1]

    def right(self):
        if self.parent is None:
            return None
        idx = self.parent.index(self)
        if idx == -1 or idx == len(self.parent):
            return None
        else:
            return self.parent[idx + 1]

    def save(self):
        # if exist, clean, rec save child
        pickle_save(self.store_path, self)


def find(tree, node_id):
    if tree.data == node_id:
        return tree
    if tree is not None:
        ret = None
        for t in tree.children:
            ret = find(t, node_id)
            if ret is not None:
                break
        return ret


trees = list()


def get_tree(root_id):
    return filter(lambda x: x.node_id == root_id, trees)[0]


def new_project(name, root_type, user_id):
    node_cnt = ProjectNodes.objects.all().count()
    tree = LGTree(node_cnt, root_type)
    trees.append(tree)
    project = Project(name=name, root_id=tree.node_id, user=get_object_or_404(User, user_id),
                      pickle_path=tree.store_path).save()
    root_node = ProjectNodes(project=project, id_on_tree=tree.node_id, node_type=root_type)
    root_node.save()
    return {'project_id': project.id, 'root_id': root_node.id}


def new_node(root_id, node_type):
    project = Project.objects.filter(root_id=root_id).first()
    node_cnt = ProjectNodes.objects.all().count()
    project_node = ProjectNodes(project=project, id_on_tree=node_cnt, node_type=node_type)
    return project_node.id

def delete_node(project_id, id_on_tree):
    # delete from tree in memory
    root_id = Project.objects.get(id=project_id).root_id
    tree = get_tree(root_id)[0]
    tree.children.remove(id_on_tree)
    # delete from db
    node = ProjectNodes.objects.filter(project_id=project_id, id_on_tree=id_on_tree).first().delete()
    return node

def move_node(node_alter, node_connect, ref_type):
    tree = get_tree(node_alter.Project.root_id)[0]
    tree.children.remove(node_alter.id_on_tree)
    return node_join(node_alter, node_connect, ref_type)

def node_join(node_a, node_b, ref_type):
    tree = get_tree(node_a.project.root_id)[0]
    tree_node_a = find(tree, node_a.id_on_tree)
    tree_node_b = find(tree, node_b.id_on_tree)
    if ref_type == 0:
        # a is b's child
        if tree_node_a not in tree_node_b.children:
            tree_node_b.children.append(tree_node_a)
    elif ref_type == 1:
        # a is b's left brother
        if tree_node_a not in tree_node_b.parent.children:
            b_level_nodes = tree_node_b.parent.children
            b_level_nodes.insert(b_level_nodes.index(tree_node_b), tree_node_a)


def ref_valid(node_id_a, node_id_b, ref_type):
    node_a = ProjectNodes.objects.filter(id_on_tree=node_id_a).first()
    node_type_a = node_a.node_type
    node_b = ProjectNodes.objects.filter(id_on_tree=node_id_b).first()
    node_type_b = node_b.node_type
    return node.ref_valid(node_type_a, node_type_b, ref_type), node_a, node_b


if __name__ == '__main__':
    root = LGTree(0, 0)
    for i in range(10):
        root.add_child(LGTree(i, i))
    root.save()
    for child in root.children:
        print(child.data)
    root_restore = pickle_load(root.store_path)
    for child in root_restore.children:
        print(child.data)

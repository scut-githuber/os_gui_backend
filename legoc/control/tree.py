from legoc.util.data import pickle_save, pickle_load


class LGTree(object):
    def __init__(self, node_id, lg_node_id):
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
import xml.etree.ElementTree as et


def travel_xml(root, parent, sibling, level, on_node):
    current_node = on_node(root, parent, sibling)
    blanks = ''
    for _ in range(level):
        blanks += ' '
    print(blanks + 'tag is : %s' % root.tag)
    print(blanks + 'tag.attributes')
    for (k, v) in root.attrib.items():
        print(blanks + '%s: %s' % (k, str(v)))
    print(blanks + 'tag.text: %s' % root.text)
    level += 1
    cur_idx = 0
    last_child = None

    for child_of_root in root:
        last_child = travel_xml(child_of_root, current_node, last_child, level, on_node)
        cur_idx += 1
    return current_node


def travel_xml_file(xml_path, on_node):
    tree = et.ElementTree(file=xml_path)
    root = tree.getroot()
    travel_xml(root, None, None, 0, on_node)

if __name__ == '__main__':
    def empty(node):
        pass
    travel_xml_file('/Users/cwh/coding/python/os-gui-backend/test_data/application.xml', empty)

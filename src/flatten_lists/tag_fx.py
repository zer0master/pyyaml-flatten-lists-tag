#!/usr/bin/env python3
#
import yaml


def tag_handler(loader: yaml.SafeLoader, node: yaml.nodes.SequenceNode):
    ''' Assumes input is multiple lists of lists of dicts, flattened with nested listcomp; result must
        still be converted to compatible object (SequenceNode) in this case:
            [item for inner in outer for item in inner]

        refs:
          tags: &common_tags
            - Key: Department
              Value: Development
            - Key: Division
              Value: Hackers
        usage:
          tags: !FlattenLists
            - *common_tags
            - - Key: Name
                Value: Your Name
              - Key: Created
                Value: 20210806T1827
    '''
    new_node = yaml.nodes.SequenceNode(
        tag='tag:yaml.org,2002:seq',
        value=[item for inner in node.value for item in inner.value])

    return loader.construct_sequence(new_node)

def update_loader():
    ''' Adds custom constructor; should consider more flexible approach so tag handlers can be registered
        by name/module
    '''
    loader = yaml.SafeLoader
    loader.add_constructor('!FlattenLists', tag_handler)
    return loader


# ** entry point (postentially self-test) **
#
if __name__ == '__main__':
    # conditional: handle case where module is run as script

    import  json
    import  os
    import  sys

    if len(sys.argv) < 2 or os.path.exists(sys.argv[1]):
        print('you must supply the name of an existing yaml-formatted file')
        sys.exit(1)

    try:
        with open(sys.argv[1]) as data:
            info = yaml.load(data, Loader=update_loader())

        if info:
            print(json.dumps(info, indent=2))

    except Exception as exc:
        print(str(exc))

#!/usr/bin/env  python3
import  sys

import  unittest

# accomodate application in sibling folder
sys.path.append(r'.')

from    src.flatten_lists   import  tag_fx


class FunctionConstructorTestCase(unittest.TestCase):
    ''' Verifies custom tag is present as constructor key after updating
    '''
    def test_loader_constructor(self):
        loader = tag_fx.update_loader()
        self.assertTrue('!FlattenLists' in loader.yaml_constructors)

class TagHandlerTestCase(unittest.TestCase):
    ''' Verifies custom tag points to expected handler
    '''
    def test_handler_present(self):
        loader = tag_fx.update_loader()
        self.assertTrue(loader.yaml_constructors['!FlattenLists'].__name__ == 'tag_handler')

if __name__ == '__main__':
    unittest.main()

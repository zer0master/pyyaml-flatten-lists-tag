#!/usr/bin/env  python3
import  sys
import  unittest

import  yaml

# accomodate application in sibling folder
sys.path.append(r'.')

from    src.flatten_lists   import  tag_fx


class LoadAndCompareTestCase(unittest.TestCase):
    '''
    '''
    def setUp(self):
        ''' Helpers
        '''
        self.expected = [
            {'Key': 'Dept', 'Value': 'Something'},
            {'Key': 'Division', 'Value': 'Else'},
            {'Key': 'Name', 'Value': 'Bozo'},
            {'Key': 'Age', 'Value': -1}]

        self.content = '''
refs:
  tags: &common
    - Key: Dept
      Value: Something
    - Key: Division
      Value: Else
usage:
  tags: !FlattenLists
    - *common
    - - Key: Name
        Value: Bozo
      - Key: Age
        Value: -1
'''[1:]

    def test_load_success(self):
        ''' Read from known string; since order is guaranteed by list behavior, assertion should pass
        '''
        result = yaml.load(self.content, Loader=tag_fx.update_loader())
        self.assertEqual(result['usage']['tags'], self.expected)


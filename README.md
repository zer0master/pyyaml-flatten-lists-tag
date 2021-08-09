# pyyaml-flatten-lists-tag
This is a small module supporting the !FlattenLists custom tag to render a list-of-lists value as a single list value; it's primary use is in handling the non-native YAML use acase of defining a list of common values (which may be something other than scalars) as an anchor in a configuration, and then needing to add it to a specific list elsewhere.

As an example, a YAML file of the form:
```
refs:
  tags: &common_tags
    - Key: Department
      Value: Development
    - Key: Division
      Value: Hackers

# the !FlattenLists custom tag expects nested lists as shown:
usage:
  tags: !FlattenLists
    - *common_tags
    - - Key: Name
        Value: Your Name
      - Key: Created
        Value: 20210806T1827
```
to yield the following JSON representation:
```
{
  "refs": {
    "tags": [
      {
        "Key": "Department",
        "Value": "Development"
      },
      {
        "Key": "Division",
        "Value": "Hackers"
      }
    ]
  },
  "usage": {
    "tags": [
      {
        "Key": "Department",
        "Value": "Development"
      },
      {
        "Key": "Division",
        "Value": "Hackers"
      },
      {
        "Key": "Name",
        "Value": "Your Name"
      },
      {
        "Key": "Created",
        "Value": "20210806T1827"
      }
    ]
  }
}
```
All that's required is to install the module, import it in the normal fashion, and specify the `update_loader()` function for the optional `Loader` keyword in the `yaml.load()` call. Note that the implementation actually instantiates and augments `yaml.SafeLoader`, preserving the intent of the class.
```
from  flatten_lists   import  tag_fx

# data is a file handle opened in read mode
yaml.load(data, Loader=tag_fx.update_loader())
```

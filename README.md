# pyyaml-flatten-lists-tag

## Background
This is a small module illustrating implementation of a `!FlattenLists` custom YAML tag to render a list-of-lists value as a single list value. Its primary use is in handling the non-native YAML use case of defining a list of common values (which may be something other than scalars) as an anchor in a configuration, then needing to merge it with a specific list elsewhere due to external requirements of the configuration.

As an example, consider a trivial YAML file of the form:
```
refs:
  tags: &common_tags
    - Key: Department
      Value: Development
    - Key: Division
      Value: Hackers

# the !FlattenLists custom tag merges nested lists of the following form:
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

## Installation
*This will be verified Real Soon Now*...

Install the module like any other, import it, and specify the `update_loader()` function for the optional `Loader` keyword in the `yaml.load()` call. Note that the implementation actually instantiates and augments `yaml.SafeLoader`, preserving the intent of the class.
```
from  flatten_lists   import  tag_fx

# data is a file handle opened in read mode
yaml.load(data, Loader=tag_fx.update_loader())
```

## Build and Test
A `Makefile` (gasp) controls operations; upload to a designated PyPi repo is not yet added; `make help` shows valid targets (which are so obvious you should be insulted).

`unittest` is used out of laziness (and a desire to keep dependencies and setup minimal), and the build target is the default.



# pyyaml-flatten-lists-tag

## Background
This is a small module illustrating implementation of a `!FlattenLists` custom YAML tag, which renders a list-of-lists value as a single list. The most likely scenario addresses the non-native YAML use case of merging a list of common values from an anchor definition (which can be non-scalars) elsewhere in the configuration due to external requirements of the consuming script or application.

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
yielding this JSON representation:
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

Install the module like any other, import it, and specify the `update_loader()` function for the optional `Loader` keyword in the `yaml.load()` call. Since the implementation instantiates and augments `yaml.SafeLoader`, intent is preserved.
```
from  flatten_lists   import  tag_fx

# data is a file handle opened in read mode
yaml.load(data, Loader=tag_fx.update_loader())
```

## Build and Test
A `Makefile` (gasp) controls operations; upload to a designated PyPi repo is not yet added; `make help` shows valid targets (so obvious you might feel insulted lol).

`unittest` is used out of laziness (and a desire to keep dependencies and setup minimal), and the build target is the default.

## Future
These are slated for implementation:
* upload (with a custom target like a self-hosted PyPi or Artifactory host)
* shakedown of the metadata (likely suspect as of this writing

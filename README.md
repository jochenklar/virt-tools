virt-tools
==========

A small collection of utilities for libvirt to complement tools like `virt-tool` and `virt-clone`.

Tools
-----

`virt-dhcpd`: Get the dhcpd configuration a given domain (i.e. virtual machine).

`virt-mac`: Get the MAC address of a given domain (i.e. virtual machine).

`virt-vnc`: Get the vnc port of a given domain (i.e. virtual machine).

`virt-xml`: Get the full xml description of a given domain (i.e. virtual machine).

Installation
------------

1. Clone the repository.
2. Set `PATH` and `PYTHONPATH` in `.bashrc`:
```
export PATH=/path/to/virt-tools/bin:$PATH
export PYTHONPATH=/path/to/virt-tools/lib:$PYTHONPATH
```

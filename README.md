# BeaconOS
This is the source code of BeaconOS
## Introduction To This Project
  BeaconOS is a operating system that is a **Embedded Linux Project** that is based on Buildroot(www.buildroot.org)
  This project is purely made with Python3.10.0(www.python.org)
## How to Load the System?
  This file sctructure of BeaconOS is mingrated from BASH, all of the system files are stored under the following directory: `/etc/profile.d`
  - All of your script file will be stored under: `/etc/profile.d/scripts`.
  - Text File will be stored under: `/etc/profile.d/tpa` or `/etc/profile.d/tpb`, `/etc/profile.d/tpc`, `/etc/profile.d/others`
  - If the OS did not load after the boot and Buildroot ask for your username and password, use the following:
            - UserName: root
            - No password
  After your login action, the OS should load. Otherwise, enter the following command: `cd /etc/profile.d && python3 New_MShell.py`
## Further Support and Help
  Please visit www.beaconos.org and refer to user instructions and quick start hand book. For bug reports or official build(regardless version) that downloaded from the website, please email: ***developer@beaconos.org***
 ## Contribute to This Project
  The memeber of BeaconOS team are looking forward to new member of to our team, please fill out this form and we will contact you as soon as possible: https://forms.office.com/r/7qaKpUy7Zf
## Credits
  - BeaconOS had embedded the project: pypa/pip. All of the usages are directed under the MIT License of PIP. 
  - Link to pypa/pip: https://github.com/pypa/pip.git

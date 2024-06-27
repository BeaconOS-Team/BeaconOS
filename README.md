# BeaconOS
This is the source code of BeaconOS


## **IMPORTANT STATEMENT BY THE BOARD OF DIRECTORS**
The BeaconOS Team noticed with deep regret that the newly founded website, known as GitCode, made by Huawei and CSDN is starting to clone many GitHub repositories without proper attribution or notification to their respective developers. In accordance with Chapter II (Article 3) and Chapter II (Article 6) of the Constitution of the BeaconOS Team, the Board of Directors issued this statement to notify the public regarding certain actions taken by the BeaocnOS Team regarding this event. 
The BeaconOS Team always sees the protection of intellectual properties and copyrights as our utmost priority while the action taken by GitCode is not tolerable, to say the least. Since the BeaconOS Project is copyrighted and protected under the United States Code: Copyright Office, 17 U.S.C. §§ 201-216 (1958), the BeaconOS Team decided to apply further protection to this project from foreign threats by amending the BeaconOS Software License. 
The amended license included an additional clause that temporarily disabled the redistribution of the BeaconOS Project without a properly written submission to the BeaconOS Team and its approval. The Board would emphasize that although this change affected all users of the BeaconOS Project and introduced more obstacles, it is the action that they are forced to take. The Board sincerely apologizes to all users regarding this change and the inconvenience it brought. The Board urges all members of the community to take actions regarding this newly amended license and report to the BeaconOS Team with any suspicions of the violation of this license. 


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
  .After your login action, the OS should load. Otherwise, enter the following command: `cd /etc/profile.d && python3 MShell4.py`
## Further Support and Help
  Please visit www.beaconos.org and refer to user instructions and quick start hand book. For bug reports or official build(regardless version) that downloaded from the website, please email: ***developer@beaconos.org***
 ## Contribute to This Project
  The memeber of BeaconOS team are looking forward to new member of to our team, please fill out this form and we will contact you as soon as possible: https://forms.office.com/r/7qaKpUy7Zf
## Credits
  - BeaconOS had embedded the project: pypa/pip. All of the usages are directed under the MIT License of PIP. 
  - Link to pypa/pip: https://github.com/pypa/pip.git

#!/bin/bash

git clone https://github.com/buildroot/buildroot.git      #get buildroot
git clone https://github.com/BeaconOS-Team/BeaconOS.git   #get BeaconOS Source Codes
git clone https://github.com/pypa/pip.git                 #get pip

cp -r pip ~/buildroot/system/skeleton/etc/profile.d
cp -r BeaconOS/Source\ Codes/Beacon1.6.2 ~/buildroot/system/skeleton/etc/profile.d

cd buildroot
make pc_x86_64_efi_defconfig
make menuconfig

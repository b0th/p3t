#!/bin/bash
   
pkg=(pacman apt dnf yum zipper)
c=False
for x in ${pkg[*]}; do
    if [ $(which $x) ];then
    sudo $x install python3 python3-pip
    c=True
    fi
done

if [ $c != True ];then exit;fi

echo -e "\n\e[32mInstall requirements ?\e[0m [Y/n]"
read ask

if [ $ask == "Y" ] || [ $ask == "y" ];then
pip3 install -r requirements.txt
fi
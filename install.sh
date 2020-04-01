#Looking for default packages manager

CHECK_APT=`which apt`
CHECK_PACMAN=`which pacman`
CHECK_DNF=`which dnf`
CHECK_YUM=`which yum`
CHECK_ZYPPER=`which zypper`

#Install python3 & pip3 in function of packages mananger

echo -e 'Looking for your default packages mananger\n' ; sleep 2

CHECK_ERROR=True

if [ -z $CHECK_APT ] ; then
CHECK_ERROR=False
else
sudo apt install python3 && sudo apt install python3-pip
fi
if [ -z $CHECK_PACMAN ] ; then
CHECK_ERROR=False
else
sudo pacman install python3 && sudo pacman install python3-pip
fi
if [ -z $CHECK_DNF ] ; then
CHECK_ERROR=False
else
sudo dnf install python3 && sudo dnf install python3-pip
fi
if [ -z $CHECK_YUM ] ; then
CHECK_ERROR=False
else
sudo yum install python3 && sudo yum install python3-pip
fi
if [ -z $CHECK_ZYPPER ] ; then
CHECK_ERROR=False
else
sudo zypper install python3 && sudo zypper install python3-pip
fi

if [ $CHECK_ERROR == True ] ; then
echo -e '\nError with packages manager , please check your packages manager'
echo -e 'If you dont have packages manager download one like apt or pacman ..\n'
exit
fi

echo ''
echo Do you want to install requirements ? [Y/n]
read YES_OR_NO

if [ $YES_OR_NO == 'Y' ] || [ $YES_OR_NO == 'y' ] ; then
pip3 install -r requirements.txt
else
exit
fi

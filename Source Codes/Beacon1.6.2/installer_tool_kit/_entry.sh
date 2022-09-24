#SHELL!!!!!!!!!!!!!!!!!!!
$NAME=sh usbname.sh

if dd if=/dev/$NAME of=/dev/sda bs=1M; then
    echo "GOOD"
else
    echo "BAD"
fi
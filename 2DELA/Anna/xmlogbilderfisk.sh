#!/bin/bash
filename="mycopy.sh"
tempfil="liste.txt"
ls -1 | grep xml > $tempfil
sed -i 's/.xml/.png/g' $tempfil
echo "#!/bin/bash" >> $filename
chmod 777 $filename
awk '{print"cp ../bilder/"$1" ."}' $tempfil > $filename
sh $filename
#cat $filename
rm -rf $filename
rm -rf $tempfil
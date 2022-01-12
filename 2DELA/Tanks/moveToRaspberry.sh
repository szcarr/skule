#Ikkje tenk paa denne
cd ..
rm -f Tanks.zip
zip -r Tanks.zip Tanks
sudo scp Tanks.zip pi@192.168.1.144:/home/pi/ 
#Ikkje tenk paa denne
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ..
cd ..

USER="pi"
IP="192.168.1.170"
#USER="pi"
#IP="192.168.1.175"

rm -rf Matrix.zip
zip -r Matrix.zip Matrix
scp Matrix.zip $USER@$IP:/home/$USER/
rm -rf Matrix.zip
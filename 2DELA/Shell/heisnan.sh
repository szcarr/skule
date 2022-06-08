search_dir="$(pwd)/"

pycache="$(find *)"

for f in $pycache
do
    if [ "${file}" = "${PROJECTDIR}TextUIstart.sh" ]
    echo $f
done
#for entry in $search_dir*
#do
#  echo "$entry"
#done
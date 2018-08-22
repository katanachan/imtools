#!bin/bash
if [ "$#" -lt 1 ]
then
    echo "Usage: traintestsplit.sh <.format of data> <pathtodata/>"
    exit 11
fi
echo $1
echo $2
ls | grep "$1" > all.txt
touch train.txt
if [ -z "$1" ]
then
    awk '$0="$2"$0' all.txt > train.txt
else
    mv all.txt train.txt
fi
cat train.txt | shuf > all.txt
spl=`cat train.txt | wc -l`
sp=$((spl * 4 / 5))
echo $sp 
sed -n -e "$sp,$spl p" -e "$spl q" all.txt  > test.txt
sed -e "$sp,$spl d" all.txt > train.txt
mv train.txt ../
mv test.txt ../

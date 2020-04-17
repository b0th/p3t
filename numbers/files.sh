#It just creates 11 files
for x in {0..10} ; do
touch $x.txt
done

touch :.txt
read -p "Enter main name" n
c=1
for f in $(cat < "links.txt"); do
	echo $f
	echo $n"$c".html
	curl -s $f >$n"$c".html
	html2text $n"$c".html >>everything.txt
	rm $n"$c".html
	((c++))
done

python Cleaner.py
cupsfilter output.txt>output.pdf
rm output.txt
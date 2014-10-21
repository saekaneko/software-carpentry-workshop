echo "Cleaning up files before downloading..." #display what we're doing

rm *.txt #clean up before downloading files 
rm *.tmp
rm *.csv


echo downloading data... #quotation marks are not necessary
curl https://github.com/zonca/swcarpentry-workshop-pandas/blob/master/rawdata/rawdata.zip?raw=true -o rawdata.zip -L

echo unzipping data...
unzip rawdata.zip

rm rawdata.zip #dont need this anymore
rm *.tmp #these files are useless

for f in *.txt
do
	mv $f ${f/txt/csv} #indentation is not necessary but helps easy reading
done

echo Available csv files
ls *.csv
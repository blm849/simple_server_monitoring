python $1/dfmon.py 60 > $1/prod1mon.txt
python $1/vmstatmon.py >> $1/prod1mon.txt
python $1/processmon.py apache >> $1/prod1mon.txt
python $1/pingtest.py $1/pingtable.txt >> $1/prod1mon.txt
detect_barcode2_all.py 
 working good, linked with database, tells the elapsed time
but make sure the books are issued by entering the following commands in the mysql


insert into e(id,name,bookid,bookname,issuedate,returndate,status)values("14BEC0***","652837659","9781904994862",                                                                     "dip","22/07/2017","15/08/2017","1");
insert into e(id,name,bookid,bookname,issuedate,returndate,status)values("14BEC0***","qwertyu","005150024163",                                                                     "dip","22/12/2017","15/01/2018","1");



set the time in order to mmake sure that fine is working good
sudo date -s"Mon aug 12 20:14:11 UTC 2014"

*********************************************************************************************

detect_working.py

working good
images/download.jpg
images/barcode_01.jpg# capstone_barcode

*************************************************************************************

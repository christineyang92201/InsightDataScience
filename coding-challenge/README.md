Packages I used: re, sys, networkx, matplotlib
1. Missing Value Record
Definition : records without target or actor.
There are 39 records with missing value,Compared with 1792 full records,it is a small number, so I just ignore these records for analysis.

2. Idea
Main:
Transform time to seconds base, day*24*3600 + hour*3600 + minute*3600 + seconds. Note: All records collected from the same year, same month, so we don't need to care them
After transformation, we can compare time for any two records.
We can get maximum time in important records which used to draw graph or say within the latest 60 seconds at this time point. 

Issue:
How to identify the arriving record is in order or out of order? If the transform time basing on seconds for the arriving record is bigger than maximum tranform time in storage, then
the arriving record is out of order, otherwise, in order. 

Updating useful records for now. Each time we recerive a new record, we should update our useful records. If it is in order, add it into useful records.  And it's transform time is maximum time now, delete records whose 
transform time is smaller than it for more than 60 minutes. If it is out of order, then compare with its tranform time with existing maximum time, if it is smaller than it for more than 60 seconds, 
ignore this record, if it is smaller than maximum time within 60 seconds, then add it into useful records.  

Two important output dictionary:Two dictionaries stores records within the latest 60 seconds at this time point. 
One is timeName, which with transform time basing on seconds for key, and a two length list which contains the target and actor for this record for 
values. This dictionary contains relationships. 
The other one with Name whatever target or actor for key, and corresponding connection times.For example, Yo-Ming's value is 3 means that, for now, Yo-Mining is connecting with 3 
different people. 

How to deal with such condition? The useful records contains the similar record with arriving one, who has same target and actor. After receive a new record, we do such job, identifing if the target to 
actor relation already exists in useful records, if no, then do normal following steps, if yes, then compare the transform time of arriving record with one of similar existing record. If it is bigger, delete existing record, if it is ignore new records. 


Run the program with the following in the command line
$ ./run.sh

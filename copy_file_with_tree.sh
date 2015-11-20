#!/bin/bash
dest_dir="/gfs2/mv/csupload/contents/20151102"
addr="192.168.20.237"
for line in `cat find.txt`
do	
	create_dir=`echo $line|cut -d '/' -f 7,8`
	ssh $addr   "/bin/mkdir -p ${dest_dir}/${create_dir}"
	scp $line $addr:${dest_dir}/${create_dir}/
	sleep 1
done

import os
import sys
import glob
import time
import re
import csv
def main(name):
    f=open(name,'r')
    file=open("./out_temp_ts.txt","w+")
    file.write("Temp"+"  "+"Timestamp\n")
    lines=f.readlines()
    for line in lines:
    	
    	
        if line.__contains__('[Khealthd') and line.__contains__('battery l='):
            list=(line.split('['))
            a=list[-1].split(' ')
            temp=a[4]
            b=list[10].split(']')
            time=b[0]

            #if line[1]==' ':
            try:
                file.write(temp+"  "+time+"\n")
            except IndexError:
                pass
            
def txt_parse(path,file):
    temp=[]
    f=open((path+"//"+file),'r')
    lines=f.readlines()
    for line in lines:
        if line.__contains__('Temperature'):
            line=line.split(' ')
            temp.append(int(line[-1]))
            
    if len(temp)>0:
        temp.sort()
        return temp[0]
    else:
        return -1
    
    
def rwr_parse(path):
    txt_files=glob.glob("*.abc")
    print len(txt_files)
    txt_files.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
    f=open("./rwr_temp_fileno.txt","w+")
    for i in range(len(txt_files)):
        p=txt_parse(path,txt_files[i])
        if p==-1:
            pass
        else:
            a=txt_files[i].split('.')
            rwr_name=a[0]
            rwr_file=path+"//"+rwr_name+".rwr"
            if p<127:
                f.write(rwr_name+"   Temp="+str(p)+"   "+time.ctime(os.path.getctime(rwr_file))+"\n")
            else:
                p=p-256
                f.write(rwr_name+"   Temp="+str(p)+"   "+time.ctime(os.path.getctime(rwr_file))+"\n")


def txt_parse_H8(path,file):
	f=open(path+"\\"+file,'r')
	lines=f.readlines()
	out.write(lines[10]+'\n')

def parse_H8(path):
	os.chdir(path)
	txt_files=glob.glob("*.txt")
	txt_files.sort(key=lambda f: int(filter(str.isdigit, f)))
	out=open("./out.txt","w+")
	for i in range(len(txt_files)):
		txt_parse_H8(path,txt_files[i])

	out.close()
    
#main("C:\\Users\\39220\\Desktop\\terminal_rahul.log")
#rwr_parse(path)
#parse_H8("C:/Qual_Reports/UFS/swift/Swift_1212/256_A0/run4")
def parse_csv():
	out=open("./out.txt","w+")
	start_time=list()
	end_time=list()
	counter=0
	with open("C:\\Users/39220\\Desktop/5d358bd96764fe21e4b14767_rwr (1).csv", 'rb') as f:
		reader = csv.reader(f, delimiter=';')
		for row in reader:
			if counter>0:
				txt=row[0].split(',')
				if counter&1:
					start_time.append(int(txt[2].replace('"','')))
				else:
					end_time.append(int(txt[2].replace('"','')))
			counter+=1

	f.close()

	#print start_time
	#print end_time
	for i in range(len(end_time)):
		out.write (str((end_time[i]-start_time[i])/1000.0)+'\n')

	out.close()



parse_csv()
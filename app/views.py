from django.shortcuts import render

# Create your views here.
from app.models import *
import csv
from django.http import HttpResponse

def insert_bank(self):
    with open('C:\\Users\\Sravani\\Dropbox\\My PC (LAPTOP-9FESU5D0)\\Desktop\\djangoprojects\\sravani\\Scripts\\csv_files\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO) #reader funtion reads all the data in the file and return the Iterable Object of the Data
        for i in IOD:
            bn=i[0].strip() #strip will remove the unwanted spaces
            BO=Bank(bank_name=bn)
            BO.save()
    return HttpResponse('Bank data inserted Successfully')



def insert_branch(self):
    with open('C:\\Users\\Sravani\\Dropbox\\My PC (LAPTOP-9FESU5D0)\\Desktop\\djangoprojects\\sravani\\Scripts\\csv_files\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD) #next method will skip the first row becoz it contains the column names
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                br=i[2]
                ad=i[3]
                con=i[4]
                ci=i[5]
                dis=i[6]
                st=i[7]
                BRNO=Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contact=con,city=ci,district=dis,state=st)
                BRNO.save()
    return HttpResponse('Branch data inserted successfully')
import csv

def write_into_csv(info_list):
    with open('student_info.csv','w+',newline") as csv_files
              writer=csv.writer(csv_file)
              writer.writerow(info_list)


condition=True
while(condition):
    student_info=input("enter student info in the following format(Name age contact_number email_ID):")
    print("Entered info"+(student_info))

    student_info_list=student_info.split(' ')
    print("Entered split up info is:"+str(student_info_list))

    write_into_csv(student_info_list)
    
          
    condition_check=input("enter (yes/no) if you want to enter info for another student")
    if condition_check=="yes":
        condition=True
    elif condition_check=="no":
        condition=False 

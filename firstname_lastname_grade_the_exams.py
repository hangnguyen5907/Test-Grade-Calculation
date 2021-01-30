import os.path
import numpy as np
filename = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
Counter_line = 0  
answer_key= "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D" 
chuoi_dapan=answer_key.split(',')
try:
  file_path=filename+".txt"
  f = open(filename+".txt", "r")
  Content = f.read() 
  CoList = Content.split("\n")   
  Counter_valid = 0
  Counter_invalid =0
  file = open("ketqua_"+filename+".txt", "w") 
  diem_tongket= []
  inval_lines_1=[]
  inval_lines_2=[]
  for i in CoList:    
    if i: 
        diem=0
        Counter_comma = 0
        for k in i: 
          if k == ',': 
            Counter_comma += 1
        Counter_line += 1
        if Counter_comma ==25:
          name=i.split(",")[0]
          if len(name)==9:
            if name[0]=="N" and name[1:9].isnumeric()  :
              chuoi_hocsinhtraloi=i.split(',')
              chuoi_traloi=chuoi_hocsinhtraloi[1:]
              for c in range(0,len(chuoi_dapan)):
                if chuoi_traloi[c]==chuoi_dapan[c]:
                   diem=diem+4
                elif chuoi_traloi[c]=='':
                   diem=diem+0
                else:
                   diem=diem-1
              print(name, ', ', diem)
              vaodiem=str(str(name)+', '+str(diem))
              file.write(vaodiem) 
              file.write("\n")
              diem_tongket.append(diem)     
              Counter_valid +=1
            else:
              Counter_invalid +=1
              inval_lines_2.append(i)              
          else:
            Counter_invalid +=1
            inval_lines_2.append(i)
        else:
          Counter_invalid +=1
          inval_lines_1.append(i)
  file.close() 
  print("Successfully opened ",str(file_path))
  print('The average score: ', np.mean(diem_tongket))
  print('The highest score: ', np.max(diem_tongket))
  print('The lowest score: ', np.min(diem_tongket))
  print('The range of scores: ', np.max(diem_tongket)-np.min(diem_tongket))
  print('The median value: ', np.median(diem_tongket))  
  print("**** ANALYZING ****") 
  if Counter_invalid==0:
    print('No errors found!')
    print('**** REPORT ****')
    print("Total valid lines of data: ",Counter_valid )
    print("Total invalid lines of data: ",Counter_invalid )
  else:
    for a in range(0,len(inval_lines_1)):
      print('Invalid line of data: does not contain exactly 26 values')
      print(inval_lines_1[a])
    for b in range(0,len(inval_lines_2)):
      print('Invalid line of data: N# is invalid')
      print(inval_lines_2[b])
    print('**** REPORT ****')
    print("Total valid lines of data: ",Counter_valid )
    print("Total invalid lines of data: ",Counter_invalid )
except:
  print("Sorry, I can't find this filename")

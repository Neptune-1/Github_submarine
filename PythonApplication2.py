import cv2
import numpy as np
cd_1=['0', '0', '0']
cd_2=['0', '0', '0']
cd_3=['0', '0', '0']
file_stl='new.stl'
file_im=r'C:\Users\allex\Pictures\2.jpg'
op_stl=open(file_stl, 'w')
op_im=cv2.imread(file_im)

gray = cv2.cvtColor(op_im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
print(blur.shape[1])
#cv2.imshow("jj",gray)
#cv2.waitKey(1000)
x=0
y=0
file='STL_project-1.stl'
o_1="\n\t"
o_2="\n\t\t"
o_3="\n\t\t\t"
op_stl.write("solid")
def face_file_stl(cd_1, cd_2, cd_3):
	op_stl.write(o_1+"facet normal 0 0 0")
	op_stl.write(o_2 + "outer loop")
	op_stl.write(o_3 + "vertex " + "  ".join(cd_1))
	op_stl.write(o_3 + "vertex " + " ".join(cd_2))
	op_stl.write(o_3 + "vertex " + " ".join(cd_3))
	op_stl.write(o_2 + "endloop \n\tendfacet")

#making the first triangls  for base
for i in range(blur.shape[1]-1):
      cd_1=[str(i),"0","0"]
      cd_3=[str(i+1),str(blur.shape[0]-1),"0"]
      cd_2=[str(i),str(blur.shape[0]-1),"0"]
      face_file_stl(cd_1, cd_2, cd_3)
#making the second triangls  for base      
for i in range(blur.shape[1]-1):
      cd_1=[str(i+1),str(blur.shape[0]-1),"0"]
      cd_3=[str(i),"0","0"]
      cd_2=[str(i+1),"0","0"]
      face_file_stl(cd_1, cd_2, cd_3)
#base has done

for i in range(blur.shape[1]):
        if i%30==0:
            print(i)
        for k in range(blur.shape[0]-1):#making the first triangls  for relief
            if i!=blur.shape[1]-1:
                    try:
                        
                        cd_1=[str(i),     str(k),   str(blur[k, i])   ]
                        cd_2=[str(i + 1), str(k),   str(blur[k, i+1]) ]
                        cd_3=[str(i+1),   str(k+1), str(blur[k+1,i+1])] 
                     
                    except:
                        print('er')
                    face_file_stl(cd_1, cd_2, cd_3)
			        #for j in range(blur.shape[1]-1):#making the second triangls  for relief
                    try:
                        cd_1=[str(i),  str(k),   str(blur[k, i])    ]
                        cd_2=[str(i+1),str(k+1), str(blur[k+1, i+1])]
                        cd_3=[str(i),  str(k+1), str(blur[k+1,i])   ]   
                    except:
                        print('er')
                    face_file_stl(cd_1, cd_2, cd_3)
#relief has done

#making the first triangls  for right side        
for i in range(blur.shape[1]):
     if i!=blur.shape[1]-1:
      try:
            cd_1=[str(i),str(blur.shape[0]-1),"0"]
            cd_3=[str(i+1),str(blur.shape[0]-1),str(blur[blur.shape[0]-1, i+1])]
            cd_2=[str(i),str(blur.shape[0]-1),str(blur[blur.shape[0]-1, i])]
            
      except:
            print("er")
      face_file_stl(cd_1, cd_2, cd_3)
      
#making the second triangls  for right side     
      try:
            cd_1=[str(i),str(blur.shape[0]-1),"0"]
            cd_3=[str(i+1),str(blur.shape[0]-1),"0"]
            cd_2=[str(i+1),str(blur.shape[0]-1),str(blur[blur.shape[0]-1, i+1])]
      except:
            print("er")
      face_file_stl(cd_1, cd_2, cd_3)

     if i!=blur.shape[1]-1:
      try:
            cd_1=[str(i),'0',"0"]
            cd_2=[str(i+1),'0',str(blur[0, i+1])]
            cd_3=[str(i),'0',str(blur[0, i])]
            
      except:
            print("er")
      face_file_stl(cd_1, cd_2, cd_3)
      
#making the second triangls  for right side     
      try:
            cd_1=[str(i),'0',"0"]
            cd_2=[str(i+1),'0',"0"]
            cd_3=[str(i+1),'0',str(blur[0, i+1])]
      except:
            print("er")
      face_file_stl(cd_1, cd_2, cd_3)
#gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
for i in range(blur.shape[0]):
   if i!=blur.shape[0]-1:
      try:
            cd_1=['0',str(i),"0"]
            cd_3=['0',str(i+1),str(blur[ i+1,0])]
            cd_2=['0',str(i),str(blur[i,0])]
            
      except:
            print("er")
      face_file_stl(cd_1, cd_2, cd_3)
      
#making the second triangls  for right side     
      try:
            cd_1=['0',str(i),"0"]
            cd_3=['0',str(i+1),"0"]
            cd_2=['0',str(i+1),str(blur[i+1,0])]
      except:
            print("er")
      face_file_stl(cd_1, cd_2, cd_3)
   
      try:
            cd_2=[str(blur.shape[1]-1),str(i),"0"]
            cd_3=[str(blur.shape[1]-1),str(i+1),str(blur[ i+1,blur.shape[1]-1])]
            cd_1=[str(blur.shape[1]-1),str(i),str(blur[i,blur.shape[1]-1])]
           
      except:
            print("er")
      face_file_stl(cd_1, cd_2, cd_3)
      
#making the second triangls  for right side     
      try:
            cd_2=[str(blur.shape[1]-1),str(i),"0"]
            cd_3=[str(blur.shape[1]-1),str(i+1),"0"]
            cd_1=[str(blur.shape[1]-1),str(i+1),str(blur[i+1,blur.shape[1]-1])]
      except:
            print("er")

      face_file_stl(cd_1, cd_2, cd_3)

op_stl.write("\nendsolid" )
op_stl.close()
    
print('end')
                  




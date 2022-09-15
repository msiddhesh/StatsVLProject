mean.py



           
        
        
    
        
        

--------------------------------------
mean.py - vd

#We are find out the mean for discrete data
TOD=int(input("Please tell us the data-type and if your data has frequency more than 1 put 1 and if your data has frequency exactly 1 than put 0 : "))

while(TOD!=1 and TOD!=0):
    if(TOD!=1 and TOD!=0):
        print(" There is an error,Please give us values as 1 or 0")
        TOD=int(input('There is an error,Please tell us the data-type and if your data has frequency more than 1 put 1 and if your data has frequency exactly 1 than put 0 :'))
    else:
        break
D1=input("please put the data-values :"  )

D2=[] 
while(D1!="."):
    if(D1!="."):
        D2.append(float(D1))
        D1=(input('Plesase Put the data-value: '))
    else:
        break

        
if(TOD==1):
    i=0
    print('for data-value',D2[i])
    F1=input("please put the Freq-values of data value :"  )

    F2=[] 
    while(F1!="."):
        i=i+1
        if(F1!="."):
            F2.append(float(F1))
            if(i<len(D2)):
                print('for data-value',D2[i])
            F1=(input('Plesase Put the Freq-value :' ))
            
            
        else:
            break
    
    while(len(F2)!=len(D2)):
        if(len(F2)!=len(D2)):
            print('there is a problem with your data or frequncy.please re-enter the values...')
            D1=input("please put the data-values :"  )

            D2=[] 
            while(D1!="."):
                if(D1!="."):
                    D2.append(float(D1))
                    D1=(input('Plesase Put the data-value: '))
                else:
                    break
            i=0
            print('for data-value',D2[i])
            F1=input("please put the Freq-values of data value :"  )

            F2=[] 
            while(F1!="."):
                i=i+1
                if(F1!="."):
                    F2.append(float(F1))
                    if(i<len(D2)):
                        print('for data-value',D2[i])
                    F1=(input('Plesase Put the Freq-value :' ))
                    
                    
                else:
                    break
            
        else:
            break
    Tot_L=[]
    TOt_Freq=0
    for i in range(len(D2)):
        L=D2[i]*F2[i]
        Tot_L.append(L)
        TOt_Freq=TOt_Freq+F2[i]
    Total=0   
    for k in range(len(Tot_L)):
        Total=Total+Tot_L[k]
            
        
    mean=Total/TOt_Freq       
    print('mean of your data is :', mean)
elif(TOD==0):
    Total=0
    for i in range(len(D2)):
        Total=Total+D2[i]
    mean=Total/len(D2)

    print('mean of your data is :',mean) 

           
        
        
    
        
        

 -----------------

median.py

#Here we are find out the median of the data:
TOD=int(input("Please tell us the data-type and if your data has frequency more than 1 put 1 and if your data has frequency exactly 1 than put 0 : "))

while(TOD!=1 and TOD!=0):
    if(TOD!=1 and TOD!=0):
        print(" There is an error,Please give us values as 1 or 0")
        TOD=int(input('There is an error,Please tell us the data-type and if your data has frequency more than 1 put 1 and if your data has frequency exactly 1 than put 0 :'))
    else:
        break
D1=float(input("please put the data-values :"  ))

D2=[] 
while(D1!="."):
    if(D1!="."):
        D2.append(float(D1))
        D1=(input('Plesase Put the data-value: '))
    else:
        break
D2.sort()  
n=len(D2)
if(TOD==0):
    if(len(D2)%2==0):
        a=int(n/2)
        b=int((n+2)/2)
        c=D2[(a-1)]
        d=D2[(b-1)]
        median=(c+d)/2
        
    else:
        c=int((n+1)/2)
        median=D2[(c-1)]
    print('Median of your data is :',median)
        
    print(D2)  
elif(TOD==1):
   i=0
   print('for data-value',D2[i])
   F1=input("please put the Freq-values of data value :"  )

   F2=[] 
   while(F1!="."):
       i=i+1
       if(F1!="."):
           F2.append(int(F1))
           if(i<len(D2)):
               print('for data-value',D2[i])
           F1=(input('Plesase Put the Freq-value :' ))
           
           
       else:
           break
   D3=[]
   for i in range(len(F2)):
       for j in range((F2[i])):
           D3.append(D2[i])
   n=len(D3)
   D3.sort()       
   if(len(D3)%2==0):
       a=int(n/2)
       b=int((n+2)/2)
       c=D3[(a-1)]
       d=D3[(b-1)]
       median=(c+d)/2
       
   else:
       c=int((n+1)/2)
       median=D3[(c-1)]
   print('Median of your data is :',median)
   print(D3)


-----------
mode.py

#Here we find out the Mode of the Data :
D1=input("please put the data-values :"  )

D2=[] 
while(D1!="."):
    if(D1!="."):
        D2.append(float(D1))
        D1=(input('Plesase Put the data-value: '))
    else:
        break
H=0
i=0
print('for data-value',D2[i])
F1=input("please put the Freq-values of data value :"  )

F2=[] 
while(F1!="."):
    i=i+1
    if(F1!="."):
        F2.append(float(F1))
        if(int(F1)>H):
            H=int(F1)
            if(i<len(D2)):
                mode=D2[i]
           
        if(i<len(D2)):
            print('for data-value',D2[i])
        F1=(input('Plesase Put the Freq-value :' ))
            
            
    else:
        break
print("Mode of your given data is : ",mode)


--------



	
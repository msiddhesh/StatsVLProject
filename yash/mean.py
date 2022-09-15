
#We are find out the mean for discrete data
TOD=int(input("Please tell us the data-type and if your data has frequency more than 1 put 1 and if your data has frequency exactly 1 than put 0 : "))

while(TOD!=1 and TOD!=0):
    if(TOD!=1 and TOD!=0):
        print(" There is an error,Please give us values as 1 or 0")
        TOD=int(input('There is an error,Please tell us the data-type and if your data has frequency more than 1 put 1 and if your data has frequency exactly 1 than put 0 :'))
    else:
        break
D1=input("please put the data-values with comma(','):  ").split(',') 
D2=[]  
for i in range (len(D1)):
    D2.append(int(D1[i]))
        
if(TOD==1):
    F1=input("please put the freq-values of respective data_values with comma(','):  ").split(',') 
    F2=[]
    for j in range (len(F1)):
        F2.append(int(F1[j]))
    
    while(len(F2)!=len(D2)):
        if(len(F2)!=len(D2)):
            print('there is a problem with your data or frequncy.please re-enter the values...')
            D1=input("please put the data-values with comma(','):  ").split(',') 
            D2=[]  
            for i in range (len(D1)):
                D2.append(int(D1[i]))
            F1=input("please put the freq-values of respective data_values with comma(','):  ").split(',') 
            F2=[]
            for j in range (len(F1)):
                F2.append(int(F1[j]))    
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
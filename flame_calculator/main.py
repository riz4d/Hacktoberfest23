#This was one of my earliest projects.Looking back there were easier methods to do this.

#First Self made project
#Completed
#Natural method
#Ongoing Updates
#Bugs fixed : 5

def flame():      

    name1=str(input("Enter your name: ").replace(" ",""))
    if name1=="":
        print("Dont you have name?")
    
    else:
        name2=str(input("Enter your crush's name: ").replace(" ",""))
    
        if name2=="":
            print("Are you still single?")
        else:    
        #Converting String to list
    
            no_of_letters_1=len(name1) 
            list1=[]
            x=0
    
            while x<no_of_letters_1:       
                element=name1[x]
                x=x+1
                list1.append(element)
    
    
            #print(list1)    
    
            no_of_letters_2=len(name2)                  
            list2=[]
            x=0
                                         
            while x<no_of_letters_2:
               element=name2[x]
               x=x+1
               list2.append(element)
    
    
            #print(list2) 
     
    
        #Removing Common Elements From Lists
    
            x=0
            z=len(list1)
            while x<z:
        
                y=list1[x]
                f=y.upper()
                if y in list2 or f in list2:
                    list1.remove(y)
                    list2.remove(y)       
                    z=len(list1)
    
            
                else:
                    x=x+1  
                    z=len(list1) 
            
            #print(list1)        
            #print(list2)
    
    
        #Total Number
       
            a=len(list1)
            b=len(list2)
            total_no_of_letters=a+b
    
            #print(total_no_of_letters)
    
        
        #Choosing From FLAME
    
            flame=['F','L','A','M','E']
            if total_no_of_letters>5:
                p=total_no_of_letters
                n=p
                while n>4:
                   p=p -6
                   n=0
                   n+=p              
                o=flame[n]
            else:
               q=total_no_of_letters -1
               o=flame[q]  
    
    
            #print(o) 
    
        #Finale
      
            if o=='F':
                print("Your Love will Fail")
            elif     o=='L':
                print("You will be Lovers")
            elif o=='A':
                print("It's just an Affection")
            elif o=='M':
                print("Happy Married Life")   
            elif o=='E':        
                print("You are Enemies")
    
flame()

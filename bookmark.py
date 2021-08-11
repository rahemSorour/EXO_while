#bookmark for web site
#empty list
myweb=[]

#maximum 
max=3

while max>0:
    w=input("write yr fav website")
    #add the liste 
    myweb.append(f"http// {w.lower().strip()}")
    
    max-=1
    #print the liste
    print(myweb)
    print(f"the website add , rest {max} place")
else:
    print('the liste is full')
        
#check if the liste is empty 
if len(myweb)>0 :
    #sort the liste
    myweb.sort()
    i=0
    while i<len(myweb):
        print( f' { myweb[i]}')
        i+=1
    
    
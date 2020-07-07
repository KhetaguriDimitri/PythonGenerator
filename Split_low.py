a=["597"]
abc=50000 # ვუთითებთ რაოდენობას, ფაილში რამდენ გენერირებულს ვინახავთ ;)
for each in a:
    with open(each+".txt") as fp:
        c=0
        
        while(a:=fp.readline()):
            a.replace("\n","").replace("\r","").strip()
            c+=1
            ff=open("spli/"+each+"-"+str(c//abc)+".txt","a")
            ff.write(a)
            ff.close()
            

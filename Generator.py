import wordlist,time
from _thread import start_new_thread as stn
def save(x):
    print("{}.txt".format(str(x)))
    for each in generator.generate(6, 6):
        print(str(x)+each)
        f=open("{}.txt".format(str(x)),"a")
        f.write(str(x)+each+"\n")
        f.close()




a=['596']
generator = wordlist.Generator('0123456789')
for each in a:
    stn(save,(each,))


# / Aldi Talk /base / Callmobile

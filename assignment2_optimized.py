from hashlib import sha1
from pdb import set_trace
import urllib2


print "Getting 1 million passwords"
raw_million_list = urllib2.urlopen(url="https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt")

print "Processing..."
million_list = [w[:-1] for w in raw_million_list]

while(True):
    counter = 0
    i = 0
    hash_to_defeat = raw_input("Enter hash: ").decode("hex")
    b = raw_input("Salt? [y/n]: ")
    if b == "y":
        b = True
    elif b == "n":
        b = False
    else:
        print "Invalid input"
        break

    if b:
        salt = raw_input("Enter salt: ").decode("hex")

    decoded_salt = None
    stop = False
    while i < len(million_list):
        w = million_list[i]
        inpt = ""

        if b and decoded_salt:
            inpt += decoded_salt
        inpt += w
        
        h = sha1()
        h.update(inpt)
        h = h.digest()

        if b and h == salt:
            decoded_salt = w
            i = 0 # reset
        if h == hash_to_defeat:
            print \
                """
Defeated.

Password: {}
Attempts: {}
""".format(w, counter)
            stop = True
            break
        
        i += 1
        counter += 1

    if stop:
        break

    print "Couldn't crack the password :("

from hashlib import sha1
import urllib2
import sys


print "Getting 1 million passwords"
raw_million_list = urllib2.urlopen(url="https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt")

print "Processing..."
million_list = [w[:-1] for w in raw_million_list]

counter = 0
i = 0
salt = None
hash_to_defeat = sys.argv[1].decode("hex")

break_salted = False
if len(sys.argv) > 2:
    if sys.argv[2] == "--salted":
        break_salted = True
    else:
        salt = sys.argv[2].decode("hex")

decoded_salt = None

if not break_salted:
    while i < len(million_list):
        print "Attempts: " + str(counter)
        w = million_list[i]
        inpt = ""

        if salt and decoded_salt:
            inpt += decoded_salt
        inpt += w
        
        h = sha1()
        h.update(inpt)
        h = h.digest()

        if salt and h == salt:
            decoded_salt = w
            i = 0 # reset

        if h == hash_to_defeat:
            print \
                """
    Defeated.

    Password: {}
    Attempts: {}
    """.format(w, counter)
            exit(0)

        
        i += 1
        counter += 1
        print("\033[A                                               \033[A")

    print "Couldn't crack the password :("

else:
    pass

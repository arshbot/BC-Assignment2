from hashlib import sha1
import urllib2


print "Getting 1 million passwords"
raw_million_list = urllib2.urlopen(url="https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt")

print "Processing..."
million_list = [w[:-1] for w in raw_million_list]

while(True):
    counter = 0
    hash_to_defeat = raw_input("Enter hash: ").decode("hex")
    stop = False
    for w in million_list:
        h = sha1()
        h.update(w)
        h = h.digest() 
        if h == hash_to_defeat:
            print \
                """
Defeated.

Password: {}
Attempts: {}
""".format(w, counter)
            stop = True
            break
        
        counter += 1

    if stop:
        break
    
    print "I'm having trouble... can I have a hint?"
    salt = raw_input("salt: ")
    decoded_salt = None
    for w in million_list:
        s = sha1()
        s.update(w)
        h = s.digest()
        if h.encode("hex") == salt:
            decoded_salt = w
    
    if decoded_salt is not None:
        for w in million_list:
            h = sha1()
            h.update(decoded_salt + w)
            h = h.digest()
            if h == hash_to_defeat:
                print """
Defeated.

Password: {}
Decoded Salt: {}
Attempts: {}
                """.format(w, decoded_salt, counter)
                stop = True
                break

        counter += 1
    
    if stop:
        break

    print "Couldn't crack the password :("

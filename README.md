Harsha Goli

# BC-Assignment2

These python program is designed to be run with python 2.7

There are 2 python programs here. 1 is the first version I wrote, the other is an optimized version. Both can be run with python2.7, and both use only the python standard library. 

## Steps to run

Ensure your python version is python 2.7.x

```
$ python --version
Python 2.7.15
```

Ensure you are in the git repo and run which ever version you prefer to test with python

```
$ python assignment2.py
```

### The following demonstrate how to test each case for assignment2.py:

#### a)

```
$ python assignment2.py
Getting 1 million passwords
Processing...
Enter hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3

Defeated.

Password: letmein
Attempts: 15
```

#### b) 

```
$ python assignment2.py
Getting 1 million passwords
Processing...
Enter hash: 801cdea58224c921c21fd2b183ff28ffa910ce31

Defeated.

Password: vjhtrhsvdctcegth
Attempts: 999967
```

#### c)

```
$ python assignment2.py
Getting 1 million passwords
Processing...
Enter hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
I'm having trouble... can I have a hint?
salt: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e

Defeated.

Password: harib
Decoded Salt: slayer
Attempts: 999999
```

### The following demonstrate how to test each case for assignment2_optimized.py:

#### a)

```
$ python assignment2_optimized.py
Getting 1 million passwords
Processing...
Enter hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Salt? [y/n]: n

Defeated.

Password: letmein
Attempts: 15
```

#### b)

```
python assignment2_optimized.py
Getting 1 million passwords
Processing...
Enter hash: 801cdea58224c921c21fd2b183ff28ffa910ce31
Salt? [y/n]: n

Defeated.

Password: vjhtrhsvdctcegth
Attempts: 999967
```

#### c)

```
python assignment2_optimized.py
Getting 1 million passwords
Processing...
Enter hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
Salt? [y/n]: y
Enter salt: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e

Defeated.

Password: harib
Attempts: 546370
```

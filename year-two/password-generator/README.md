## Programming Club (2021): #3
Split into two sides (beginners & experienced).

### Replit
To run your program:
Click on the shell tab (to the right)
Type ```python files/yourname.py``` and click ```enter```.

### Key Concepts
**Selecting Substring:**

To select a specific charcter from a string you can use []

**Remember** computers start counting @ 0. Therefore your first letter ("a") will be index 0.

``` string = "apple" string[2] = p```

** Randomly Selecting a Substring:**
There are 2 ways to select a letter, at random, from a larger string.

Method 1:
```
import random
string = "apple"
randomIndex = random.randint(0, len(string)-1)
print(string[randomIndex])
```

Method 2:
```
import random
string = "apple"
print(random.choice(string))
```

**Add to a Variable:**

Method One (Adding a Number):
```
count = 0 # Defining the variable
count += 1 # Adding one to the variable
```

Method Two (Adding a Character):
```
count = "" # Defining the variable (as an empty string)
count += "e" # Adding an "e" to the variable
```

**Floor Division:**

Division that rounds decimal points down:``` 7//2 = 3```

### Challenges
1. (ex) Make a password generator with only letters & numbers.
2. Allow the user to input a length for the outputted password (try doing this without any parameters).
3. Allow user to select if they would like symbols in their password.

### Resources
[Old Solution (Click Here!)](https://github.com/jackokeeffe/programming-club/tree/master/year-two/password-generator/thirdStep-old.py)

[Github](https://github.com/jackokeeffe/programming-club): Where all the code answers/solutions will be stored.
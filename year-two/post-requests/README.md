## Programming Club (2021): #11

### Replit
To run your program:
Click on the shell tab (to the right) and
type ```python files/yourname.py``` and click ```enter```.

### What is an API (Review)?
- An API can send/receive data.
- They are commonly used to communicate with data sources such as databases.
- You can use them to check the weather, stock prices, or, create your own.
- Think of it as code that is stored online, allowing it to be accessed from anywhere.

### GET vs POST Requests
- A **GET** request asks for something from the API. This could be user data or information about the weather.
- A **POST** request gives data to the API. This could be user info, to be stored within a database, or you could POST data to your API to tell it that the current temperature in Toronto is 3°C.

### Challenges
This challenge may be difficult, take your time and feel free to look at challenges from the past. If you do not finish this week, next week we can spend some time finishing your project.

**User Registration ([Solution]())**
- Allow the "user" to input their username, email and password.
- Send a POST request to your API. The API should receive the data and check if it is a valid entry (more about this below).
- Let the user know if their data is "valid".

**What is Valid User Data?**
- Sometimes, when you sign up for a website, they will tell you to make your password over 8 characters, ensure your email is following the proper format, etc.
- When your API receives the data, check to see if:
  1. The username is over 6 characters
  2. The email includes a "@" and ".com"
  3. The password contains at least one number.
- In order to create a final product, I recommend that you split this project into separate parts, and combine them when you feel ready.

### Resources
[PyCharm](https://www.jetbrains.com/pycharm/): I find that Replit doesn't work very well with APIs. PyCharm is a great (free) substitute to write code locally, on your machine.

[Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status): If you want to know more about the different meanings and variations of status codes, this Mozilla article lists many of them and their various uses.

[Github](https://github.com/jackokeeffe/programming-club): Where all the code answers/solutions will be stored.
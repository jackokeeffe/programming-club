## Programming Club (2021): #10

### Replit
To run your program:
Click on the shell tab (to the right) and
type ```python files/yourname.py``` and click ```enter```.

### What is an API?
- An API can send/receive data.
- They are commonly used to communicate with data sources such as databases.
- You can use them to check the weather, stock prices, or, create your own.
- Think of it as code that is stored online, allowing it to be accessed from anywhere.

### Challenges
Try to change your API to solve this. Try new things, there are many different ways to use APIs, I have not gone over all of them.

**Step 1. Football Countdown ([Solution]())**
- Allow the user to request from your API.
- You should return something with scores of teams from one sport.
- The user should be allowed to index this item you returned and ask for the score for one particular team (you do not need too many teams, just two will suffice).

Note: The score does not need to be a real score, feel free to make the information up.

Example: `requestScore()["Toronto"]`

Returns: `03-01`

**Step 2. More Sports ([Solution]())**
- Add more sports to your item and allow the user to request one of multiple (can be as low as two) sports.

**Requesting the Sport**
- Example: `requestScore()["Hockey"]`
- Returns: `Toronto: 03-01, Montreal: 03-04`

**Requesting the Sport and the Team**
- Example: `requestScore()["Hockey"]["Toronto"]`
- Returns: `03-01`

### Resources
[PyCharm](https://www.jetbrains.com/pycharm/): I find that Replit doesn't work very well with APIs. PyCharm is a great (free) substitute to write code locally, on your machine.

[Create JokeAPI Endpoint](https://jokeapi.dev/#try-it): Create a custom link with specific parameters to only return jokes matching those parameters.

[Github](https://github.com/jackokeeffe/programming-club): Where all the code answers/solutions will be stored.
# happyBot
## Runs as Below in the Anaconda Environment/ Anaconda Prompt

### Motivation
  + ChatBots are the new AI tool and are getting a Lot of attention, some are used by *Slack *Twitter etc
  + ChatBots involve good amount of Natural language processing to begin with
  + We are making a Chat Bot called "HappyBot" that can react and predict sentences based on user input and which could be scalable for more functions per demand and bandwidth
  + Currently we are using the NLTK module to do some of the processing
  + Our Goal would be to make a highly interactive GUI based BOT that will interact with users and will learn from interactions and from the knowledge it gathers from the web/google/twitter/wikipedia etc .
  + As our processing needs increase we will also think of making the project more scalable

### APIs Used
  + getProcess.py
    - These has the class parsecorpus has functions to process the corpus data provided as the input
    - clean1() - cleans the lines completely with only letters
    - tokenize() - tokenize the lines
    - ngram() - convert into n-grams
    - uniquewords() - gets the count and create a dictionary to get the positinons for creating the one hot vectors
    - vectorize() - gets the vectors for input and output , this is a generator function
  + Skip-gram Model using jupyter Notebooks
    - 

### Tools
  + python, Jupyter Notebooks

### Resources Used

**Output**
 ```
 (C:\Users\sanan\Anaconda3) C:\Public\Code\happyBot>python main.py
 Enter your greeting and I will respond !
 Good Morning
 No Comment


[['He', 'wasnt', 'home', 'alone', 'apparently']]
('time taken for filtering with filtersize = +0.000600', 20.661389134061913)
 ```

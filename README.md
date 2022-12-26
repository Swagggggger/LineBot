# LineBot

### FilmFinder
![image](https://www.erinartscentre.com/content/uploads/2022/02/2ATHYW0-1038x778-1.jpg)

## Description

Help you find the information about films

## Features

1. Show the rank of films this week in Taipei and provide links
2. Show the new films' list this week and provide the information of specific film <br />
   Information includes descriptioin and expectation
3. Show a list of theaters in Taiwan and provide links <br />
   Users can choose the area theaters in 

## FSM
![image](https://raw.githubusercontent.com/Swagggggger/LineBot/img/FSM.png)

## Technique
* LINE Bot: Built by the official LINE Messaging API
* Web Crawling: Use BeutifulSoup to search the website and fetch films' information
* Backend: Use Flask to handle the webhook and build the backend
* Anaconda: Use virtualenv to create my python environment
* ngrok: Test server locally by mapping my localhost to https domain

## Demo
### Menu
Text any messenge to call FilmFinder,then select a button <br />
![image](https://raw.githubusercontent.com/Swagggggger/LineBot/img/menu.png) <br /><br />
### Rank
Rank of this week <br />
![image](https://raw.githubusercontent.com/Swagggggger/LineBot/img/rank.png) <br /><br />
### Films This Week
![imgae](https://raw.githubusercontent.com/Swagggggger/LineBot/img/movieinfo.png)
### Film's Information
Choose the film you want to know about <br />
![image](https://raw.githubusercontent.com/Swagggggger/LineBot/img/moviedetail.png)
### Find More
Find more or back to menu <br />
![image](https://raw.githubusercontent.com/Swagggggger/LineBot/img/findmore.png) <br /><br />
### Theater
Choose the area first <br />
![image](https://raw.githubusercontent.com/Swagggggger/LineBot/img/theater.png) <br />
Theater in the area <br />
![image](https://raw.githubusercontent.com/Swagggggger/LineBot/img/theaterdeatail.png)

## Add Friends!
![image](https://raw.githubusercontent.com/Swagggggger/LineBot/img/QRcode.png)

## Reference
https://movies.yahoo.com.tw

## Bonus
### Meme
Text "more" outside the menu to find surprise <br />
![image](https://raw.githubusercontent.com/Swagggggger/LineBot/img/more.png)

# TV-Series-Library
A small app for TV Series
Written in Django, used a lot of HTML, CSS, Python and a little JavaScript.

# Origin and Reason
Initially I started testing dynamic url routing, but while testing, I decided to make an app with working database,   
some templates with style (the similarity with IMDB website is intentional). The app is specifically for TV series,  
because each series has seasons and episodes, this way one could browse and see the dynamic urls on the address bar.

# The Hardest Problem While Creating The App
Like a ship in the sea, i travelled through the code, without seeing that my model scheme is not optimal, so I reached a point  
where my app was running with pretty ugly models, 20 migrations and overriding the save() method.  

# From Scratch
At that point I decided that I should start all over. Even on the second try I had some hard time to determine a proper working model scheme,  
where a series cannot have two equal seasons or a season should be able to be in two different series and many other limitations,   
which are used to accept as something usual. 

# And it is Even Working
- Browse each series, seasons and episodes
- Add new series
- Look for info about the series and find it in IMBD
- Delete and update series - in process...

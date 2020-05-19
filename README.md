# BingoCaller

----------
- README -
----------

D.E.B.R.A.
Definitely Effective Bingo Reciting Application

DEBRA's a quick terminal-based bingo caller I wrote over a week or so to make my friends laugh. 
She'll work on Windows and that's about it because it uses the MS text to speech libraries.

DEBRA comes in two files.

------------
scrape_v1.py
------------

Bingo has a set of traditional calls for each number so I thought it'd be funny to take different 
sites, run them through Google with a number, then use the title as the call so you get a computer 
voice saying stuff like

"33. 33 Things That'll Help Solve All Of Your Cooking Frustrations. 33."

(via Buzzfeed)

Because I didn't want to pay for proper libraries to Google stuff and I'm running 100 searches each 
pass, this was super rate limited, so it writes these to a CSV rather than on the fly.

Because it was a quick build, some numbers didn't work, and it wasn't as funny as I thought, the 
CSVs for Buzzfeed and Upworthy are in there, but not complete, and I didn't use them for the game.

standard.csv has the traditional calls, modified1.csv has some in-jokes for my friends.

------------
call_v4.py
------------

This is DEBRA herself. You basically import her with a CSV then run her manually. She has an 
autoPilot method which just spews numbers out. Keyboard breaks (Ctrl + C) are handled to stop 
that loop running forever.

Main commands I used for running her in Powershell are:

import call_v4 as bingo

deb = bingo.DEBRA("standard.csv")
deb = bingo.DEBRA("modified1.csv")
deb = bingo.DEBRA("buzzfeed.csv", encoding = 'utf-8')
deb = bingo.DEBRA("upworthy.csv", encoding = 'utf-8')

deb.intro()

deb.callNum()
deb.callNum(show = True)
deb.autoPilot()
deb.autoPilot(secs = 5, show = True)

Show is used to print stuff in Powershell in case people can't hear over Zoom or whatever.
Secs specifies the pause between numbers. Default is 3.

deb.line()
deb.fullHouse()
deb.outro()

deb.called.sort()
deb.justCalled()
deb.justCalled(3)

deb.say("lol")

-----
TO DO
-----

It's honestly pretty unlikely I'll do more on this because part of the charm is that it's held 
together with the coding equivalent of duct tape, loo roll and hope. But if I do, I'd like to:

-Add a twoLines() method and just tidy up game flow. Didn't 100% know how bingo worked when I 
	made this. Again, felt it was part of the charm
-Add a better way to verify remote users' numbers after a bingo. Did it in a pinch by sorting the 
	list then printing, but Python sorts in place, so it messed up the justCalled() order
-Load the full 'Millenial bingo lingo' set
	https://www.dailymail.co.uk/news/article-7915501/Millennials-rewriting-Bingo-lingo-bid-make-game-cool-replacing-terms.html
-Make the video at the end play smoother. Just did it quickly, not well
-Use different voices to have different personalities
-Adapt for a web app
-Sort the scraper out (maybe) or come up with another funny way to generate calls from a seed
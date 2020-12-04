# Project Title

Python Twitter Bot

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

This is a python twitter bot to automate the processes of a twitter account.
This means that while you are able to opperate your twitter account as you would normally,
you could now leave the program running on your own system, or cloud server such as AWS lamda or pythonanywhere.

Leaving the program running will allow your account to automatically like tweets based on a search query that you can set.
The bot also has functions that allow you to follow all users that follow you, and unfollow those not following you.
This is useful for acount growth.

The current function that likes tweets based on a query, will also retweet the tweet, and follow the user that tweeted it.

## Getting Started <a name = "getting_started"></a>

The curent version of the bot needs only to be ran from a terminal as a python command. python3 twitter_bot.py

### Prerequisites

You need a twitter developer account to get your access and consumer keys.
The keys can be added as a dictionary together, or in a dictionary in a separate module.

### Installing

The bot runs without needing installation.
Just add the keys, and run the file.

## Usage <a name = "usage"></a>

v1 - change the 'auto_like()' function to any of the other functions to perform the operation.
unfollow_nonfollowers(): unfollows all non following friends
follow_followers(): follows all following friends
check_followers(): outputs the current followers.

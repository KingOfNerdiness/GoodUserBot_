# Good User Bot v0.1
# Created by: /u/whaliam
# Import required libraries

print("Starting /u/GoodUserBot_:")
print("Importing required libs:")

import praw
import pdb
import os
import time
import re
import random
from datetime import datetime
import sys
from setuptools.command.rotate import rotate

print("Creating a Reddit instance:")
print("Logging in:")

# Define a Reddit instance
# Change settings to your own API settings

reddit = praw.Reddit(user_agent='x',
                  client_id='x',
                  client_secret='x',
                  username='x',
                  password='x')

print("Welcome /u/GoodUserBot_")
print("Defining variables:")

def scan():
    for c in reddit_client.get_comments('all'):
        if keyword not in c.body.lower():
            continue
        if c.author == None:
            continue
        if c.author.name ==bot_name:
            continue
        anwser(c, c.link_id[3:])

def answer(comment, sub_id):
    sub = reddit_client.get_submission(submission_id=sub_id)
    sub.replace_more_comments(limit=None,threshold=0)
    flat_comments = praw.helpers.flatten_tree(sub.comments)
    if len([com for com in flat_comments if com.author != None and com.author.name.lower() == bot_name.lower()]) > 0:
        return False
    
# Define variables
# For multiple subs use ("sub1"+"sub2")
# Change quote value to response string

username = "GoodUserBot_"

print("Setting subreddit parameters:")

subreddit = reddit.subreddit("all")
quote = "Good User!"
reply = (quote)

print("Searching for comments to reply to:")
for comment in subreddit.stream.comments():
    if re.search("Good Bot", comment.body, re.IGNORECASE):

        print("Comment found: replying:")

        comment.reply(reply)

        print("Replied!")
        print("Searching for comments to reply to:")
        print("Cooldown")
time.sleep(5)
# Created by /u/whaliam
# 6Ep96ck9@protonmail.com

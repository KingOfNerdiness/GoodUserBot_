import praw
import time
import re
import config

print("Starting /u/GoodUserBot_:")
print("Importing required libs:")

path = '/home/whaliam/Desktop/GoodUserBot/commented.txt'

blacklistUsers = ('Automoderator', 'friendly-bot', 'GoodBot_BadBot', 'GoodUserBot_')

print("Creating a Reddit instance:")
print("Logging in:")



def authenticate():

      print('Authenticating...\n')
      reddit = praw.Reddit(user_agent=config.user_agent,
                        client_id=config.client_id,
                        client_secret=config.client_secret,
                        username=config.username,
                        password=config.password)
      print('Authenticated as {}\n'.format(reddit.user.me()))
      return reddit
print("Welcome /u/GoodUserBot_")
print("Defining variables:")
def run_bot(reddit):

    print('Get comments..\n')
    for comment in reddit.subreddit('all').comments(limit = None):
        author = str(comment.author)

        matchBLACKLIST = author not in blacklistUsers 
        matchGOOD = re.search("Good Bot", comment.body, re.IGNORECASE)
        
        if matchGOOD and matchBLACKLIST:
        
            #opening commented.txt
            file_obj_r = open(path,'r')
            try:
                reply = 'Good user'
            except:
                print('debug')
          
            else:

                # checking if already answered to comment or other comment in thread
                if comment.id not in file_obj_r.read().splitlines() and comment.submission.id not in file_obj_r.read().splitlines():
                    print('Comment is unique..replying')
                
                    try:
                        comment.reply(reply)
                    except Exception as e:
                        print('Error encountered:')
                        print(e)
                        print('Continuing...')
                    file_obj_r.close()

                    file_obj_w = open(path,'a+')
                    file_obj_w.write(comment.submission.id + '\n' + comment.id + '\n')
                    file_obj_w.close()
                
                else:
                    print('Already replied...no reply needed\n')
                    
            time.sleep(5)
                        
            print('Get comments..\n')
            for comment in reddit.subreddit('all').comments(limit = None):
              author = str(comment.author)

              matchBLACKLIST = author not in blacklistUsers 
              matchGOOD = re.findall(r"(?i)^\bgood\sbot\b", comment.body)
              
              if matchGOOD and matchBLACKLIST:
        
        	#opening commented.txt
                  file_obj_r = open(path,'r')
            try:
                reply = 'Good user'
            except:
                print('debug')
          
            else:
          			# checking if already answered to comment or other comment in thread
                if comment.id not in file_obj_r.read().splitlines() and comment.submission.id not in file_obj_r.read().splitlines():
                    print('Comment is unique..replying')
                
                    try:
                        comment.reply(reply)
                    except Exception as e:
                        print('Error encountered:')
                        print(e)
                        print('Continuing...')
                    file_obj_r.close()

                    file_obj_w = open(path,'a+')
                    file_obj_w.write(comment.submission.id + '\n' + comment.id + '\n')
                    file_obj_w.close()
                
                else:
                    print('Already replied...no reply needed\n')
        

def main():
    reddit = authenticate()
    while True:
        run_bot(reddit)


        
if __name__ == '__main__':
        main()


					
                
                    
                

import praw
import obot
import time



phrases_to_look_for = ("I am ugly", "I am not worth it",
                       "I don't deserve it", "I suck",
                       "I shouldn't exist",
                       "I am a phony", "I should die", "I am not beautiful",
                       "I am not pretty", "Why do I even exist", 
                       "I am an idiot", "I am a monster", "I am not beautiful")
already_done_comments = []

def main():
	try:
		r = obot.login()
		subreddit = r.subreddit('test') #fetch top hot 15 submissions from each subreddit 
		for comment in subreddit.stream.comments():
			print("hi")
			process_comments(comment)
	except Exception as e:
		print("Going to sleep for 10 minutes")
		time.sleep(600)
		main()

	

def process_comments(comment):
	print("hello")
	green_light = True
	for phrase in phrases_to_look_for:  		
		if phrase in comment.body and comment.id not in already_done_comments:
			for reply in comment.replies:
				if reply.author.name == 'the_ugly_bot':
					print("check")
					green_light = False
					break
			if (green_light == True):
				print("nice")
				comment.reply("You are beautiful")
				print(comment.body)
				already_done_comments.append(comment.id)
				break
	
              	        	
if __name__ == '__main__':
    main()       		
        
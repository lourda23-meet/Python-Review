def create_youtube_video (title, description):
	newvideo = {"Title": title, "description" : description, "likes" : 0, "comments": {"user": " "}}
	return youtube_video 

def likes (youtube_video): 
	if "likes" in youtube_video:
		youtube_video["likes"]+=1

def dislikes(youtube_video): 
	if "dislikes" in youtube_video: 
		youtube_video{"dislikes"}+=1 

def add_comment(youtube_video,username1,commen_text):
	youtube_video[comments[username]]==commen_text

lour = create_youtube_video("firstvideo","ilikeyoutube")

for i in range(495): 
	likes(lour)

print(lour)
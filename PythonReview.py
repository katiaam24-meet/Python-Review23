def create_youtube_video(title, description):
	youtube_video = {"title" : title , "description" : description , "likes" : 0 , "dislikes" : 0 , "comments" : {'username':""}}
	return youtube_video
def like(youtub_video):
	if "likes" in youtube_video:
		likes+=1
		return youtube_video

def disike(youtube_video):
	if "dislikes" in youtube_video:
		dislikes+=1
		return youtube_video

def add_comment(youtube_video, username,comment_text):
	comments ={"username" : comment_text}
	return comments

new_vid = create_youtube_video('ALIII','ALII WAS HERE' )
print(new_vid  )




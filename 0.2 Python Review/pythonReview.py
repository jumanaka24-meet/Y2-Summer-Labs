def create_youtube_video(title, description):
	youtubevideo = {"title": title, "description": description, "likes": 0, "dislikes" : 0 , "comments": {"username": ""}}
	return youtubevideo
   
x =  ("Jumana ")
y =  ("Hello ")
newvid = create_youtube_video(x, y)



def likes (vid):
	if "likes" in vid:
		vid["likes"]+= 1
	return vid 



def dislikes (vid2):
	if "dislike" in vid:
		vid["dislikes"]+= 1
	return vid2


def add_comment (youtubevideo, username, comment_text) : 
	youtubevideo["comments"] [username] = comment_text 
	return youtubevideo 
youtube_dict = create_youtube_video ("Jumana", "My life")

while youtube_dict ["likes"] < 495:
	youtube_dict["likes"]+= 1
 

print(youtube_dict)








import praw

def reddit_instance() -> praw:
    return praw.Reddit(config_interpolation="basic")

def redditImageType(url):
    # Code provided by: tdifilippo
    # Will implement in the future. Not needed at the moment
    """
        redditImageType 
            args: url text
            return: True if its an image, False if not
            
        This function searches the url text to determine if its:
            An imgur asset
            One of the : PNG, JPG, JPEG, GIF (etc.)
            return True
    """
    # imageType
    imageType=['.jpg','.png','.jpeg','.bmp']
    # Assume imgur url always returns an image
    if url.find('imgur') != -1:
        return True
    # Find the last . to check for image extension types
    index = url.rfind('.')
    # Check that it was found
    if index != -1:
        # Iterate through the imageType
        for imageExt in imageType:
            if url[index:].find(imageExt) != -1:
                return True
    # Not an image return False
    return False

def gallery_img(url) -> list:
    submission = reddit_instance().submission(url=url)
    gallery = []
    for i in submission.gallery_data['items']:
        media_id = i['media_id']
        meta = submission.media_metadata[media_id]
        if meta['e'] == 'Image':
            img_data = meta['s']
            img_source = img_data['u']
            gallery.append(img_source)
    return gallery

def get_data (
    submission_limit = 10, 
    selected_subreddit = "customkeyboards"
    ):
    """
        get_data
            args: 
                submissions_limit
                selected_subreddit
            return: submissions

        Returns a list of submissions
    """
    instance = reddit_instance()
    submissions = []
    for submission in instance.subreddit(selected_subreddit).hot(limit=submission_limit):
        submission_data = {
            "author" : submission.author.name,
            "pfp" :submission.author.icon_img,
            "likes" : submission.score,
            "title" : submission.title,
            "img" : submission.url,
        }

        if "gallery" in submission_data["img"]:
            submission_data["img"] = gallery_img(submission_data["img"])

        submissions.append(submission_data)
    return submissions
    

if __name__ == "__main__":
    instance = reddit_instance()
    subreddit = instance.subreddit("customkeyboards")
    # Very slow. Waits until all request are sent
    print(f'{get_data()}')
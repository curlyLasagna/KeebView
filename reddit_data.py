import asyncio
import praw

def reddit_instance() -> praw:
    return praw.Reddit()

"""
get_submission_data

Args:
    submission: Given subreddit from a praw instance

Returns:
    submission_data: Data from a submission's:
                     author, upvotes, title, time & img
"""
def get_submission_data(submission) -> dict:
    submission_data = {
        "author" : submission.author.name,
        "pfp" : submission.author.icon_img,
        "likes" : submission.score,
        "time" : submission.created,
        "title" : submission.title,
        "img" : submission.url
    }

    def gallery_img() -> list:
        gallery = []
        for i in submission.gallery_data['items']:
            media_id = i['media_id']
            meta = submission.media_metadata[media_id]
            if meta['e'] == 'Image':
                img_data = meta['p']
                # img_source = img_data['u']
                gallery.append(img_data)
        return gallery

    if "gallery" in submission_data["img"]:
        submission_data["img"] = gallery_img()

    return submission_data

if __name__ == "__main__":
    instance = reddit_instance()
    subreddit = instance.subreddit("customkeyboards")
    for s in subreddit.hot(limit=15):
        print(f'{get_submission_data(s)}')

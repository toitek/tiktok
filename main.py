from TikTokApi import TikTokApi
import csv
import os
import time


api = TikTokApi()
hashtag = "Safari"

filename = f"{hashtag}_tiktok_data.csv"

if not os.path.exists(filename):
    
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Author", "Likes", "Shares", "Comments", "Video URL"])

while True:
    
    tiktoks = api.byHashtag(hashtag, count=30)

    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        existing_posts = set(row[0] for row in reader)

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
       
        for tiktok in tiktoks:
            title = tiktok["desc"]
            if title in existing_posts:
                continue

            author = tiktok["author"]["uniqueId"]
            likes = tiktok["stats"]["diggCount"]
            shares = tiktok["stats"]["shareCount"]
            comments = tiktok["stats"]["commentCount"]
            video_url = tiktok["video"]["downloadAddr"]
            writer.writerow([title, author, likes, shares, comments, video_url])
    
    time.sleep(3600)

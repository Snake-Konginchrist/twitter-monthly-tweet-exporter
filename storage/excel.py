import pandas as pd
import os


# 保存推文到Excel
def save_to_excel(tweets, username, year, month):
    data = [{
        'Tweet': tweet.full_text,
        'Created At': tweet.created_at,
        'Retweets': tweet.retweet_count,
        'Likes': tweet.favorite_count
    } for tweet in tweets]

    df = pd.DataFrame(data)
    filename = f"{username}_{year}_{month}.xlsx"
    data_dir = 'data'  # 定义数据存储目录
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    filepath = os.path.join(data_dir, filename)
    df.to_excel(filepath, index=False)
    return filepath

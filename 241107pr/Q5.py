def calculate_priority_score(views, avg_watch_time, video_length, relevance_coefficient):
    return views * avg_watch_time * video_length * relevance_coefficient

def recommend_videos(n, videos_data):
    video_scores = []
    for video in videos_data:
        name, views, avg_watch_time, video_length, relevance_coefficient = video
        priority_score = calculate_priority_score(views, avg_watch_time, video_length, relevance_coefficient)
        video_scores.append((name, priority_score))
    video_scores.sort(key=lambda x: x[1], reverse=True)
    sorted_video_names = [video[0] for video in video_scores]
    return sorted_video_names
n = int(input("請輸入影片總數："))
videos_data = []
for _ in range(n):
    video_info = input("請輸入影片資料 (名稱 觀看人數 平均觀看時間 影片長度 相關係數):").split()
    name = video_info[0]
    views = int(video_info[1])
    avg_watch_time = int(video_info[2])
    video_length = int(video_info[3])
    relevance_coefficient = int(video_info[4])
    videos_data.append((name, views, avg_watch_time, video_length, relevance_coefficient))
sorted_videos = recommend_videos(n, videos_data)
print("\n影片推薦排序:")
for video in sorted_videos:
    print(video)

class VideoContent:
    def __init__(self, title, clicks, watch_time):
        self.title = title
        self.clicks = clicks
        self.watch_time = watch_time  

    def engagement_rate(self):
        return self.clicks * self.watch_time
    
    def __repr__(self):
        return f"{self.title}"
    
database = [
    VideoContent("Funny Cats", clicks = 4000, watch_time = 1.0),
    VideoContent("Cooking Bangladeshi food", clicks = 800, watch_time = 5.0),
    VideoContent("Dhaka Times News", clicks = 1500, watch_time = 3.0) ]

print("Old algorithm recommendations:")
bad_ranking = sorted(database, key=lambda x: x.clicks, reverse=True)
for i, vid in enumerate(bad_ranking):
    print(f"{i+1}. {vid} with {vid.clicks} clicks")

print("\nImproved algorithm recommendations:")
better_ranking = sorted(database, key=lambda x: x.engagement_rate(), reverse=True)
for i, vid in enumerate(better_ranking):
    score = vid.engagement_rate()
    print(f"{i+1}. {vid} with engagement rate of {score}")



        
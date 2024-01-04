from youtube_search import YoutubeSearch
import webbrowser
results = YoutubeSearch('burj khalifa song', max_results=1).to_dict()
res = results[0]['url_suffix']
webbrowser.open(f"https://youtube.com{res}")
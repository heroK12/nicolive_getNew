import requests
import json
import time
 

class Search:
	def url_create(self,tags):
		url = "https://api.search.nicovideo.jp/api/v2/live/contents/search?q="+ tags +"&targets=tags&fields=contentId,title&_sort=-startTime&_limit=100&filters[liveStatus][0]=onair"
	return url




url_tags = Search()
url = url_tags.url_create(str(input("検索したいタグを入力してください:")))
# print(url)


# 10秒ごとにループさせる


while True:
 	print("取得を開始")
 	response = requests.get(url)
	
 	# print (response.text)
 	# jsonに変換
 	data = json.loads(response.text)
 	# リストは100件まで取得
 	# でもそのタグに100件も配信が無ければ存在しないリスト番号ができてエラーが起きる
 	# だからリストの数だけを取得するようにする
 	data_len1 = len(data["data"]) 
 	print("現在のそのタグでの配信数"+ str(data_len1))
 	data_len = data_len1 - 1

 	while data_len > 0:
 		print (data["data"][data_len]["title"])
 		print ("https://live2.nicovideo.jp/watch/"+data["data"][data_len]["contentId"])
 		print ()
 		data_len-=1
 	print("終了するならCtrl+Cを押してください")
 	print("更新頻度は100秒ごとです")

 	
 	# 10秒間隔で情報を取得する
 	time.sleep(100)

# import requests
#
# url = "https://streaming-availability.p.rapidapi.com/shows/search/title"
#
# querystring = {"country":"IN","title":"hanuman","output_language":"en","show_type":"movie","series_granularity":"show"}
#
# headers = {
# 	"X-RapidAPI-Key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
# 	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())


import requests

url = "https://imdb188.p.rapidapi.com/api/v1/searchIMDB"

querystring = {"query":"Action"}

headers = {
	"X-RapidAPI-Key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
	"X-RapidAPI-Host": "imdb188.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

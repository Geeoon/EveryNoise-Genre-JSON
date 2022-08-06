import json
import requests

if __name__ == "__main__":
	vector = "name"  # sorting method
	url = 'https://everynoise.com/everynoise1d.cgi?scope=all' + (vector and ("&vector=" + vector))  # everynoise genre list
	html = requests.get(url).text
	genre_total = 0
	genre_array = []
	for line in html.splitlines():
		if line.find("<tr valign=top class=><td align=right class=note  >") != -1:
			genre_total += 1
			temp = line.split(">")
			genre_array.append(temp[-4].split("<")[0])
	f = open("output.json", "w")
	f.write(json.dumps({"genres": genre_array, "total": genre_total}))
	f.close()
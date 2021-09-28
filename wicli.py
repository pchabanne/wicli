import wikipedia
import sys
import argparse
import urllib.request
import json

parser = argparse.ArgumentParser()
parser.add_argument("search", help="The article you search")
parser.add_argument("random", action="store_true", help="type random to get a random article")
parser.add_argument("--lang", "-l", type=str,  help="choose language")
parser.add_argument("--full", "-f", action="store_true", help="if sets, display the full page")
parser.add_argument("--link", action="store_true", help="if sets, display the link of the article at the end")
args = parser.parse_args()

lang = "en"

if args.lang:
	wikipedia.set_lang(args.lang)
	lang = args.lang

if args.search == "random":
	url = "https://"+lang+".wikipedia.org/api/rest_v1/page/random/title"
	req = urllib.request.Request(url)
	r = urllib.request.urlopen(req).read()
	cont = json.loads(r.decode("utf-8"))
	subject=cont["items"][0]['title']
else:
	subjectList = wikipedia.search(args.search)
	subject = subjectList[0]

try:
	p = wikipedia.page(subject, auto_suggest=False)
	print("====== "+p.title+" ======")
	if args.full:
		print(p.content)
	else:
		print(p.summary)
	if args.link:
		title = p.title
		title = title.replace(" ", "_")
		print(title)
		print("https://"+lang+".wikipedia.org/wiki/"+title)
	
except wikipedia.exceptions.DisambiguationError as e:
	print("Too Many results, be more specific")
	print(e)

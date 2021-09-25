import wikipedia
import sys
import argparse
import urllib.request
import json

parser = argparse.ArgumentParser()
parser.add_argument("search", help="The article you search")
parser.add_argument("--lang", "-l", type=str,  help="choose language")
parser.add_argument("--full", "-f", action="store_true", help="if sets, display the full page")
args = parser.parse_args()


if args.lang:
	wikipedia.set_lang(args.lang)

if args.search == "random":
	url = "https://en.wikipedia.org/api/rest_v1/page/random/title"
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
	
except wikipedia.exceptions.DisambiguationError as e:
	print("Too Many results, be more specific")
	print(e)

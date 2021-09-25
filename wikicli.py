import wikipedia
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("search", help="The article you search")
parser.add_argument("--lang", "-l", type=str,  help="choose language")
parser.add_argument("--full", "-f", action="store_true", help="if sets, display the full page")
args = parser.parse_args()


if args.lang:
	wikipedia.set_lang(args.lang)


subjectList = wikipedia.search(args.search)
subject = subjectList[0]

try:
#	print(wikipedia.summary(subject))
#	page = wikipedia.page("Popee")
#	print(page.title)
	p = wikipedia.page(subject, auto_suggest=False)
	print("====== "+p.title+" ======")
	if args.full:
		print(p.content)
	else:
		print(p.summary)
	
except wikipedia.exceptions.DisambiguationError as e:
	print("Too Many results, be more specific")
	print(e)

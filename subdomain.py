import requests
import sys
import urllib
import urllib.request as ur

domain_dict=open("names.txt").read()
subs = domain_dict.splitlines()

for sub in subs:
	url_to_check=f"http://{sub}.{sys.argv[1]}"

	try:
		requests.get(url_to_check)

	except requests.ConnectionError:
		pass
	else:
		print("Found subdomain:",url_to_check)

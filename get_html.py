import time
import urllib.request, urllib.parse

url = "https://forethumb.com"

with urllib.request.urlopen(url) as res:
  html = res.read().decode("utf-8")
  print(html)

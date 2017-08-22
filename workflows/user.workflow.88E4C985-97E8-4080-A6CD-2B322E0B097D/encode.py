import sys
import urllib

query = sys.argv[1]
print urllib.quote(query)

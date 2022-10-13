import sys
import json

for line in sys.stdin:
    print(json.loads(line)['content'])

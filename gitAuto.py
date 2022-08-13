import os
lst = ['git pull', 'git add -A', 'git commit -m "Modified 1.0"', 'git push']
for i in lst:
    os.system(i) 
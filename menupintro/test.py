from datetime import datetime
date = list('2011-04-14T16:00:49Z')
date.pop(10)
date.pop(18)
l = ''
l = l.join(date)
print(l)
dd = datetime.strptime(l, "%Y-%m-%d%H:%M:%S")
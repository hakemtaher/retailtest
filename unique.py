import datetime
def unique(prefix):
    ct = datetime.datetime.now()
    ts = ct.timestamp()
    ts = int(ts)
    ts = str(ts)
    ts = prefix + ts
    return ts
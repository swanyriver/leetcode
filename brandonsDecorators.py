def prettystring(obj):
    string = []
    for k,v in obj.__dict__.items():
        string.append("%s:%r"%(k,v))
    return "(" + ",".join(string) + ")"

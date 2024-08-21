import io

class DebugLog:
    def __init__(self):
        self.msg = []

debug_log=None

def init():
    global debug_log
    debug_log=DebugLog()

def error(msg):
    print("error: " + msg)

def fatal(msg):
    print("fatal: " + msg)
    exit

def info(msg):
    print("info: " + msg)

def debug(obj=""):
    output = io.StringIO()
    print(obj, file=output, end="")
    debug_log.msg = debug_log.msg + [output.getvalue()]
    output.close()

def dump():
    for m in debug_log.msg:
        print(m)

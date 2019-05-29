from logbook import Logger, StreamHandler
import sys


StreamHandler(sys.stdout).push_application()
log = Logger('linda的日志')
log.warn('这是一个非常酷的输出')

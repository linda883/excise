import os
import logbook
from logbook import Logger, TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.00"


def user_handler_log_formatter(record, handler):
    log = "[{date}][{level}][{filename}][{func_name}][{lineno}]- {msg}".format(
        date=record.time,
        level=record.level_name,  # 日志等级
        filename=os.path.split(record.filename)[-1],  # 文件名
        func_name=record.func_name,  # 函数名
        lineno=record.lineno,  # 行号
        msg=record.message,  # 日志内容
    )
    return log


# 打印到屏幕句柄
user_std_handler = ColorizedStderrHandler(bubble=True, level='ERROR')
user_std_handler.formatter = user_handler_log_formatter
# 日志路径，在主工程下生成log目录
LOG_DIR = os.path.join('log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 打印到文件句柄
user_file_handler = TimedRotatingFileHandler(
    os.path.join(LOG_DIR, '%s.log' % 'test_log'), date_format='%Y%m%d', bubble=True)
user_file_handler.formatter = user_handler_log_formatter
# 用户代码logger日志
user_log = Logger("user_log")


def init_logger():
    logbook.set_datetime_format("local")
    user_log.handlers = []
    user_log.handlers.append(user_std_handler)
    user_log.handlers.append(user_file_handler)

import logging
import time

# logging.info("这是信息。默认不输出")
# logging.debug("这是调试信息")
# logging.warning("p warning")
# logging.error("error")
# logging.critical("yanzhong")


# 默认输入警告级别warning
# 设置输出的格式和位置，# 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
#  # a是追加模式，默认如果不写的话，就是追加模式  # 日志格式
logfilename = time.strftime('%Y%m%d-%H%M%S')
logging.basicConfig(level=logging.WARNING,
                    filename=logfilename+'.log',
                    filemode='a',
                    format=
                    '%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s')

logging.debug('debug级别，最低级别，一般开发人员用来打印一些调试信息')
logging.info('info级别，正常输出信息，一般用来打印一些正常的操作')
logging.warning('waring级别，一般用来打印警信息')
logging.error('error级别，一般用来打印一些错误信息')
logging.critical('critical 级别，一般用来打印一些致命的错误信息,等级最高')
'''
%(name)s            Name of the logger (logging channel)
    %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                        WARNING, ERROR, CRITICAL)
    %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                        "WARNING", "ERROR", "CRITICAL")
    %(pathname)s        Full pathname of the source file where the logging
                        call was issued (if available)
    %(filename)s        Filename portion of pathname
    %(module)s          Module (name portion of filename)
    %(lineno)d          Source line number where the logging call was issued
                        (if available)
    %(funcName)s        Function name
    %(created)f         Time when the LogRecord was created (time.time()
                        return value)
    %(asctime)s         Textual time when the LogRecord was created
    %(msecs)d           Millisecond portion of the creation time
    %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                        relative to the time the logging module was loaded
                        (typically at application startup time)
    %(thread)d          Thread ID (if available)
    %(threadName)s      Thread name (if available)
    %(process)d         Process ID (if available)
    %(message)s         The result of record.getMessage(), computed just as
                        the record is emitted
'''
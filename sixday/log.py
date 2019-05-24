import logbook
import os
from logbook.more import ColorizedStderrHandler
from file_path_m import file_path

path = file_path()
LOG_DIR = os.path.join(path, 'log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)   #  如果log不存在，在当前路径下创建一个log文件夹，


def get_logger(name='Test', file_log=True, level='debug'):
    logbook.set_datetime_format('local')

    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    if file_log:
        logbook.TimedRotatingFileHandler(os.path.join(LOG_DIR, '%s.log' % name),
                                         date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)


LOG = get_logger(file_log=True, level='INFO')


if __name__ == "__main__":
    LOG.info("log-info")
    LOG.error('Log-error')



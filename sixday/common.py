import os, logging, configparser


def load_config(file_name):
    config = configparser.ConfigParser()
    if os.path.exists(file_name):
        config.read(file_name)
        return config


def init_log(log_level, log_path):

    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s [%(levelname)-8s %(module)s:%(lineno)d] %(message)s')
    log_file = logging.FileHandler(log_path)
    log_file.setFormatter(formatter)
    logger.addHandler(log_file)
    logger.setLevel(log_level)

    return logger


if __name__ == "__main__":
    log = init_log(10, "monitor.log")
    log.info("建立日志")
    monitor_cfg = load_config("monitor.cfg")
    try:
        for section in monitor_cfg.sections():
            log.info("section is " + section)
            print(section)
            if section == 'sys':
                log.debug("monitor ip:" + monitor_cfg.get(section, 'ip'))
    except AttributeError:
        log.error("没这个东西")

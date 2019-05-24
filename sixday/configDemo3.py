import configparser


config = configparser.ConfigParser()

cfg_info = config.read("monitor3.cfg")
print(config.sections())
print(config.get(config.sections()[0], 'log_level'))
print(config.get(config.sections()[0], 'ip'))




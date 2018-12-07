from configparser import ConfigParser

configfile = 'config.ini'
config = ConfigParser()
config.read(configfile)
print('请输入名字:')
print(config['messages'].get('greeting'), input())
print(config['messages'].get('question'))
nums = config['numbers']
print('背诵圆周率:', nums.get('pi'))

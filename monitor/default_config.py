# spark default config

class Config():

    def __init__(self):
        self.file = 'data/spark-defaults.conf'
        self.conf = dict()

    def _read_from_file(self):
        with open(file=self.file) as f:
            lines = f.readlines()
            for line in lines:
                if not line.strip() or line[0] != '#':
                    cf = line.split(' ')
                    if len(cf) == 2:
                        self.conf[cf[0]] = cf[1][:-1]

    def get(self, conf_key):
        return self.conf[conf_key]

    def set(self, conf_key, conf_value):
        self.conf[conf_key] = conf_value

    def get_all(self):
        for key in self.conf.keys():
            print('--config ' + key + ' ' + str(self.conf[key]))

    def get_part(self, part_name):
        for key in self.conf.keys():
            if part_name in key:
                print('--config ' + key + ' ' + str(self.conf[key]))


if __name__ == '__main__':
    config = Config()
    config._read_from_file()
    # print(config.conf)
    print(config.conf['spark.port.maxRetries'])
    print('total config parameters: ' + str(len(config.conf)))
    # config.get_all()
    config.get_part('shuffle')
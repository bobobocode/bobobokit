#!/usr/bin/env python3

# BoBoBo

import configparser


def get_conf(conf_file, default_section=None):
    conf = configparser.ConfigParser()
    try:
        conf.read(conf_file)
        print("Read config from: " + conf_file)
    except:
        print("Failed to read conf file: " + str(conf_file))
        conf = None

    def _get_conf(key, section=None, default=None):
        nonlocal conf
        nonlocal default_section

        if None is section:
            if default_section:
                section = default_section
            else:
                section = "default"
        try:
            if conf is None:
                raise Exception('None conf.')

            if key is None:
                return dict(conf[section])

            s = conf.get(section, key)
            if s.isnumeric():
                try:
                    return int(s)
                except ValueError:
                    return float(s)
            else:
                return s
        except configparser.Error:
            print('Found No config of %s:%s' %
                  (section, key) + '. Will use default.')
            return default
        except Exception as e:
            print('Faild to get value %s : %s' %
                  (section, key) + ' Exception: ' + str(e))
            return default

    return _get_conf

import configparser
import os


def read_configuration(category, key):
    # configure = configparser.ConfigParser()
    # script_path = os.path.abspath("config.ini")
    # script_directory = os.path.dirname(script_path)
    # config_ini_path = os.path.join(script_directory, 'configurations', 'config.ini')
    configure = configparser.ConfigParser()
    # print(config_ini_path)
    # read_status = configure.read(config_ini_path)
    configure.read("C:\\Users\\User\\PycharmProjects\\pythonProject1\\configurations\\config.ini")
    # print(read_status)
    # Get a list of all sections
    # sections = configure.sections()

    # Print the list of sections
    # print("Sections:", sections)
    # print(configure.get('config', 'url'))
    return configure.get(category, key)

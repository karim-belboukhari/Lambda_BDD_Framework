import yaml


def get_config_values(section, key):
    with open(r".\features\resources\config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
    return config[section][key]
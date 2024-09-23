
import yaml
from typing import Dict

class ConfigManager():

    ''' Configuration creator and manager'''

    def __init__(self, config_path):
        with open(config_path, encoding='utf-8') as c:
            config = yaml.safe_load(c)
        
        self.__config = config

    def get_config(self) -> Dict:
        return self.__config
    
config: ConfigManager = ConfigManager('/home/hcheong/projects/spenny/backend/app/configs/spenny_backend_config.yml')
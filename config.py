from os import path

import hiyapyco

global_config_file = 'config/config.yaml'
local_config_file = 'config/config.local.yaml'

if path.exists(local_config_file):
    options = hiyapyco.load([global_config_file, local_config_file], method=hiyapyco.METHOD_MERGE)
else:
    options = hiyapyco.load(global_config_file)

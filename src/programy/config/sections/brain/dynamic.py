"""
Copyright (c) 2016-17 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import logging

from programy.config.base import BaseConfigurationData

class BrainDynamicsConfiguration(BaseConfigurationData):

    def __init__(self):
        BaseConfigurationData.__init__(self, "dynamic")
        self._dynamic_sets      = {}
        self._dynamic_maps      = {}
        self._dynamic_vars      = {}

    @property
    def dynamic_sets(self):
        return self._dynamic_sets

    @property
    def dynamic_maps(self):
        return self._dynamic_maps

    @property
    def dynamic_vars(self):
        return self._dynamic_vars

    def load_config_section(self, config_file, brain_config, bot_root):
        dynamic_config = config_file.get_section("dynamic", brain_config)
        if dynamic_config is not None:
            self.load_dynamic_sets(config_file, dynamic_config)
            self.load_dynamic_maps(config_file, dynamic_config)
            self.load_dynamic_vars(config_file, dynamic_config)
        else:
            if logging.getLogger().isEnabledFor(logging.ERROR): logging.error("Config section [dynamic] missing from Brain, using defaults")

    def load_dynamic_sets(self, config_file, dynamic_config):
        sets_config = config_file.get_option(dynamic_config, "sets")
        if sets_config is not None:
            for set in sets_config.keys():
                dyn_set_class = sets_config[set]
                self._dynamic_sets[set.upper()] = dyn_set_class

    def load_dynamic_maps(self, config_file, dynamic_config):
        maps_config = config_file.get_option(dynamic_config, "maps")
        if maps_config is not None:
            for map in maps_config.keys():
                dyn_map_class = maps_config[map]
                self._dynamic_maps[map.upper()] = dyn_map_class

    def load_dynamic_vars(self, config_file, dynamic_config):
        vars_config = config_file.get_option(dynamic_config, "variables")
        if vars_config is not None:
            for var in vars_config.keys():
                dyn_var_class = vars_config[var]
                self._dynamic_vars[var.upper()] = dyn_var_class



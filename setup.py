#!/usr/bin/env python3

# Copyright 2016 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

if sys.version_info < (3, 7):
    raise SystemExit(
        f'ERROR: Tried to install Meson with an unsupported Python version: \n{sys.version}\nMeson requires Python 3.7.0 or greater'
    )

from setuptools import setup

data_files = []
if sys.platform != 'win32':
    # Only useful on UNIX-like systems
    data_files = [('share/man/man1', ['man/meson.1']),
                  ('share/polkit-1/actions', ['data/com.mesonbuild.install.policy'])]

setup(data_files=data_files,)

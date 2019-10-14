"""
Copyright 2019 ARC Centre of Excellence for Climate Extremes

author: Aidan Heerdegen <aidan.heerdegen@anu.edu.au>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys

import xarray

def check_calendar(filepath):

    try:
        ds = xarray.open_dataset(filepath, decode_cf=False)
    except:
        print("check_calendar :: File failed to open cleanly without decode_cf {}".format(filepath))
        raise

    try:
        ds = xarray.open_dataset(filepath, decode_times=False)
    except:
        print("check_calendar :: File failed to open cleanly without decode_times {}".format(filepath))
        raise

    try:
        ds = xarray.open_dataset(filepath)
    except:
        print("check_calendar :: File failed to open cleanly with decode_cf {}".format(filepath))
        raise

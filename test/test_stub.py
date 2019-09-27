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

import qcmip6

verbose = True

def setup_module(module):
    """
    Put any test-wide setup code in here, e.g. creating test files
    """
    if verbose: print ("setup_module      module:%s" % module.__name__)
 
def teardown_module(module):
    """
    Put any test-wide teardown code in here, e.g. removing test outputs
    """
    if verbose: print ("teardown_module   module:%s" % module.__name__)


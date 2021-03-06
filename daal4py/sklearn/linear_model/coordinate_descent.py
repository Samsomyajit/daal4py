#
#*******************************************************************************
# Copyright 2020 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#******************************************************************************/


from sklearn import __version__ as sklearn_version
from distutils.version import LooseVersion
from daal4py import __daal_run_version__, __daal_link_version__

daal_run_version = tuple(map(int, (__daal_run_version__[0:4], __daal_run_version__[4:8])))
daal_link_version = tuple(map(int, (__daal_link_version__[0:4], __daal_link_version__[4:8])))

if daal_run_version >= (2020, 1) and daal_link_version >= (2020, 1):
    if (LooseVersion(sklearn_version) >= LooseVersion("0.21") and LooseVersion(sklearn_version) < LooseVersion("0.23")):
        from ._coordinate_descent_0_21 import *
    elif (LooseVersion(sklearn_version) >= LooseVersion("0.23")):
        from ._coordinate_descent_0_23 import *
    else:
        from sklearn.linear_model._coordinate_descent import *
else:
    from sklearn.linear_model._coordinate_descent import *

'''
This file is part of DoctestAll.

DoctestAll is free software: you can redistribute it and/or modify it
under the terms of the GNU Lesser Public License as published by the 
Free Software Foundation, either version 3 of the License, or (at 
your option) any later version.

DoctestAll is distributed in the hope that it will be 
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser Public License for more details.

You should have received a copy of the GNU Lesser Public License
along with DoctestAll.  If not, see 
<http://www.gnu.org/licenses/>.
'''

# LIBRARY MODULE

import doctest

def test_recursive(mod, debug=False):
    # Accept strings, import
    if isinstance(mod, str):
        mod = __import__(mod, fromlist=[""])
    if debug:
        print("Testing " + mod.__name__)

    # Set up counts while testing self
    (failure_count, test_count) = doctest.testmod(mod)

    # Test children
    children = []
    if "__doctestall__" in dir(mod):
        children = mod.__doctestall__
    elif "__all__" in dir(mod):
        children = mod.__all__

    for child in children:
        childname = mod.__name__+"."+child
        cf, ct = test_recursive(childname, debug)
        failure_count += cf
        test_count    += ct

    # Done
    return (failure_count, test_count)

def test_toplevel(mod, debug = False):
    failures, tests = test_recursive(mod, debug)
    print("%d failures, %d tests." % (failures, tests))
    return (failures, tests)

#
# Copyright 2021 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import sys

from java.lang import Exception
from java.io import PrintWriter
from java.io import StringWriter

from com.xebialabs.overthere import CmdLine, ConnectionOptions, OperatingSystemFamily, Overthere
from com.xebialabs.overthere.local import LocalConnection
from com.xebialabs.overthere.ssh import SshConnectionBuilder, SshConnectionType
from com.xebialabs.overthere.util import CapturingOverthereExecutionOutputHandler, OverthereUtils
import com.xebialabs.xlrelease.plugin.ansible.RemoteScript as RemoteScript
from skopeo.SkopeoRunner import SkopeoRunner


if source_registry is None:
    if source_registry_name is None:
        print "Source Registry or Source Registry name should be configured"
        sys.exit(-1)
    else:
        skopeoRegistries = configurationApi.searchByTypeAndTitle("skopeo.Registry", source_registry_name)
        if len(self.skopeoRegistries) == 1:
            source_registry = skopeoRegistries[0]
        else:
            print "Error : Cannot find Skopeo Registry by name " + source_registry_name
            sys.exit(-1)

if target_registry is None:
    if target_registry_name is None:
        print "Target Registry or Target Registry name should be configured"
        sys.exit(-1)
    else:
        skopeoRegistries = configurationApi.searchByTypeAndTitle("skopeo.Registry", target_registry_name)
        if len(self.skopeoRegistries) == 1:
            target_registry = skopeoRegistries[0]
        else:
            print "Error : Cannot find Skopeo Registry by name " + source_registry_name
            sys.exit(-1)


skopeoRun = SkopeoRunner(source_registry, source_image, target_registry, target_image, host, skopeo_bin)


returnCode = skopeoRun.execute()

output = skopeoRun.getStdout()
errorOutput = skopeoRun.getStderr()

if len(output) > 0:
    print "```"
    print output
    print "```"
else:
    print "----"
    print "#### Output:"
    print "```"
    print output
    print "```"

    print "----"
    print "#### Error stream:"
    print "```"
    print errorOutput
    print "```"
    print

    sys.exit(response.rc)
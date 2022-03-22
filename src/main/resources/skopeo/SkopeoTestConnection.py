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



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

from com.xebialabs.overthere.util import CapturingOverthereExecutionOutputHandler
from com.xebialabs.overthere import CmdLine, ConnectionOptions, OperatingSystemFamily, Overthere
from com.xebialabs.overthere.local import LocalConnection
from com.xebialabs.overthere.ssh import SshConnectionBuilder, SshConnectionType

class SkopeoRunner():

   def __init__(self, sourceRegistry,sourceImage, targetRegistry, targetImage, runnerHost, skopeoBin = "skopeo"):

      self.cmdLine = CmdLine()
      self.cmdLine.addArgument( skopeoBin )
      self.cmdLine.addArgument( 'copy' )

      if sourceRegistry["token"] is not None:
         self.cmdLine.addArgument( '--src-creds' )
         self.cmdLine.addArgument( sourceRegistry["token"])

      if targetRegistry["token"] is not None:
         self.cmdLine.addArgument( '--dest-creds' )
         self.cmdLine.addArgument( targetRegistry["token"])
      
      self.sourceImage = sourceRegistry['registryUrl'] + "/" + sourceImage
      self.targetImage = targetRegistry['registryUrl'] + "/" + targetImage


      self.cmdLine.addArgument( self.sourceImage)
      self.cmdLine.addArgument( self.targetImage)

      self.runnerHost = runnerHost

      self.stdout = CapturingOverthereExecutionOutputHandler.capturingHandler()
      self.stderr = CapturingOverthereExecutionOutputHandler.capturingHandler()
   
   # End Init

   def getConnection(self):
      connection = None
      if self.runnerHost is not None:
         print "Run promotion remotly on %s" % self.runnerHost['address']
         options = ConnectionOptions()
         options.set(ConnectionOptions.USERNAME, self.runnerHost.get("username"))
         options.set(ConnectionOptions.ADDRESS, self.runnerHost.get("address"))
         options.set(SshConnectionBuilder.PRIVATE_KEY_FILE, self.runnerHost.get("privateKeyFile"));
         options.set(ConnectionOptions.OPERATING_SYSTEM, OperatingSystemFamily.UNIX)
         options.set(SshConnectionBuilder.OPEN_SHELL_BEFORE_EXECUTE, True)
         options.set(ConnectionOptions.OPERATING_SYSTEM, OperatingSystemFamily.UNIX)
         options.set(SshConnectionBuilder.CONNECTION_TYPE, SshConnectionType.SCP)


         connection = Overthere.getConnection("ssh", options)
      else:
         print "Run promotion locally"
         connection = LocalConnection.getLocalConnection()
      return connection
   # End getConnection

   def execute( self ):
      connection = None
      try:
         connection = self.getConnection()
         print "Promote image %s to %s " % (self.sourceImage, self.targetImage)

         exitCode = connection.execute( self.stdout, self.stderr, self.cmdLine )
      except Exception, e:
            stacktrace = StringWriter()
            writer = PrintWriter(stacktrace, True)
            e.printStackTrace(writer)
            self.stderr.handleLine(stacktrace.toString())
            return 1
      finally:
            if connection is not None:
                connection.close()
      return exitCode
   # End execute

   def getStdout(self):
        return self.stdout.getOutput()
   # End getStdout

   def getStdoutLines(self): 
        return self.stdout.getOutputLines()
   # End getStdoutLines

   def getStderr(self):
        return self.stderr.getOutput()
   # End getStderr

   def getStderrLines(self):
        return self.stderr.getOutputLines()
   # End getStderrLines
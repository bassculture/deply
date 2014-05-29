import paramiko
import sys
import os

config = sys.argv[1]
config_module = __import__(config, globals(), locals(), -1)

site = config_module.Site();
if site.protocol != 'sftp':
  raise 'Protocol ' + site.protocol.toString() + ' not supported'

transport = paramiko.Transport((site.host, site.port))
transport.connect(username = site.username, password = site.password)
sftp = paramiko.SFTPClient.from_transport(transport)

for f in config_module.Puts():
    print f.local + ' --> ' + f.remote
    sftp.put(f.local, f.remote)
    if (f.chmod is not None):
        print 'Setting permissions for ' + f.remote
        sftp.chmod(f.remote, f.chmod)

sftp.close()
transport.close()
print 'Upload done.'
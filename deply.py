class Target:
    
  def __init__(self, local, remote, chmod = None):
    self.local = local
    self.remote = remote
    self.chmod = chmod

class Site:
  
  protocol = 'sftp'
  
  def __init__(self, host, port, username, password, protocol = 'sftp'):
    self.host = host
    self.port = port
    self.username = username
    self.password = password
    self.protocol = protocol


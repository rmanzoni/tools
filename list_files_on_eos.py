import subprocess
import sys

def listfiles(eosfolder) :
  proc = subprocess.Popen(['/afs/cern.ch/project/eos/installation/0.3.15/bin/eos.select','ls',eosfolder],stdout=subprocess.PIPE)
  files = []
  for line in proc.stdout:
    files.append('root://eoscms//eos/cms/'+eosfolder+'/'+line.rstrip())
  return files

if len(sys.argv)<2:
  print 'you need to specify which folder to inspect'
  exit()
else :
  eosfolder = sys.argv[1]
  files = listfiles(eosfolder)
  for file in files : print file

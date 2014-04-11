import os
import sys
import subprocess
from optparse import OptionParser



def last_change_date(filename, humanReadable = False):
    t = os.path.getctime(filename)
    if humanReadable : return datetime.datetime.fromtimestamp(t)
    else             : return t    
    
    
parser = OptionParser()
parser.usage = '''


%prog <samples_pub.txt> options

samples in samples_pub.txt should be formatted like (as you would do for publish.py)
/Tau/Run2012A-13Jul2012-v1/AOD/V5_B/PAT_CMG_V5_14_0/HTT_22Apr_manzoni_Nom manzoni
or 
/Tau/Run2012A-13Jul2012-v1/AOD/V5_B/PAT_CMG_V5_14_0/HTT_22Apr_manzoni_Nom
or
manzoni%/Tau/Run2012A-13Jul2012-v1/AOD/V5_B/PAT_CMG_V5_14_0/HTT_22Apr_manzoni_Nom


'''
parser.add_option("-Q", "--queue"      , dest = "queue"      ,  help = "choose queue. Available 1nh 8nh 1nd 2nd 1nw 2nw. Default is 1nd" , default = '1nd'     )
parser.add_option("-R", "--resubmit"   , dest = "resubmit"   ,  help = "Resubmit after jobreport.py. Default False"                      , default = False     )
parser.add_option("-U", "--user"       , dest = "user"       ,  help = "username of owner of the samples. Default manzoni"               , default = 'manzoni' )
parser.add_option("-T", "--tuple"      , dest = "tuple"      ,  help = "pattern to look for in sample directory. Default diTau"          , default = 'diTau'   )
parser.add_option("-E", "--edmintcheck", dest = "edmintcheck",  help = "run edmIntegrityCheck.py. Default False"                         , default = False     )
parser.add_option("-P", "--publish"    , dest = "publish"    ,  help = "publish.py dataset if it is fine. Default False"                 , default = False     )
parser.add_option("-L", "--logger"     , dest = "logger"     ,  help = "compress and cmsStage the Logger file to eos. Default False"     , default = False     )

(options,args) = parser.parse_args()

try:
  fname = args[0]
except:
  print 'provide the list of samples to check'
  print 'usage: resubmitter.py samples_pub.txt queue'
  sys.exit(0)  

try :
  os.path.isfile(fname)
except :
  print 'unknown file'
  print 'usage: resubmitter.py samples_pub.txt queue'
  sys.exit(0)  

queue = options.queue

if queue not in ['1nh','8nh','1nd','2nd','1nw','2nw'] :
  print 'unknown queue. Available queues: 1nh 8nh 1nd 2nd 1nw 2nw'
  print 'usage: resubmitter.py samples_pub.txt queue'
  sys.exit(0)  

fname = args[0]
print 'reading samples to check from', fname

with open(fname) as f:
  content = f.readlines()

for c in content :
  if c.replace(' ','') == '' or c.replace(' ','') == '\n' :
    content.remove(c)

for c in content :
  c = c[c.find('%')+1:]
  sample = c.split(' ')[0]
  if options.edmintcheck :
    print 'executing integrity check'
    ic = "edmIntegrityCheck.py --update -u {USER} -p -w '*.root' {SAMPLE}".format(USER = options.user, SAMPLE = sample)
    print ic
    os.system(ic)
  #command = "jobreport.py -u {USER} {SAMPLE} . -p '{TUPLE}.*root'".format(USER=options.user,SAMPLE=sample,TUPLE=options.tuple) # old version of jobreport.py
  command = "jobreport.py -u {USER} {SAMPLE} .".format(USER=options.user,SAMPLE=sample)
  command = command.replace('\n','')  
  print command
  cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  
  for line in cmd.stdout:
    line = line.rstrip()
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.replace(' ','')
    toResubmit = line.split(',') 
  
  folder = sample.split('/')
  
  wd = os.getcwd()
  go = True
  try :
    os.listdir('/'.join([folder[1],folder[2]]))
  except :
    print 'WARNING!! Likely production of sample:\n',sample,'didn\'t even start'
    go = False
  
  if go :  
    os.chdir('/'.join([folder[1],folder[2]]))
    if 'V5' in folder or 'V5_B' in folder :
      maxDepth = 3
    else :
      maxDepth = 2
    i = 0
    while i <= maxDepth :
      if len(os.listdir(os.getcwd()))>1 :
        change_time = 0
        newFolder   = []
        for d in os.listdir(os.getcwd()) : 
          if last_change_date(d) > change_time :
            newFolder = [d]
      else :
        newFolder = os.listdir(os.getcwd())
          
      #for d in os.listdir(os.getcwd()) : 
      for d in newFolder : 
        #import pdb ; pdb.set_trace()
        if os.path.isdir(d) :
          os.chdir(d)
          #print os.getcwd()
          i += 1
          
    if '' in toResubmit : toResubmit.remove('')      
    print 'I am going to resubmit', len(toResubmit),'file(s) on queue', queue
    print toResubmit
    
    if options.logger :
      #import pdb ; pdb.set_trace()
      print 'compressing Logger folder'
      print 'tar -cvzf Logger.tgz Logger'
      os.system('tar -cvzf Logger.tgz Logger')
      eosFolder = os.getcwd()
      eosFolder = eosFolder.replace(wd,'')
      eosFolder = eosFolder.split('/')
      eosFolder[-1] = eosFolder[-1].replace('_Jobs','')
      eosFolder[-2] = '_'.join(eosFolder[-2].split('_')[:-1])
      eosFolder = ['','store','cmst3','user',options.user,'CMG']+eosFolder
      eosFolder = '/'.join(eosFolder)
      #import pdb ; pdb.set_trace()
      print 'staging Logger file'
      print 'cmsStage Logger.tgz '+ eosFolder
      os.system('cmsStage Logger.tgz '+ eosFolder)
    
    if len(toResubmit) > 0 and options.resubmit:
      for i in toResubmit :
        print 'cd Job_'+i+'/; bsub -q '+queue+' < batchScript.sh ; cd -'
        os.system('cd Job_'+i+'/; bsub -q '+queue+' < batchScript.sh ; cd -')

  if options.publish and len(toResubmit) == 0 :
    print 'going to publish.py the dataset'
    pub = "publish.py -f -u {USER} {SAMPLE}".format(USER = options.user, SAMPLE = sample)
    print pub
    os.system(pub)
      
  os.chdir(wd)
  
  print ''
  print ''

  



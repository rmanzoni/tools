import os, re, sys

masses  = ['100','120','130','140','160','180','200','250','300','350','500','600','900','1000']
#masses  = ['100','120','130','140','160','180','200','250','300','350','500','600','900','1000']

for mass in masses :
  path = '/store/cmst3/group/cmgtools/CMG/SUSYBBHToTauTau_M-'+mass+'_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM/PAT_CMG_5_6_0_B'
  if len(sys.argv) > 1:
      print len(sys.argv)
      path = sys.argv[1]

  print '\n\n'   
  print '*'*(len('inspecting this folder: '+path)+6) 
  print '** inspecting this folder:', path,'**' 
  print '*'*(len('inspecting this folder: '+path)+6) 
    
  dir = os.popen("/afs/cern.ch/project/eos/installation/0.1.0-22d/bin/eos.select ls -latrh " + path + " | grep manzoni | grep cmg")
  manzoniFiles = dir.readlines()
  dir = os.popen("/afs/cern.ch/project/eos/installation/0.1.0-22d/bin/eos.select ls -latrh " + path + " | grep kkaadze | grep cmg")
  ketinoFiles = dir.readlines()
  
  
  if len(ketinoFiles) > 0:
      print "Here are manzoni's file "
      filesToDelete = []
      for i in manzoniFiles:
          newFile = path + "/cmgTuple" + re.split("cmgTuple", i)[1][:-1]
          filesToDelete += [newFile,]
          os.system("echo  " + newFile)
          #os.system('/afs/cern.ch/project/eos/installation/0.1.0-22d/bin/eos.select rm '+ newFile)
  else:
      print "No kkaadze files are found, here are manzoni's files:"
      for i in manzoniFiles:
          newFile = path + "/cmgTuple" + re.split("cmgTuple", i)[1][:-1]
          print newFile



masses2  = ['90','120','130','140','200','400','450','500','600','700','800','900','1000']

for mass in masses2 :
  path = '/store/cmst3/group/cmgtools/CMG/SUSYGluGluToHToTauTau_M-'+mass+'_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM/PAT_CMG_5_6_0_B'
  if len(sys.argv) > 1:
      print len(sys.argv)
      path = sys.argv[1]

  print '\n\n'   
  print '*'*(len('inspecting this folder: '+path)+6) 
  print '** inspecting this folder:', path,'**' 
  print '*'*(len('inspecting this folder: '+path)+6) 
    
  dir = os.popen("/afs/cern.ch/project/eos/installation/0.1.0-22d/bin/eos.select ls -latrh " + path + " | grep manzoni | grep cmg")
  manzoniFiles = dir.readlines()
  dir = os.popen("/afs/cern.ch/project/eos/installation/0.1.0-22d/bin/eos.select ls -latrh " + path + " | grep kkaadze | grep cmg")
  ketinoFiles = dir.readlines()
  
  
  if len(ketinoFiles) > 0:
      print "Here are manzoni's file "
      filesToDelete = []
      for i in manzoniFiles:
          newFile = path + "/cmgTuple" + re.split("cmgTuple", i)[1][:-1]
          filesToDelete += [newFile,]
          os.system("echo  " + newFile)
          #os.system('/afs/cern.ch/project/eos/installation/0.1.0-22d/bin/eos.select rm '+ newFile)
  else:
      print "No kkaadze files are found, here are manzoni's files:"
      for i in manzoniFiles:
          newFile = path + "/cmgTuple" + re.split("cmgTuple", i)[1][:-1]
          print newFile
         

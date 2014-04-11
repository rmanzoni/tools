import os

path = os.getcwd()

dirList = os.listdir(os.getcwd())

#for fname in ['DYJets'] :
for fname in dirList:
  if not os.path.isdir(fname) : continue
  if 'DY' in fname : continue
  toSkim = '/'.join([path,fname,'H2TauTauTreeProducerTauTau','H2TauTauTreeProducerTauTau_tree.root'])
  os.system('/afs/cern.ch/user/m/manzoni/.utils/tree_trimmer.py -t H2TauTauTreeProducerTauTau -b /afs/cern.ch/user/m/manzoni/.utils/branches.txt -s skimming2 {TOSKIM} /afs/cern.ch/user/m/manzoni/.utils/skim.py'.format(TOSKIM=toSkim))
  #import pdb ; pdb.set_trace()
  os.system('mv {OLDFILE} {NEWFILE}'.format(OLDFILE=toSkim, NEWFILE=toSkim.replace('.root','_PRESKIM.root')))
  #import pdb ; pdb.set_trace()
  os.system('mv {SKIMMED} {OLDFILE}'.format(SKIMMED='/'.join([path,'skim.root']),OLDFILE=toSkim))  
  
  
  #forStitching = '/'.join([path,fname,'H2TauTauTreeProducerTauTau','forStitching.root'])
  #os.system('mv {SKIMMED} {OLDFILE}'.format(SKIMMED='/'.join([path,'skim.root']),OLDFILE=forStitching))  







from ROOT import TFile, TH1F, gDirectory
import os
import datetime

now = datetime.datetime.now()
rootlogon = 'rootlogon_'+str(now.day)+'_'+str(now.month)+'_'+str(now.year)+'.C'

print os.getcwd()+'/'+rootlogon

out_file = open(os.getcwd()+'/'+rootlogon,'w')
out_file.write('#include <iostream.h> \n#include <stdio.h>    \n#include <math.h>     \n\n')
out_file.write(rootlogon.replace('.C','()')+'{\n}\n\n')

dirList = os.listdir(os.getcwd())
fileNames = []
for fname in dirList:
  if os.path.isdir(fname) : continue
  if ( ( "BOOSTED" in fname or "VBF" in fname ) and ".root" in fname ):
    if "PLOT" in fname and "_QCD_" in fname and "mH125" in fname and "CORRELATIONS" not in fname :
      print 'File Found: ', fname
      fileNames.append(fname)

directories = [('dRtt','1./3.','QCDlooseOS_QCDlooseSS_ratio'),('nVert','0.5','QCDtightSS_QCDlooseSS_ratio')]

for name in fileNames :
  file = TFile.Open(name,'read')
  for sys in ['_nom','_dR2','_dR3','_iso04','_iso06'] :
    if sys in name :
      systematic = sys
  
  for dir, width, ratio in directories :
    file.cd(dir)
    hist = gDirectory.FindObjectAny(ratio)

    nBins = hist.GetNbinsX()+1
    
    out_file.write('float weightQCD'+systematic+'_'+dir+'(float '+dir+') {\n')
    out_file.write('  int '+dir+'Bin = int('+dir+'/('+width+')) ;\n')
    out_file.write('  '+dir+'Bin = '+dir+'Bin+1 ;\n')
    out_file.write('    float w['+str(nBins)+'] ;\n')
    
    for bin in range(nBins) :
      #print 'bin', bin, ':', hist.GetBinContent(bin)
      out_file.write('    w['+str(bin)+'] = '+str(hist.GetBinContent(bin))+' ;\n')
    
    out_file.write('  if ('+dir+'Bin < '+str(nBins)+' && fabs(w['+dir+'Bin]) < 3. && w['+dir+'Bin] > 0. ){\n')
    out_file.write('    return w['+dir+'Bin] ;\n')
    out_file.write('  }\n')
    out_file.write('  else{\n')
    out_file.write('    return 1. ;\n')
    out_file.write('  }\n')
    out_file.write('}\n\n')
 
  file.Close()
  
out_file.close()


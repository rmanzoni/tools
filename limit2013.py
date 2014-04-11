import os
import inspect

def lineno():
  '''Returns the current line number in our program.'''
  return inspect.currentframe().f_back.f_lineno

from optparse import OptionParser

parser = OptionParser()
parser.usage = '''
%prog [options]

bla bla
to be written

'''
parser.add_option("-M", "--masses"       , dest = "masses"       , help = "masses: all ==> 110,145:5 or any within that range. [Default 125]" , default = "125"     )
parser.add_option("-O", "--observed"     , dest = "observed"     , help = "observed limit. [Default False]"                                   , default = False     )
parser.add_option("-S", "--significance" , dest = "significance" , help = "expected significance. [Default False]"                            , default = False     )
parser.add_option("-P", "--pulls"        , dest = "pulls"        , help = "pulls at mH 125. [Default False]"                                  , default = False     )
parser.add_option("-C", "--categories"   , dest = "categories"   , help = "tt categories: 0 boost, 1 vbf. [Default \'0 1\']"                  , default = '\"0 1\"' )
    
(options,args) = parser.parse_args()

if options.masses == 'all'                                             : mass = '110 115 120 125 130 135 140 145'
if options.masses in ['110','115','120','125','130','135','140','145'] : mass = options.masses

wd = os.getcwd()
wd += '/Combined'

folders = []
dirList = os.listdir(wd)
print dirList
print 'categories:', options.categories 
for fname in dirList:
  print fname, os.path.isdir( '/'.join([wd,fname]) )
  if os.path.isdir( '/'.join([wd,fname]) ) :
    if 'CMS_2012_' not in fname                        : continue
    if ('BOOSTED' not in fname and 'VBF' not in fname) : continue
    folders.append(fname)

fileName = 'htt_tt.inputs-sm-8TeV.root'

print folders
for fol in folders :
  os.system( 'cp '+'/'.join([wd,fol,fileName])+' '+'/'.join([os.environ.get('CMSSW_BASE'),'src','setups','std','tt']) )
  os.chdir( '/'.join([os.environ.get('CMSSW_BASE'),'src']) )
  os.system( 'eval `scramv1 runtime -csh`' ) ## cmsenv
  os.system( 'add_bbb_errors.py \'tt:8TeV:00,01:ZTT,QCD\' -i setups/std -f -o setups/std-bin-by-bin --normalize --threshold 0.10' )
  os.system( 'cp setups/std-bin-by-bin/tt/* HiggsAnalysis/HiggsToTauTau/setup/tt/')
  os.system( 'rm MY-LIMITS/tt/common/*' )
  os.system( 'setup-datacards.py --channels="tt" -p "8TeV" '+mass+' --sm-categories-tt='+options.categories )
  os.system( 'setup-htt.py -o MY-LIMITS '+mass+' --channels="tt" -p "8TeV" -i auxiliaries/datacards/ --sm-categories-tt='+options.categories )
  for m in mass.split() :
    os.system( 'limit.py --expectedOnly --asymptotic --userOpt \'-t-1 --minosAlgo stepping\' MY-LIMITS/tt/'+m+' >& ' + '/'.join([wd,fol,'expOnlyLimit'+m+'.txt']) )
    if options.observed :
      os.system( 'limit.py --asymptotic --userOpt \'--minosAlgo stepping\' MY-LIMITS/tt/'+m+' >& ' + '/'.join([wd,fol,'obsLimit'+m+'.txt']) )
    if options.pulls :  
      os.system( 'limit.py --max-likelihood --stable --rMin -5 --rMax 5 MY-LIMITS/tt/125 >& ' + '/'.join([wd,fol,'pulls125.txt']) )
    #if options.significance :
    #  os.system( 'limit.py --max-likelihood --stable --rMin -5 --rMax 5 MY-LIMITS/tt/125 >& ' + '/'.join([wd,fol,'pulls125.txt']) )      
    #os.system( 'cp MY-LIMITS/tt/'+m+'/* ' + '/'.join([wd,fol]) )
    #os.system( 'cp MY-LIMITS/tt/common/* ' + '/'.join([wd,fol,fileName.replace('.root','.new.root')]) )
  os.system( 'cp -r MY-LIMITS/tt/* ' + '/'.join([wd,fol]) )
  
  
  
  
  
  
  
  
  

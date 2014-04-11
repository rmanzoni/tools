#!/usr/bin/python

import os
from optparse import OptionParser

parser = OptionParser()
parser.usage = '''
%prog <crabDir> 

crabDir: folder you want to inspect, get output and resubmit failed jobs

'''

parser.add_option("-f", "--forcePending", 
                  dest="force", 
                  help="forceResubmit for pending, stuck, unknown jobs (the ones you cannot getOutput of)",
                  default=False)

parser.add_option("-F", "--forceAll", 
                  dest="forceAll", 
                  help="forceResubmit for all jobs that are not Successfully Done",
                  default=False)

(options,args) = parser.parse_args()

if len(args) != 1:
    parser.print_help()
    sys.exit(1)

crabDir = args[0]

print '#'*(len(crabDir)+10)
print '##  ',crabDir,'  ##'
print '#'*(len(crabDir)+10)

fileName   = os.getcwd()+'/report_'+crabDir+'.txt'
reportFile = open(fileName,'w')

print >> reportFile, 'noknaosjdoai'

os.system('crab -status -c '+crabDir)
os.system('crab -status -c '+crabDir+' >& '+reportFile)



reportFile.close()





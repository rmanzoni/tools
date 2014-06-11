import os
from sys      import argv     as av
from copy     import deepcopy as dc
from optparse import OptionParser
from ROOT     import TFile, gDirectory


parser = OptionParser()
parser.usage = '''
customDatacard.py folder1:name_of_the_category1 folder2:name_of_the_category2 ... [OPTIONS]

EXAMPLE:
customDatacard.py CMS_2012_tight_VBF_nom:tight_vbf CMS_2012_tight_BOOSTED_nom:tight_boost CMS_2012_loose_BOOSTED_nom:loose_boost CMS_2012_loose_VBF_nom:loose_vbf
'''
parser.add_option("-N", "--shift" , dest = "shift" ,  help = "save the up, down shifts. Default is True"    , default = True       )
parser.add_option("-S", "--susy"  , dest = "susy"  ,  help = "susy datacard. Default is False"              , default = False      )
parser.add_option("-F", "--file"  , dest = "file"  ,  help = "filename. Default is '' "                     , default = ''         )
parser.add_option("-M", "--mass"  , dest = "mass"  ,  help = "mass. Default is svfitMass, optional visMass" , default = 'svfitMass')
parser.add_option("-V", "--vh"    , dest = "vh"    ,  help = "merge ttH, WH and ZH into VH"                 , default = True      )

(options,av) = parser.parse_args()

#print 'Merge VH ? ', options.vh
print av
print options

if options.susy : filename = 'htt_tt.inputs-mssm-8TeV-0.root'
else            : filename = 'htt_tt.inputs-sm-8TeV.root'

if options.mass == 'visMass' :
  filename = filename.replace('.root','-mvis.root')

if options.file != '' : filename = options.file

hists = {}

for category in av :

  cat_fold = category.split(':')[0]
  cat_name = category.split(':')[1]

  if options.shift :
    for n in ['_nom','_up','_down'] :
      cat_fold = cat_fold.replace(n,'')

  else :
    for n in ['_nom'] :
      cat_fold = cat_fold.replace(n,'')

  hists.update({cat_name:[]})

  if 'BOOSTED' in cat_fold : cat = 'boost'
  if 'VBF'     in cat_fold : cat = 'vbf'

  f1 = TFile(cat_fold+'_nom/'+cat_fold+'_nom_tauTau_'+cat+'_'+options.mass+'.root','read')
  dir = 'tauTau_'+cat
  f1.cd(dir)
  dirList = gDirectory.GetListOfKeys()
  sum_vh = []
  
  for k1 in dirList:
    h1 = k1.ReadObj()
    hh = dc(h1)

    if 'ZTT' in hh.GetName() or 'QCD' in hh.GetName() :
      for bin in range(hh.GetNbinsX()+1) :
        if hh.GetBinError(bin) == 0 :
          hh.SetBinError(bin, 1.)
    print h1.GetName()
    if (h1.GetName()=='ttH125' or h1.GetName()=='WH125' or h1.GetName()=='ZH125') and options.vh :
      sum_vh.append(dc(h1))
      continue

    hists[cat_name].append(hh)
    
  if options.vh :
    vh = dc(sum_vh[0])
    vh.Add(sum_vh[1])
    vh.Add(sum_vh[2])
    vh.SetName('VH125')
    hists[cat_name].append(vh)


  f1.Close()


  if options.shift :
    f2 = TFile(cat_fold+'_up/'+cat_fold+'_up_tauTau_'+cat+'_'+options.mass+'.root','read')
    dir = 'tauTau_'+cat
    f2.cd(dir)
    dirList = gDirectory.GetListOfKeys()
    sum_vh = []

    for k2 in dirList:
      h2 = k2.ReadObj()
      if 'ZTT' in h2.GetName() or \
         'qqH' in h2.GetName() or \
         'ggH' in h2.GetName() or \
         'VH'  in h2.GetName() or \
         'WH'  in h2.GetName() or \
         'ZH'  in h2.GetName() or \
         'ttH' in h2.GetName() or \
         'bbH' in h2.GetName() or \
         'QCD' in h2.GetName() :
        if (h2.GetName()=='ttH125' or h2.GetName()=='WH125' or h2.GetName()=='ZH125') and options.vh :
          sum_vh.append(dc(h2))
          continue
        hh = dc(h2)
        hh.SetName(hh.GetName()+'_CMS_scale_t_tautau_8TeVUp')
        hists[cat_name].append(hh)

    if options.vh :
      vh = dc(sum_vh[0])
      vh.Add(sum_vh[1])
      vh.Add(sum_vh[2])
      vh.SetName('VH125_CMS_scale_t_tautau_8TeVUp')
      hists[cat_name].append(vh)
    f2.Close()

    f3 = TFile(cat_fold+'_down/'+cat_fold+'_down_tauTau_'+cat+'_'+options.mass+'.root','read')
    dir = 'tauTau_'+cat
    f3.cd(dir)
    dirList = gDirectory.GetListOfKeys()
    sum_vh = []
    for k3 in dirList:
      h3 = k3.ReadObj()
      if 'ZTT' in h3.GetName() or \
         'qqH' in h3.GetName() or \
         'ggH' in h3.GetName() or \
         'VH'  in h3.GetName() or \
         'WH'  in h3.GetName() or \
         'ZH'  in h3.GetName() or \
         'ttH' in h3.GetName() or \
         'bbH' in h3.GetName() or \
         'QCD' in h3.GetName() :
        if (h3.GetName()=='ttH125' or h3.GetName()=='WH125' or h3.GetName()=='ZH125') and options.vh :
          sum_vh.append(dc(h3))
          continue
        hh = dc(h3)
        hh.SetName(hh.GetName()+'_CMS_scale_t_tautau_8TeVDown')
        hists[cat_name].append(hh)
    if options.vh :
      vh = dc(sum_vh[0])
      vh.Add(sum_vh[1])
      vh.Add(sum_vh[2])
      vh.SetName('VH125_CMS_scale_t_tautau_8TeVDown')
      hists[cat_name].append(vh)
    f3.Close()

#print [ h.GetName() for h in hists['boost_tight']]

tot = TFile(filename,'recreate')
for d in hists.keys():
  tot.mkdir('tauTau_'+d)
  tot.cd('tauTau_'+d)

  alreadyIn = []

  for h in hists[d] :
    if h.GetName() not in alreadyIn:
      if '_fine_binning' in h.GetName() :
        oldname = h.GetName()
        newname = oldname.replace('_fine_binning','')
        newname = newname+'_fine_binning'
        h.SetName(newname)
      alreadyIn.append(h.GetName())
      alreadyIn.append(oldname)
      h.Write()
  tot.cd('..')
tot.Close()


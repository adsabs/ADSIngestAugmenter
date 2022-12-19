import os

# data files for bibstem selection
ISSN2BIBSTEM_file = os.path.realpath(os.path.join(os.path.dirname(__file__), './')) + '/bibcode_data/issn2bibstem.txt'
NAME2BIBSTEM_file = os.path.realpath(os.path.join(os.path.dirname(__file__), './')) + '/bibcode_data/name2bibstem.txt'

ISSN2BIBSTEM = dict()
with open(ISSN2BIBSTEM_file, 'r') as fi:
    for l in fi.readlines():
        (issn, bibstem) = l.strip().split('\t')
        ISSN2BIBSTEM[issn] = bibstem

NAME2BIBSTEM = dict()
with open(NAME2BIBSTEM_file, 'r') as fi:
    for l in fi.readlines():
        (bibstem, name) = l.strip().split('\t')
        NAME2BIBSTEM[name] = bibstem

APS_BIBSTEMS = ['PhRvL', 'PhRvX', 'RvMP.', 'PhRvA', 'PhRvB', 'PhRvC', 'PhRvD', 'PhRvE', 'PhRvS', 'PhRvS', 'PhRvP', 'PhRvF', 'PhRvM', 'PRPER', 'PRSTP', 'PhRv.', 'PhRvI', 'PhyOJ', 'PhRvR']

IOP_BIBSTEMS = ['ApJ..', 'JCAP.', 'EJPh.', 'RAA..', 'PhyM.', 'JPhD.', 'AJ...', 'APExp', 'ApJL.', 'ApJS.', 'BiBi.', 'BioFa', 'BioMa', 'CQGra', 'ChPhC', 'CoTPh', 'EL...', 'ERCom', 'ERExp', 'ERL..', 'EleSt', 'FCS..', 'FlDyR', 'IzMat', 'JBR..', 'JOpt.', 'JPCM.', 'JPEn.', 'JPhA.', 'JPhB.', 'JPhCo', 'JPCom', 'JSSST', 'IOPSN', 'JPhG.', 'JPhM.', 'JPhP.', 'LaPhL', 'MRE..', 'MatQT', 'MLS&T', 'MeScT', 'MuMat', 'NanoE', 'NJPh.', 'NanoF', 'Nanot', 'Nonli', 'PASP.', 'Metro', 'PMB..', 'PPCF.', 'PlREx', 'PhyS.', 'PhyEd', 'PSJ..', 'PhyU.', 'PlST.', 'PrEne', 'RNAAS', 'RPPh.', 'RuMaS', 'SeScT', 'SuScT', 'TDM..', 'TDM..', 'JElS.', 'TDM..', 'ERIS.', 'ECSMA', 'PBioE', 'RuCRv', 'NucFu', 'JMiMi', 'ChPhL', 'InvPr', 'JRP..', 'PSST.', 'SMaS.', 'MSMSE', 'QuEle', 'SbMat', 'JaJAP', 'ANSNN', 'MApFl', 'SuTMP', 'QS&T.', 'E&ES.', 'MS&E.', 'PhBio', 'LaPhy', 'ChPhB', 'JSemi', 'JNEng', 'JGE..', 'JSMTE', 'JPhCS', 'PhyW.', 'PPS..', 'JPhC.', 'JPhF.', 'IJExM', 'ECSTr', 'JInst', 'NanoE']

OUP_BIBSTEMS = ['MNRAS', 'PASJ.', 'PTEP.', 'GeoJI']

AIP_BIBSTEMS = ['AIPA.', 'AIPC.', 'ApPhL', 'APL..', 'APLM.', 'APLP.', 'AVSQS', 'AmJPh', 'ApPRv', 'Chaos', 'JAP..', 'JChPh', 'JMP..', 'JPCRD', 'LTP..', 'PhFl.', 'PhPl.', 'PhTea', 'RScI.']

SPRINGER_BIBSTEMS = ['A&ARv', 'AAM..', 'AAnST', 'ACME.', 'AeMiS', 'AJPAS', 'AMGBA', 'AMGBB', 'AnHP.', 'AnSSM', 'ApNan', 'APhy.', 'APPSB', 'ApWS.', 'ARIJ.', 'ARep.', 'AcGeo', 'AcMSn', 'AcSSn', 'AdAer', 'AdAtS', 'AerSE', 'AerSy', 'AnGeo', 'Ap&SS', 'Ap...', 'ApCM.', 'ApGeo', 'ApPhy', 'ApPhA', 'ApPhB', 'ArM..', 'ArRMA', 'AstBu', 'AsDyn', 'AstL.', 'AtOO.', 'BeiMP', 'BGeod', 'BVol.', 'BVol.', 'BoLMe', 'BuLPI', 'BRASP', 'BrJPh', 'CEAS.', 'CEJE.', 'CEJG.', 'CEJPh', 'CESW.', 'CMMPh', 'CMT..', 'CMaPh', 'CeMec', 'CeMDA', 'ChJME', 'ChJOL', 'ClDy.', 'CmPhy', 'ComAC', 'CoMat', 'ComEE', 'CoMP.', 'CompM', 'CorRe', 'CosRe', 'CPM..', 'CryRp', 'CSBS.', 'CSSE.', 'CSSP.', 'CzJPh', 'CzJPS', 'DeHyZ', 'DiEne', 'DiMat', 'DISER', 'DiSus', 'DiWat', 'DokES', 'DokPh', 'EP&S.', 'EaSci', 'EEEV.', 'EFM..', 'EJASP', 'EM&P.', 'EML..', 'EnGeo', 'EES..', 'EnMan', 'EPJA.', 'EPJAS', 'EPJB.', 'EPJC.', 'EPJCS', 'EPJD.', 'EPJH.', 'EPJP.', 'EPJQT', 'EPJST', 'EScIn', 'ESE..', 'EurSS', 'ExA..', 'ExFl.', 'FBS..', 'FlDy.', 'FoPh.', 'FoPhL', 'FrME.', 'FrMS.', 'FrPhC', 'FrPhy', 'FTC..', 'Ge&Ae', 'GML..', 'GrCo.', 'GReGr', 'Geote', 'GeoPA', 'GeoOD', 'GeoRu', 'GeoSu', 'Grund', 'GSL..', 'HM...', 'HMR..', 'HMT..', 'HWM..', 'HyInt', 'HydJ.', 'IAM..', 'InJPh', 'INL..', 'IJASE', 'IJASS', 'IJBB.', 'IJBm.', 'IJEaS', 'IJEnR', 'IJIMW', 'IJMMD', 'IJMMM', 'IJMW.', 'IJT..', 'IJTP.', 'INL..', 'IREdu', 'IzAOP', 'IzPSE', 'JAMTP', 'JAnSc', 'JApA.', 'JApSp', 'JASMS', 'JCAMD', 'JDBM.', 'JEET.', 'JEMat', 'JEOS.', 'JEP..', 'JEPT.', 'JESS.', 'JETP.', 'JETPL', 'JHyDy', 'JIEI.', 'JIEIA', 'JIEIB', 'JIEIC', 'JIEID', 'JIEIE', 'JIMTW', 'JGS..', 'JGeod', 'JHEP.', 'JKPS.', 'JLTP.', 'JMarA', 'JMatR', 'JMEP.', 'JMFM.', 'JMSA.', 'JNMP.', 'JNR..', 'JNS..', 'JOM..', 'JOUC.', 'JPalA', 'JPalg', 'JPEle', 'JPRSG', 'JSedE', 'JSEdT', 'JSER.', 'JSP..', 'JSTEd', 'JSeis', 'JTAP.', 'JThSc', 'JTST.', 'JTePh', 'LMaPh', 'LMMP.', 'LaPhy', 'LRCA.', 'LRSP.', 'LRR..', 'MAMMP', 'MAP..', 'MCM..', 'MEdRJ', 'MecSM', 'MeSol', 'MMA..', 'MMTA.', 'MpNp.', 'MTB..', 'MMTB.', 'MT...', 'MTDM.', 'MarGR', 'MatTh', 'MicNa', 'MicST', 'MinDe', 'MinPe', 'M&P..', 'Moon.', 'MLST.', 'MMI..', 'MNSL.', 'MPAG.', 'MRSAd', 'MRSBu', 'MRSCo', 'MRSES', 'MSHT.', 'MWE..', 'MulSE', 'MUPB.', 'NanMe', 'NanoC', 'NatAs', 'NatCC', 'NatCh', 'NatCo', 'NatEn', 'NatGe', 'NatMa', 'NatNa', 'NatPh', 'NanRe', 'NatSy', 'NatRM', 'NatRP', 'NaPho', 'NatSD', 'NatSR', 'Natur', 'NCimR', 'NML..', 'npjAM', 'npjCM', 'npjCA', 'npjQI', 'npjQM', 'npjRM', 'npjSL', 'NRL..', 'NRvEE', 'NW...', 'OERv.', 'SLSci', 'OLEB.', 'OrLi.', 'OcDyn', 'Ocgy.', 'OIDP.', 'OptEL', 'OptNa', 'OptRv', 'OptSp', 'OQEle', 'OSJ..', 'PAN..', 'PApGe', 'PCM..', 'PCMPS', 'PEPS.', 'PFG..', 'PKM..', 'PMM..', 'Polyt', 'PPN..', 'PPNL.', 'PhP..', 'PhSen', 'PhSS.', 'PhyMe', 'PlPhR', 'PlSci', 'Prama', 'PWP..', 'QuIP.', 'R&QE.', 'RaF..', 'RCD..', 'RDTM.', 'RJMP.', 'RJPCA', 'RLSFN', 'RMFMR', 'RMRE.', 'RScEd', 'RSESS', 'RuAer', 'RuMet', 'RuPhJ', 'RvMPP', 'SGC..', 'SGeo.', 'SSRv.', 'Sc&Ed', 'ScChG', 'SciNa', 'SenIm', 'SHH..', 'ShWav', 'SMS..', 'ShMeS', 'SoPh.', 'SoSyR', 'StMat', 'SuEa.', 'SvApM', 'SvRP.', 'TAOS.', 'TDR..', 'TMP..', 'SCPMA', 'TePhL', 'Th&Ae', 'ThApC', 'ThCFD', 'ThEng', 'W&S..', 'WatWa', 'ZAGeo', 'ZaMP.', 'ZPhy.', 'ZPhyA', 'ZPhyB', 'ZPhyC', 'ZPhyD', 'KARJ.']

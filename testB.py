#!/usr/bin/python
#Reliable grad tests
'''
Tests Religrad
'''
import subprocess as proc
import sys, getopt, os
inputfile = ''
outputfile = ''
isovalue = ''
def readParameters(argv):
   global inputfile
   global isovalue
   global outputfile
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","iso="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> --iso <isovalue> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -iso <isovalue>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o"):
         outputfile = arg
      elif opt in ( "--isovalue"):
         isovalue = arg

cdist=[2]
extend_max=[2]

def run_ijkgradient_diff(f):
    ijkgradientdiff_loc = ['E:\\Programs\\Win\\stdAlone\\ijkgradientdiff_bin\\Release\\ijkgradientdiff.exe']
    ijkgradientdiff = [ijkgradientdiff_loc, '-minmag', '0.001','-ignore_small_mag',\
                       'either', '-total']
    ijkgradientdiff.append("out.grad.nrrd")
    ijkgradientdiff.append(inputfile.rpartition('.')[0] + '.grad.nrrd')
    o = proc.check_output(ijkgradientdiff)
    print(o.decode("utf-8"), file=f )
    
def run_ijkgradient_info(f):
    print('isovalue ', isovalue)
    ijkgradient_info_loc = 'E:\\Programs\\Win\\stdAlone\\ijk\\src\\ijkgradientinfo\\Release\\ijkgradientinfo.exe'
    ijkgradient_info = [ijkgradient_info_loc, '-dist2grad', '-min_mag', '0.001', '-intersects_edge', \
                        '-min_scalar', isovalue, '-max_scalar', isovalue]
    ijkgradient_info.append(inputfile.strip())
    ijkgradient_info.append("out.grad.nrrd")
    o = proc.check_output(ijkgradient_info)
    text = os.linesep.join([s for s in o.decode("utf-8").splitlines() if s])
    print(text, file=f )
    
def run_computegrad():
     f=open('./out.txt', 'w+')
     print ('cdist','extend', file=f)
     for i in cdist:
         for j in extend_max:
             computegrad_loc = 'E:\Programs\Win\stdAlone\\religrad_bin\\Release\\religrad.exe'
             computeGrad = [computegrad_loc,  '-extended_curv' , '-angle', '20', '-neighbor_angle', '10']
             computeGrad.append('-cdist')
             computeGrad.append(str(i))
             computeGrad.append('-extend_max')
             computeGrad.append(str(j))
             computeGrad.append(inputfile.strip())
             outname = "out.grad.nrrd"
             computeGrad.append(outname)
             print (i,j, file=f)
             print (computeGrad)
             proc.check_call(computeGrad)
             run_ijkgradient_info(f)
             run_ijkgradient_diff(f)
   
def main(argv):
    readParameters(argv)
    print ('Input file is "', inputfile)
    print ('Isovalue is "', isovalue)
    run_computegrad()
if __name__ == "__main__":
   main(sys.argv[1:])

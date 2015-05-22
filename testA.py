#!/usr/bin/python

'''
MergeSharp tests
'''

##sample runs
## python C:\Users\bhattaca\Documents\GitHub\pythonScripts\testA.py -i A.nrrd --iso 3.1 --gradient A.grad.nrrd
##E:\Data\heinzl\ieeevis2015Tests\crops\toDelete>python C:\Users\bhattaca\Documents\GitHub\pythonScripts\testA.py
## --ifile ..\160uCT.crop1.nhdr --iso 10000 -p test10000  --gradient test10000.grad.nrrd
##E:\Data\heinzl\ieeevis2015Tests\crops\toDelete>python C:\Users\bhattaca\Documents\GitHub\pythonScripts\testA.py
##--ifile ..\160uCT.crop1.nhdr --iso 9000 -p test9000  --gradient test10000.grad.nrrd

import sys
import subprocess as proc
print ("Hello, Python!")


#argument1 = isovalue
#argument2 = dataset

import sys, getopt

def parse_input(argv, inputfile, isovalue, prefix, gradientf):
   try:
      opts, args = getopt.getopt(argv,"hi:p:",["ifile=","iso=", "gradient="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -iso <isovalue> --gradient <gradientfilename>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -iso <isovalue>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ( "--iso"):
         isovalue = arg
      elif opt in ( "--gradient"):
         gradientf = arg
      elif opt == '-p':
          prefix = arg
   return inputfile, isovalue, prefix, gradientf

#Run compute grad
def run_computegrad(inputfile, prefix):
    computegrad_loc = 'E:\Programs\Win\stdAlone\\religrad_bin\\Release\\religrad.exe'
    print("COMPUTE GRAD")
    #computeGrad = [computegrad_loc, '-algo12','2', '-angle', '20', '-neighbor_angle', '20']
    
    computeGrad = [computegrad_loc,  '-extended_curv' , '-extend_max', '2', '-cdist','2', '-angle', '5', '-neighbor_angle', '20']
    
    #computeGrad = [computegrad_loc,  '-extended_curv' , '-cdist','2', '-angle', '20', '-neighbor_angle', '20']
    computeGrad.append(inputfile.strip())
    if(prefix == ""):
        outname = "out.grad.nrrd"
    else:
        outname = prefix + ".grad.nrrd" 
    computeGrad.append(outname)
    print( 'TEST:',' '.join(computeGrad))
    proc.check_call(computeGrad)

#Run mergesharp
def run_mergesharp(inputfile, isovalue, prefix):
    mergesharp_loc =  'E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe'
    mergesharp =  [ mergesharp_loc,'-trimesh','-max_grad_dist', '4',\
                    '-out_isovert','edge','all','-gradS_offset', '0.2', '-position', 'gradBIES', '-map_extended' ] 
    mergesharp.append('-o')
    if(prefix == ""):
        outoff = "out.off"
        mergesharp.append(outoff)
    else:
        outoff = prefix + ".off"
        mergesharp.append(outoff)
    mergesharp.append('-s')
    mergesharp.append('-gradient')
    if(prefix == ""):
        outname = "out.grad.nrrd"
        mergesharp.append(outname)
    else:
        outname = prefix + ".grad.nrrd"
        mergesharp.append(outname)
    mergesharp.append(isovalue)
    mergesharp.append(inputfile)
    print( 'RUN : ', ' '.join(mergesharp))
    #proc.check_call(mergesharp)

#Run mergesharp with pre computed gradient
def run_mergesharp_precompGrad(inputfile, isovalue, prefix, gradientf):
    mergesharp_loc =  'E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe'
    mergesharp =  [ mergesharp_loc,'-trimesh','-max_grad_dist', '4','-out_isovert','sharp','selected', '-gradS_offset', '0.2', '-position', 'gradBIES', '-map_extended' ] 
    mergesharp.append('-o')
    if(prefix == ""):
        outoff = "out.off"
        mergesharp.append(outoff)
    else:
        outoff = prefix + ".off"
        mergesharp.append(outoff)
    mergesharp.append('-s')
    mergesharp.append('-gradient')
    mergesharp.append(gradientf)
    mergesharp.append(isovalue)
    mergesharp.append(inputfile)
    print( ''.join(mergesharp))
    proc.check_call(mergesharp)
    
#Run tests, called from main    
def run_tests (inputfile, isovalue, prefix, gradientf):
    if gradientf == "":
        run_computegrad(inputfile, prefix)
        run_mergesharp(inputfile, isovalue, prefix);
    else:
        run_mergesharp_precompGrad(inputfile, isovalue, prefix, gradientf);

#Main
def main(argv):
    inputfile = ""
    isovalue = ""
    prefix = ""
    gradientf = ""

    inputfile, isovalue, prefix, gradientf  = parse_input(argv, inputfile, isovalue, prefix, gradientf)
    
    print ('Input file is "', inputfile)
    print ('Isovalue is "', isovalue)
    print ('Prefix is "', prefix)
    print ('Gradient is "', gradientf)

    run_tests(inputfile, isovalue, prefix, gradientf)
if __name__ == "__main__":
   main(sys.argv[1:])

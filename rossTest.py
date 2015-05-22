#!/usr/bin/python
import sys
import subprocess as proc

#E:\Data\heinzl\ieeevis2015Tests\crops\toDelete2>python "C:\Users\bhattaca\Documents\GitHub\pythonScr
#ipts\rossTest.py" test5000 test6000 test7000 test8000 test9000 test10000


rossTest = [];



def ross_test(argv, a, b):
    rossTestLoc = 'E:\\Programs\\Win\\stdAlone\\SurfaceAngleDistance-master\\bin\\surfaceAngle\\Release\\surfaceAngle.exe'
    prefix =  't_' + sys.argv[a]+ sys.argv[b]  
    rossTest = [rossTestLoc, '-nh', '-prefix', prefix , '-percent_done','-adjust_coloring_range', '-e', '1','-d','3' ]
    rossTest.append(str(sys.argv[a])+'.off')
    rossTest.append(str(sys.argv[b])+'.off')
    print (rossTest)
    procced =proc.check_call(rossTest)
        
def main(argv):
    print ('Ross test')
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
    
    for  w in range(2,len(sys.argv)):
        print (sys.argv[w])
        ross_test(argv, 1,w)
        
    
    
if __name__ == "__main__":
  main(sys.argv[1:])

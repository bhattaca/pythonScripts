#!/usr/bin/python
'''
Generate datasets.
'''
import subprocess as proc
import os



ijkgenscalar_loc = 'E:\Programs\Win\stdAlone\ijkgenscalarNew_bin\Debug\ijkgenscalar.exe '
ijkgenmesh_loc = 'E:\Programs\Win\stdAlone\ijkgenmesh_bin\Release\ijkgenmesh.exe'

####FLANGE
flangeBase=[ijkgenscalar_loc, '-field', 'annulus', '-flange_wh', '4','3','-grad','-length_diff', '0','-dim',
            '3','-asize','200', '-center', '100 100 100']
flangeBase2=[ijkgenmesh_loc,'-mesh', 'annulus','-flange', '-flange_wh', '4','3','-length_diff', '0',
             '-center', '100 100 100']
flangeDataGenInfo = 'flangeDataGen.txt'
flange_isoVal=['3.1','3.3']

####TwoCube
twoCubeDataGenInfo ='twoCubeDataGen.txt'
twoCubeBase =[ijkgenscalar_loc, '-field','cube', '-n','2','-dim',
            '3','-asize','200', '-center','100 100 100 80 80 80','-grad']
twoCubeBase2=[ijkgenmesh_loc,'-mesh', 'cube','-n', '2',
             '-center','100 100 100 80 80 80']
twoCube_isoVal=['20.1','20.3']

'''
twoCubeBase =[ijkgenscalar_loc, '-field','cube', '-n','2','-dim',
            '3','-asize','100', '-center','50 50 50 40 40 40','-grad']
twoCubeBase2=[ijkgenmesh_loc,'-mesh', 'cube','-n', '2',
             '-center','50 50 50 40 40 40']
twoCube_isoVal=['10.1']
'''
def generateFlange():
    print ('generating Flange')
    testcase = 100
    if not os.path.exists("Flange"):
        os.makedirs("Flange")
    if not os.path.exists("Flange\\mesh"):
        os.makedirs("Flange\\mesh")
    lines = [line.strip() for line in open(flangeDataGenInfo)]
    for line in lines:
        flangeBaseTemp = flangeBase[:]
        whiteSpaceRegex = ",";
        inp = line.split(whiteSpaceRegex)
        flangeBaseTemp.append(inp[:])
        flangeBaseTemp.append( 'Flange\\f'+str(testcase)+ '.nrrd')
        #print (flangeBaseTemp)
        procced = proc.check_call(flangeBaseTemp)
        for ii in flange_isoVal:
            temp2=flangeBase2[:]
            whiteSpaceRegex = ",";
            inp = line.split(whiteSpaceRegex)
            temp2.append(inp[:])
            temp2.append('-distance')
            temp2.append(ii)
            temp2.append('Flange\\mesh\\f'+str(testcase)+"_"+str(ii)+'.off')
            #run the ijkgenmesh test
            procced = proc.check_call(temp2)
        testcase = testcase+5
        
def generateTwoCube():
    print ('generating TwoCube')
    
    testcase = 100
    if not os.path.exists("TwoCube"):
        os.makedirs("TwoCube")
    if not os.path.exists("TwoCube\\mesh"):
        os.makedirs("TwoCube\\mesh")
    lines = [line.strip() for line in open(twoCubeDataGenInfo)]
    #print (lines)
    
    for line in lines:
        twoCubeBaseTemp = twoCubeBase[:]
        whiteSpaceRegex = ",";
        inp = line.split(whiteSpaceRegex)
        twoCubeBaseTemp.append(inp[:])
        twoCubeBaseTemp.append( 'twoCube\\t'+str(testcase)+ '.nrrd')
        print (twoCubeBaseTemp)
        procced = proc.check_call(twoCubeBaseTemp)
        for ii in twoCube_isoVal:
            temp2=twoCubeBase2[:]
            #whiteSpaceRegex = ",";
            #inp = line.split(whiteSpaceRegex)
            temp2.append(inp[:])
            temp2.append('-distance')
            temp2.append(ii)
            temp2.append('twoCube\\mesh\\t'+str(testcase)+"_"+str(ii)+'.off')
            #run the ijkgenmesh test
            print ('genmesh command ', temp2)
            procced = proc.check_call(temp2)
        testcase = testcase+5
def main():
    print ('generate datasets')
    #generateFlange()
    generateTwoCube()

if __name__ == "__main__":
    main()    

#!/usr/bin/python
'''
Merge Test , Reliable gradienents test.
'''
import subprocess as proc
import sys as sys
import os

#configurations

#setup isovalues
#isoval_opts =['10.1', '3.1']
isoval_opts =['4']

#set up location of file locations
fread = open ('./file-names.txt','r') # contains the names of the files on which the test is run
surface_results = open ('./surface-results.txt','w') # stores the edge count values
ftestdetails = open ('./test-details.txt','w') # stores deatails of the test runs



############
## mergeSharp  runs 
## set up the test you want to run.
## write the test as 'mergesharp' and then append it to the mergesharpTests, as shown below
############
mergesharpTests=[]
computeGradTests=[]
surfaceAngleDistTest = []

######################################################################
#TESTS
######################################################################

mergesharp = ['C:\\Users\\Ross\\Documents\\binGithub\\mergesharp\\Release\\mergesharp.exe', '-trimesh', '-position', 'GRAD_PLACE_HOLDER' ]
mergesharpTests.append(mergesharp)

######################################################################
#COMPUTE GRAD TESTS
######################################################################

computeGrad = ['C:\\Users\\Ross\\Documents\\binGithub\\religrad\\Release\\religrad.exe',  '-angle_test',  '-scalar_test']
computeGradTests.append(computeGrad)


######################################################################
#SURFACE ANGLE DISTANCE TESTS
######################################################################

surfaceAngleDist = ['C:\\Users\\Ross\\Documents\\Visual Studio 2013\\Projects\\SurfaceAngleDistance\\Release\\SurfaceAngleDistance.exe', 'fileplaceholder1', 'fileplaceholder2', '-nh', '-ah', '-ca', '7.5', '-d', '4', '-e', '1', '-w', '.5']
surfaceAngleDistTest.append(surfaceAngleDist);
'''
#test1
mergesharp = ['./mergesharp', '-no_merge_sharp','-position','gradEC','-trimesh' ,'-dist2centroid','-allow_conflict',\
            '-multi_isov','-max_dist','5','-clamp_far','-sharp_edgeI','-lindstrom_fast']
mergesharpTests.append(mergesharp)
#test2
mergesharp = ['./mergesharp', '-no_merge_sharp','-position','gradEC','-trimesh' ,'-dist2centroid','-allow_conflict',\
            '-multi_isov','-max_dist','0','-clamp_far','-sharp_edgeI','-lindstrom_fast']
mergesharpTests.append(mergesharp)
#test3 
mergesharp = ['./mergesharp', '-no_merge_sharp','-position','gradEC','-trimesh' ,'-dist2centroid','-clamp_conflict',\
            '-multi_isov','-sharp_edgeI','-lindstrom_fast']
mergesharpTests.append(mergesharp)
#test4
mergesharp = ['./isodual3D', '-merge_sharp','-position','gradEC','-trimesh' ,'-dist2centroid','-allow_conflict',\
            '-multi_isov','-sharp_edgeI','-lindstrom_fast']
mergesharpTests.append(mergesharp)
'''


#######################################################################
                        
findsharp_windows = ['E:\\Programs\Win\\stdAlone\\findsharp_bin\\Debug\\findsharp.exe','140']
countdegree_windows =['E:\\Programs\\Win\\stdAlone\\findEdgeCount_bin\\Debug\\findEdgeCount.exe', '-fp']

def test__surfaces(n, m, angle_test, merge_test, st):
    print ("status: in function TEST")
    fread = open ('./file-names.txt','r') # contains the names of the files on which the test is run
    for f in fread:
        fname_with_nrrd = f.split("/")[len(f.split("/"))-1]
        fname = fname_with_nrrd.split(".")[0]
        f_original_grad = fname + ".grad.nrrd"
        #gradients
        temp_g = angle_test[:]
        temp_g.append(f.strip())
        
        #Running test 1 with angle test
        f_angle_test_grad_name = fname+".angle_test.grad.nrrd"
        temp_g.append(f_angle_test_grad_name)
        #print(temp_g)
        procced = proc.check_call(temp_g)
        for s in isoval_opts:
        
            ###Generating original surface to compare
            mt_temp = merge_test[:]
            test_details = str(n)+","+str(m)+","+fname+"\n"# test details
            mt_temp.append('-o')
            outFileName = fname + "." + s + ".original.out.off"
            mt_temp.append(outFileName)
            mt_temp.append('-s')
            #add the gradient file name extracted from the file name.
            mt_temp.append('-gradient')
            mt_temp.append(f_original_grad)
            mt_temp.append(s)
            mt_temp.append(f.strip())
            mt_temp[3] = "gradNIES"
            ftestdetails.write(test_details)
            procced = proc.check_call(mt_temp)
            
            ##Generating surface with angle difference tests
            mt_temp = merge_test[:]
            mt_temp.append('-o')
            outAngleDiffFileName = fname + "." + s + ".angle_diff.out.off"
            mt_temp.append(outAngleDiffFileName)
            mt_temp.append('-s')
            #add the gradient file name extracted from the file name.
            mt_temp.append('-gradient')
            mt_temp.append(f_angle_test_grad_name)
            mt_temp.append(s)
            mt_temp.append(f.strip())
            mt_temp[3] = "gradBIES"
            procced = proc.check_call(mt_temp)
            
            ##Comparing surfaces
            
            ##Original with angle test
            surface_test = st[:]
            surface_test[1] = outFileName
            surface_test[2] = outAngleDiffFileName
            surface_test.append(outFileName)
            surface_test.append(outAngleDiffFileName)
            surface_test.append('-prefix')
            surface_test.append(fname + '.' + s + '.angle_diff.')
            procced = proc.check_call(surface_test, stdout=surface_results)
            

def main():
    print ("status: start test1")
    n=1
    m=1
    for g in range (0, len(computeGradTests)):
        m=1
        for mt in mergesharpTests:
            for st in surfaceAngleDistTest:
                # print iso
                angle_test = computeGradTests[g]
                
                print ("\nstatus: in function MAIN\n ", mt, angle_test)
                #print >>ftestdetails, iso 
                test__surfaces(n, m, angle_test, mt, st) 
                m=m+1
        n=n+1;
if __name__ == "__main__":
    main()
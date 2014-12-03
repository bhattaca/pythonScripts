#!/usr/bin/python
'''
Merge Test , Reliable gradienents test.

'''
import subprocess as proc
import sys as sys
import os

#configurations

#setup isovalues
isoval_opts =['4.1']

#set up location of file locations
fread = open ('./file-names.txt','r') # contains the names of the files on which the test is run
fedgecount = open ('./edge-count.txt','w') # stores the edge count values
ftestdetails = open ('./test-details.txt','w') # stores deatails of the test runs



############
## mergeSharp  runs 
## set up the test you want to run.
## write the test as 'mergesharp' and then append it to the mergesharpTests, as shown below
############
mergesharpTests=[]
computeGradTests=[]

######################################################################
#	TESTS
######################################################################


mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '4',
              '-gradS_offset', '1', '-max_dist', '1.0', '-position', 'gradBIES', '-map_extended' ]
mergesharpTests.append(mergesharp)
######################################################################
#COMPUTE GRAD TESTS
######################################################################

computeGrad = ['E:\Programs\Win\stdAlone\\religrad_bin\\Release\\religrad.exe',  '-angle_test',  '-scalar_test']
computeGradTests.append(computeGrad)

#computeGrad = ['E:\Programs\Win\stdAlone\\religrad_bin\\Release\\religrad.exe',  '-curvature_based']
#computeGradTests.append(computeGrad)

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
countdegree_windows =['E:\\Programs\Win\\stdAlone\\count_degree_bin\\Debug\\countdegree.exe', '-fshort','-e']

'''
for each file run mergesharp with correct gradients
'''
def test_correct_grad(n,iso):
    print ("status: in function TEST")
    fread = open ('./file-names.txt','r') # contains the names of the files on which the test is run
    for f in fread:
        fname_with_nrrd = f.split("/")[len(f.split("/"))-1]
        fname = fname_with_nrrd.split(".")[0]
        print ("\n**********************************\n filename ", fname)
        fgradnoisename = fname+".grad.nrrd"
        for i in isoval_opts:
                #iso_temp = isodual3D[:]
                iso_temp = iso[:]        
                test_details = str(n)+","+fname+","+str(i)+"\n"
                print("isovalue ", i)
                #fname_line_name = loc+"output_offs/"+fname+"-iso-"+str(i)+".line"
                iso_temp.append('-o')
                iso_temp.append("out_ms"+str(n)+".off")
                iso_temp.append('-s')
                #add the gradient file name extracted from the file name.
                iso_temp.append('-gradient')
                iso_temp.append(fgradnoisename)
                iso_temp.append(i)
                iso_temp.append(f.strip())
                #print "test call:", iso_temp[:]
                #print >>ftestdetails, test_details, iso, "correct"
                ftestdetails.write(test_details)
                procced = proc.check_call(iso_temp)
                
                if procced==0:
                    if procced == 0:
                        findsharpTemp = findsharp_windows[:]
                        findsharpTemp.append("out_ms"+str(n)+".off")
                        #print "findsharp: ", findsharpTemp[:]
                        procced = proc.check_call(findsharpTemp)
                        if procced ==0:
                            countdegreeTemp = countdegree_windows[:]
                            countdegreeTemp.append("out_ms"+str(n)+".line")
                            #print "countdegree: ", countdegreeTemp[:]
                            procced=proc.check_call(countdegreeTemp,stdout=fedgecount)
                        else:
                            print ('error in degree count')
                            sys.exit()
                    else:
                        print ('error in meshconvert')
                        sys.exit()
                                
                else:
                    print ("error")
                    sys.exit();
		
'''
for each file run mergesharp with cdiff gradients
'''

def test__grad(n, m, g, mt):
    print ("status: in function TEST")
    fread = open ('./file-names.txt','r') # contains the names of the files on which the test is run
    for f in fread:
        fname_with_nrrd = f.split("/")[len(f.split("/"))-1]
        fname = fname_with_nrrd.split(".")[0]
        #gradients
        temp_g = g[:]
        temp_g.append(f.strip())
        fgrad_name = fname+".test.grad.nrrd"
        temp_g.append(fgrad_name)
        #print(temp_g)
        procced = proc.check_call(temp_g)
        
        for s in isoval_opts:
            mt_temp = mt[:]
            test_details = "cg "+str(n)+",ms "+str(m)+","+fname+","+str(s)+"\n"# test details
            mt_temp.append('-o')
            mt_temp.append("out_cg"+str(n)+"ms"+str(m)+".off")
            mt_temp.append('-s')
            #add the gradient file name extracted from the file name.
            mt_temp.append('-gradient')
            mt_temp.append(fgrad_name)
            mt_temp.append(s)
            mt_temp.append(f.strip())
            #mt_temp.append(' > '+ ' garb ')
            print (mt_temp)
            ftestdetails.write(test_details)
            procced = proc.check_call(mt_temp)
            
            findsharpTemp = findsharp_windows[:]
            findsharpTemp.append("out_cg"+str(n)+"ms"+str(m)+".off")
            #print "findsharp: ", findsharpTemp[:]
            procced = proc.check_call(findsharpTemp)
            
            countdegreeTemp = countdegree_windows[:]
            countdegreeTemp.append("out_cg"+str(n)+"ms"+str(m)+".line")
            #print "countdegree: ", countdegreeTemp[:]
            procced=proc.check_call(countdegreeTemp,stdout=fedgecount)


def main():
    print ("status: start test1")
    n=1
    m=1
	
    for mt in mergesharpTests:
        test_correct_grad(m,mt)
        m=m+1
        
    for g in computeGradTests:
        #ms
        m=1
        for mt in mergesharpTests:
           # print iso
            print ("\nstatus: in function MAIN\n ", mt, g)
            #print >>ftestdetails, iso
            #test__grad(n, m, g, mt) 
            m=m+1
        n=n+1;
if __name__ == "__main__":
    main()            
            
            
            
    

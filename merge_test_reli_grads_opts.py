#!/usr/bin/python
'''
Latest as of 5/7/2015
Merge Test , Reliable gradienents test.
Modified to take arbitary input parameters
test_correct_grad has been updated for perfect gradient so that all results are accumulated in test_details

'''
import subprocess as proc
import sys as sys
import os
import glob

#user input.
surface_distance_loc = 'E:\\Programs\\Win\\stdAlone\\SurfaceAngleDistance-master\\bin\\SurfaceAngleDistance_ari\\Release\\SurfaceAngleDistance_ari.exe'
mergesharp_loc =  'E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe'
computegrad_loc = 'E:\Programs\Win\stdAlone\\religrad_bin\\Release\\religrad.exe'
findsharp_windows = ['E:\\Programs\Win\\stdAlone\\findsharp_bin\\Debug\\findsharp.exe','140']
countdegree_windows =['E:\\Programs\Win\\stdAlone\\count_degree_bin\\Debug\\countdegree.exe', '-fshort']
ijkgradientinfo_location = ['E:\\Programs\\Win\\stdAlone\\ijkgradientinfo_bin\\Release\\ijkgradientinfo.exe']
ijkgradientdiffangle_loc = ['E:\\Programs\\Win\\stdAlone\\ijkgradientdiff_bin\\Release\\ijkgradientdiff.exe']

#setup isovalues
isoval_opts =[]

#set up location of file locations
fread = open ('./file-names.txt','r') # contains the names of the files on which the test is run
fedgecount = open ('./edge-count.txt','w') # stores the edge count values
ftestdetails = open ('./test-details.txt','w') # stores deatails of the test runs
fijkgradientdiff_info = open ('./ijkgradinfo.txt','w') # stores deatails of the test runs



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

    
mergesharp = [ mergesharp_loc,'-trimesh','-max_grad_dist', '4',
              '-gradS_offset', '0.2', '-position', 'gradBIES', '-map_extended' ]
mergesharpTests.append(mergesharp)

######################################################################
#COMPUTE GRAD TESTS
######################################################################

#computeGrad = [computegrad_loc,  '-angle_test',  '-scalar_test']
#computeGradTests.append(computeGrad)

computeGrad = [computegrad_loc,  '-extended_curv' , '-extend_max', '2', '-cdist','2', '-angle', '20', '-neighbor_angle', '20']
computeGradTests.append(computeGrad)


#######################################################################
                        
'''
find in file,
reads a file for a particular string
and returns the line with the string
'''
def findInFile(fname, x):
    with open(fname, 'r') as f:
        for line in f:
           if x in line:
               break
    return line

def searchFor(f, x):
    f=f.split('\n')
    for line in f:
        if x in line:
            break
    return line

'''
Run Ijkgenmesh
'''
def run_ijkgenmesh(fname):
    print('In ijkgenmesh ', fname)
    centerLine = findInFile(fname+'.nrrd', 'center')
    print (centerLine)
    '''
    with open(fname+'.nrrd', 'r') as f:
        for line in f:
           if 'center' in line:
               break
    print ('found ', line)
    '''
    
'''
for each file run mergesharp with correct gradients
'''
def test_correct_grad(n,iso):
    print ("status: in function test correct gradients... ")
    fread = open ('./file-names.txt','r') # contains the names of the files on which the test is run
    #
    #delete all off files.
    #
    files = glob.glob('*.off')
    for f in files:
        os.remove(f)
    files = glob.glob('*.line')
    for f in files:
        os.remove(f)

    for f in fread:
        fname_with_nrrd = f.split("/")[len(f.split("/"))-1]
        fname = fname_with_nrrd.split(".")[0]
        print ("\n**********************************\nfilename ", fname)
        fgradnoisename = fname+".grad.nrrd"
        for i in isoval_opts:
                #iso_temp = isodual3D[:]
                iso_temp = iso[:]        
                test_details = str(n)+","+fname+","+str(i)+"\n"
                print("isovalue ", i)
                #fname_line_name = loc+"output_offs/"+fname+"-iso-"+str(i)+".line"
                iso_temp.append('-o')
                iso_temp.append("out_ms"+str(i)+".off")
                iso_temp.append('-s')
                #add the gradient file name extracted from the file name.
                iso_temp.append('-gradient')
                iso_temp.append(fgradnoisename)
                iso_temp.append(i)
                iso_temp.append(f.strip())
                print ("test call:", iso_temp[2:])
                #print >>ftestdetails, test_details, iso, "correct"
                ftestdetails.write((test_details.rstrip()+","))
                procced = proc.check_call(iso_temp)

                temp3=[surface_distance_loc]
                temp3.append('-e')
                temp3.append('1')
                temp3.append('-d')
                temp3.append('2')
                temp3.append('-w')
                temp3.append('3')
                temp3.append('-sr')
                temp3.append('4')
                temp3.append("out_ms"+str(i)+".off")
                temp3.append("mesh\\"+fname+"_"+i+".off")
                #proceed = proc.check_call(temp3)
                temp3Result = (proc.check_output(temp3)).decode("utf-8")
                #print(temp3Result)
                angle1to2 = (searchFor(temp3Result, "Max of min angle from surface 1 to surface 2")).rstrip()
                angle2to1 = (searchFor(temp3Result, "Max of min angle from surface 2 to surface 1")).rstrip()
                
                
                angle2to1=angle2to1.split(':')[1]
                angle1to2=angle1to2.split(':')[1]
                ftestdetails.write(angle1to2+","+angle2to1+",")

                dist1to2 = (searchFor(temp3Result, "Max of min distance from surface 1 to surface 2")).rstrip()
                dist2to1 = (searchFor(temp3Result, "Max of min distance from surface 2 to surface 1")).rstrip()
                dist2to1=dist2to1.split(':')[1]
                dist1to2=dist1to2.split(':')[1]
                ftestdetails.write(dist1to2+","+dist2to1+",")
                
                print ('angle2to1 ', angle2to1)
                if procced==0:
                    if procced == 0:
                        findsharpTemp = findsharp_windows[:]
                        findsharpTemp.append("out_ms"+str(i)+".off")
                        #print "findsharp: ", findsharpTemp[:]
                        procced = proc.check_call(findsharpTemp)
                        if procced ==0:
                            countdegreeTemp = countdegree_windows[:]
                            countdegreeTemp.append("out_ms"+str(i)+".line")
                            ftestdetails.write((proc.check_output(countdegreeTemp)).decode("utf-8").rstrip()+"\n")
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
    #delete all off files before starting
    files = glob.glob('*.off')
    for f in files:
        os.remove(f)
    for f in fread:
        fname_with_nrrd = f.split("/")[len(f.split("/"))-1]
        fname = fname_with_nrrd.split(".")[0]
        #gradients
        temp_g = g[:]
        temp_g.append(f.strip())
        #fgrad_name = fname+".test.grad.nrrd"
        fgrad_name = fname+".test."+ str(n) +".grad.nrrd"
        temp_g.append(fgrad_name)
        print("tempg ", temp_g)
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
            
            procced = proc.check_call(countdegreeTemp,stdout=fedgecount)
            

            
def test_ijkgradient_info(n,g):
    print('************************ in test ijk gradient info ************************** ')
    fread = open ('./file-names.txt','r') # contains the names of the files on which the test is run
    for f in fread:
        fname_with_nrrd = f.split("/")[len(f.split("/"))-1]
        fname = fname_with_nrrd.split(".")[0]
        #gradients
        temp_g = g[:]
        temp_g.append(f.strip())
        #fgrad_name = fname+".test.grad.nrrd"
        fgrad_name = fname+".test."+ str(n) +".grad.nrrd"
        temp_g.append(fgrad_name)
        print("tempg ", temp_g)
        procced = proc.check_call(temp_g)
        ijkgradientdiffangle_temp = ijkgradientdiffangle_loc[:]
        ijkgradientdiffangle_temp.append("-minmag")
        ijkgradientdiffangle_temp.append("0.001")
        ijkgradientdiffangle_temp.append("-angle")
        ijkgradientdiffangle_temp.append("10")
        ijkgradientdiffangle_temp.append("-ignore_small_mag")
        ijkgradientdiffangle_temp.append("either")
        ijkgradientdiffangle_temp.append("-total")
        foriggradname = fname+".grad.nrrd"
        ijkgradientdiffangle_temp.append(foriggradname)
        ijkgradientdiffangle_temp.append(fgrad_name)
        procced=proc.check_call( ijkgradientdiffangle_temp,stdout=fijkgradientdiff_info)
        for s in isoval_opts:
            ijkgradientinfo_test = ijkgradientinfo_location[:]
            ijkgradientinfo_test.append("-dist2grad")
            ijkgradientinfo_test.append("-min_mag")
            ijkgradientinfo_test.append("0.0001")
            ijkgradientinfo_test.append("-intersects_edge")
            ijkgradientinfo_test.append("-min_scalar")
            ijkgradientinfo_test.append(s)
            ijkgradientinfo_test.append("-max_scalar")
            ijkgradientinfo_test.append(s)
            ijkgradientinfo_test.append(f.strip())
            ijkgradientinfo_test.append(fgrad_name)
            print("ijkgradientdiff ", ijkgradientinfo_test)
            procced=proc.check_call(ijkgradientinfo_test,stdout=fijkgradientdiff_info)
            
            
            

def main():
    print ("status: start test1")
    ftestdetails.write("testNo,DataSet,isoval, maxOfMinAngle1to2, maxOfMinAngle2to1,maxOfMinDist1to2,maxOfMinDist2to1, EdgeCntErr\n")
    files = glob.glob('*.off')
    for f in files:
        os.remove(f)
    files = glob.glob('*.line')
    for f in files:
        os.remove(f)
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
    for i in range(1,len(sys.argv)):
        #print ('isovalue ', str(sys.argv[i]))
        isoval_opts.append(str(sys.argv[i]))
    
    n=1
    m=1
    #perfect gradient	
    for mt in mergesharpTests:
        test_correct_grad(m,mt)
        m=m+1
    '''
    #computed gradients    
    for g in computeGradTests:
        #ms
        m=1
        
        for mt in mergesharpTests:
           # print iso
            print ("\nstatus: in function MAIN\n ", mt, g)
            test__grad(n, m, g, mt) 
            m=m+1
        #test_ijkgradient_info(n,g)
        
        n=n+1;
    '''        
if __name__ == "__main__":
    main()
    files = glob.glob('*.off')
    for f in files:
        os.remove(f)
    files = glob.glob('*.line')
    for f in files:
        os.remove(f)
    fread.close()
    fedgecount.close()
    ftestdetails.close()
    fijkgradientdiff_info.close();
            
            
            
    

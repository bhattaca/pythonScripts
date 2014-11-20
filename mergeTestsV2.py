#!/usr/bin/python
'''
Merge Test 
'''
import subprocess as proc
import sys as sys
import os

#configurations

#setup isovalues
isoval_opts =['3.5','3.8','3.9','4.0','4.2']

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

######################################################################
#Change max_grad_dist
#test1
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '4',
              '-gradS_offset', '1', '-max_dist', '2', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test2 
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '3',
              '-gradS_offset', '1', '-max_dist', '2', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)

#test3
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '2',
              '-gradS_offset', '1', '-max_dist', '2', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test4
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '1',
              '-gradS_offset', '1', '-max_dist', '2', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)

#change max_dist
#test1
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '4',
              '-gradS_offset', '1', '-max_dist', '1', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test2 
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '3',
              '-gradS_offset', '1', '-max_dist', '1', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test3
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '2',
              '-gradS_offset', '1', '-max_dist', '1', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test4
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '1',
              '-gradS_offset', '1', '-max_dist', '1', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)

#change grad_S_offset
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '4',
              '-gradS_offset', '0.5', '-max_dist', '2', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test2 
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '3',
              '-gradS_offset', '0.5', '-max_dist', '2', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test3
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '2',
              '-gradS_offset', '0.5', '-max_dist', '2', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test4
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '1',
              '-gradS_offset', '0.5', '-max_dist', '2', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#############################################################################################
#with map_extended turned on
#Change max_grad_dist
#test1
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '4',
              '-gradS_offset', '1', '-max_dist', '2','-map_extended', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test2 
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '3',
              '-gradS_offset', '1', '-max_dist', '2','-map_extended', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test3
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '2',
              '-gradS_offset', '1', '-max_dist', '2','-map_extended', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test4
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '1',
              '-gradS_offset', '1', '-max_dist', '2','-map_extended', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)

#change max_dist
#test1
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '4',
              '-gradS_offset', '1', '-max_dist', '1','-map_extended', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test2 
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '3',
              '-gradS_offset', '1', '-max_dist', '1','-map_extended', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test3
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '2',
              '-gradS_offset', '1', '-max_dist', '1','-map_extended','-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test4
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '1',
              '-gradS_offset', '1', '-max_dist', '1','-map_extended', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)

#change grad_S_offset
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '4',
              '-gradS_offset', '0.5', '-max_dist', '2','-map_extended', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test2 
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '3',
              '-gradS_offset', '0.5', '-max_dist', '2','-map_extended', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test3
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '2',
              '-gradS_offset', '0.5', '-max_dist', '2','-map_extended', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)
#test4
mergesharp = ['E:\Programs\Win\stdAlone\mergesharp_bin\Release\mergesharp.exe','-trimesh', '-max_grad_dist', '1',
              '-gradS_offset', '0.5', '-max_dist', '2','-map_extended', '-position', 'gradBIES' ]
mergesharpTests.append(mergesharp)

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

'''
for each file run mergesharp with correct gradients
'''
def test_correct_grad(n,iso):
    print "status: in function TEST"
    fread = open ('./file-names.txt','r') # contains the names of the files on which the test is run
    for f in fread:
        fname_with_nrrd = f.split("/")[len(f.split("/"))-1]
        fname = fname_with_nrrd.split(".")[0]
        fgradnoisename = fname+".grad.nrrd"
        for i in isoval_opts:
                #iso_temp = isodual3D[:]
                iso_temp = iso[:]        
                test_details = str(n)+","+fname+","+str(i)
                n = n+1
                #fname_line_name = loc+"output_offs/"+fname+"-iso-"+str(i)+".line"
                iso_temp.append('-o')
                iso_temp.append('out.off')
                iso_temp.append('-s')
                #add the gradient file name extracted from the file name.
                iso_temp.append('-gradient')
                iso_temp.append(fgradnoisename)
                iso_temp.append(i)
                iso_temp.append(f.strip())
                #print "test call:", iso_temp[:]
                print >>ftestdetails,test_details,iso, "correct"
		
		procced = proc.check_call(iso_temp)
                
                if procced==0:
                    if procced == 0:
                        findsharpTemp = findsharp_windows[:]
                        findsharpTemp.append("out.off")
                        #print "findsharp: ", findsharpTemp[:]
                        procced = proc.check_call(findsharpTemp)
                        if procced ==0:
                            countdegreeTemp = countdegree_windows[:]
                            countdegreeTemp.append("out.line")
                            #print "countdegree: ", countdegreeTemp[:]
                            procced=proc.check_call(countdegreeTemp,stdout=fedgecount)
                        else:
                            print 'error in degree count'
                            sys.exit()
                    else:
                        print 'error in meshconvert'
                        sys.exit()
                                
                else:
                    print "error"
                    sys.exit();
		
'''
for each file run mergesharp with cdiff gradients
'''                
def test_cdiff_grad(n,iso):
    print "status: in function TEST"
    fread = open ('./file-names.txt','r') # contains the names of the files on which the test is run
    for f in fread:
        fname_with_nrrd = f.split("/")[len(f.split("/"))-1]
        fname = fname_with_nrrd.split(".")[0]
        fgradnoisename = fname+".cdiff.grad.nrrd"
        for i in isoval_opts:
                #iso_temp = isodual3D[:]
                iso_temp = iso[:]        
                test_details = str(n)+","+fname+","+str(i)
                n = n+1
                #fname_line_name = loc+"output_offs/"+fname+"-iso-"+str(i)+".line"
                iso_temp.append('-o')
                iso_temp.append('out.off')
                iso_temp.append('-s')
                #add the gradient file name extracted from the file name.
                iso_temp.append('-gradient')
                iso_temp.append(fgradnoisename)
                iso_temp.append(i)
                iso_temp.append(f.strip())
                #print "test call:", iso_temp[:]
                print >>ftestdetails,test_details,iso, "cdiff"
		
		procced = proc.check_call(iso_temp)
                
                if procced==0:
                    if procced == 0:
                        findsharpTemp = findsharp_windows[:]
                        findsharpTemp.append("out.off")
                        #print "findsharp: ", findsharpTemp[:]
                        procced = proc.check_call(findsharpTemp)
                        if procced ==0:
                            countdegreeTemp = countdegree_windows[:]
                            countdegreeTemp.append("out.line")
                            #print "countdegree: ", countdegreeTemp[:]
                            procced=proc.check_call(countdegreeTemp,stdout=fedgecount)
                        else:
                            print 'error in degree count'
                            sys.exit()
                    else:
                        print 'error in meshconvert'
                        sys.exit()
                                
                else:
                    print "error"
                    sys.exit();


'''
for each file run mergesharp with reliable_grads
'''
def test_reli_grad(n,iso):
    print "status: in function TEST"
    fread = open ('./file-names.txt','r') # contains the names of the files on which the test is run
    for f in fread:
        fname_with_nrrd = f.split("/")[len(f.split("/"))-1]
        fname = fname_with_nrrd.split(".")[0]
        fgradnoisename = fname+".reli.grad.nrrd"
        for i in isoval_opts:
                #iso_temp = isodual3D[:]
                iso_temp = iso[:]        
                test_details = str(n)+","+fname+","+str(i)
                n = n+1
                #fname_line_name = loc+"output_offs/"+fname+"-iso-"+str(i)+".line"
                iso_temp.append('-o')
                iso_temp.append('out.off')
                iso_temp.append('-s')
                #add the gradient file name extracted from the file name.
                iso_temp.append('-gradient')
                iso_temp.append(fgradnoisename)
                iso_temp.append(i)
                iso_temp.append(f.strip())
                #print "test call:", iso_temp[:]
                print >>ftestdetails,test_details,iso,"reli"
		
		procced = proc.check_call(iso_temp)
                
                if procced==0:
                    if procced == 0:
                        findsharpTemp = findsharp_windows[:]
                        findsharpTemp.append("out.off")
                        #print "findsharp: ", findsharpTemp[:]
                        procced = proc.check_call(findsharpTemp)
                        if procced ==0:
                            countdegreeTemp = countdegree_windows[:]
                            countdegreeTemp.append("out.line")
                            #print "countdegree: ", countdegreeTemp[:]
                            procced=proc.check_call(countdegreeTemp,stdout=fedgecount)
                        else:
                            print 'error in degree count'
                            sys.exit()
                    else:
                        print 'error in meshconvert'
                        sys.exit()
                                
                else:
                    print "error"
                    sys.exit();
def main():
    print "status: start test1"
    n=1
    for iso in mergesharpTests:
       # print iso
       print "status: in function MAIN\n ", iso
       #print >>ftestdetails, iso  
       test_correct_grad (n,iso)
       test_cdiff_grad (n,iso)
       test_reli_grad (n,iso)
if __name__ == "__main__":
    main()            
            
            
            
    

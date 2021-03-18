run = [1,124]
directory = '../data//20210317/'
#output_file = directory+'output_Cs137s_lysoDUT_lysoTAG_run'+str(run[0]) + '_' + str(run[1]) + '.root'
output_file = directory+'output_Co57Calib_DUT_run'+str(run[0]) + '_' + str(run[1]) + '.root'
cmd = 'hadd ' + output_file + ' '
for i in range(run[0],run[1]+1):
    cmd = cmd+ ' ' + directory + 'output_run'+str(i)+'.root'
print(cmd)


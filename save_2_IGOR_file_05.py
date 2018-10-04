import numpy as np
import scipy as sp
import math as ma

def save_single_data(folderPath,DataWave,waveName,run,start_at,end_at) :
    waveName = waveName.replace('=','_')
    delta = (end_at - start_at)/len(DataWave)
    with open(folderPath + 'data_output_2_igor_run%04d' % run + '.itx', 'w') as out_file : 
        for i in range(len(DataWave)+1):
            out_string = ''
            if i == 0:
                out_string = 'IGOR\nWAVES/D/O/N=('+str(len(DataWave))+') '+ waveName +'\nBEGIN\n'
                out_string += str(DataWave[i])
                out_string += '\n'
            elif i < len(DataWave):
                out_string += str(DataWave[i])
                out_string += '\n'
            else:
                out_string = 'END\n\nX SetScale/P y 0,1, \"Counts [a.u.]\", ' + waveName + '\nX SetScale/P x {0:g},{1:g}, \"Kinetic Energy [eV]\",  '.format(start_at, delta)  + waveName + '\nX Display ' + waveName + '\nX Legend/C/N=text0/F=0/B=1/A=LT\nX ModifyGraph nticks=10,minor=1\n'
                
            out_file.write(out_string)
            
def save_2to1_data(folderPath,DataWave,DataXWave,waveName,run,runType) :
    if waveName.find('Sum_') != -1 :
        SaveName = 'data2igor_from_' + runType + '_Sum_%04d'
        waveName = waveName[ :4] + runType + '_' + waveName[4:]
        waveName = waveName.replace('=','_')
    else :
        SaveName = 'data2igor_from_' + runType + '_%04d'
        waveName = runType + '_' + waveName
        waveName = waveName.replace('=','_')
        
    with open(folderPath + SaveName % run + '.itx', 'w') as out_file :
        for i in range(len(DataWave)+1):
            out_string = ''
            if i == 0:
                out_string = 'IGOR\nWAVES/D/O/N=('+str(len(DataWave))+') '+ waveName +', Energy_wave_2_' + runType + '_%04d' % run +'\nBEGIN\n'
                out_string += str(DataWave[i]) + '\t' + str(DataXWave[i])
                out_string += '\n'
            elif i < len(DataWave):
                out_string += str(DataWave[i]) + '\t' + str(DataXWave[i])
                out_string += '\n'
            else:
                out_string = 'END\n\nX SetScale d 0,0, \"Counts [a.u.]\", ' + waveName + '\nX SetScale d 0,0, \"Kinetic Energy [eV]\", Energy_wave_2_' + runType + '_%04d' % run + '\nX Display ' + waveName + ' vs Energy_wave_2_' + runType + '_%04d' % run + '\nX Legend/C/N=text0/F=0/B=1/A=LT\nX ModifyGraph nticks=10,minor=1\n'
                
            out_file.write(out_string)

def save_2D_data(folderPath,DataWave,waveName,start_at,delta,run,runType) :
    waveName = waveName.replace('=','_')
    with open(folderPath + 'output_2D_Igor_' + runType + '_data_run%04d' % run + '.itx', 'w') as out_file :
        for i in range(len(DataWave)+1):
            out_string = ''
            if i == 0:
                out_string = 'IGOR\nWAVES/D/O/N=('+str(len(DataWave))+','+str(len(DataWave[0]))+') Intensity_2D_' + runType + '_%04d' % run + '\nBEGIN\n'
                for j in range(len(DataWave[0])):
                    out_string += ' ' + str(DataWave[i][j]) + '\t'
                
                out_string += '\n'
            elif i < len(DataWave):
                for j in range(len(DataWave[0])):
                    out_string += ' ' + str(DataWave[i][j]) + '\t'
            else:
                out_string = 'END\n\nX SetScale/P y 0,1 \"Region Iteration [a.u.]\", Intensity_2D_' + runType + '%04d' % run + '\nX SetScale/P x {0:g},{1:g}, \"Kinetic Energy [eV]\",  '.format(start_at, delta) + 'Intensity_2D_' + runType + '_%04d' % run + '\nX NewImage/K=0 Intensity_2D_' + runType + '_%04d' % run + '\nX ModifyGraph nticks=10,minor=1\nX ModifyGraph Intensity_2D_' + runType + '_%04d ctab= {*,*,Rainbow,1}\n' % run
             
            out_file.write(out_string)             

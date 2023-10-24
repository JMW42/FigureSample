# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 10:28:35 2023

@author: jwill
"""

#import module
import xmltodict, re
import pandas as pd
import numpy as np

filepath = 'materials data base/materials.xml'


# METHODS:
    
def extract_material(material_dict, tag):
    
    material_name = material_dict["@description"]
    print(f'{tag} --> {material_name}')
    
    material_data = {'Material Name': material_name}
    
    df_properties = pd.DataFrame({'property':[], 'property value':[], 'property unit':[]})
    
    
    # read all properties:
    for key in material_dict:
        prop = material_dict[key]
        
        if key == '@description': continue
        
        desc = prop["@description"]
        value = prop["@value"]
        unit = ''
        
        unit_search = re.search('\[(.*?)\]', desc)
        if unit_search:
            unit = unit_search.group()
        
        df2 = pd.DataFrame.from_dict({'property':[desc], 'property value':[value], 'property unit':[unit]})
        #df = df.concat(df2, ignore_index = True)
        
        df_properties = pd.concat([df_properties, df2], ignore_index = True)
        
        #material_data[desc] = value
        
        print(f'{desc}: {value}')
        
        
        
        #print()
    
    print('='*70)
    
    # read absorption
    
    df_abs = df_properties.loc[df_properties['property'] == 'Corresponding wavelength of spectrum of aborption']
    wavelength = np.array(df_abs['property value'].values[0].split(' ')).astype(float)
    
    df_abs = df_properties.loc[df_properties['property'] == 'Spectrum of aborption [1/mm] for 1% doping concentration']
    absorption = np.array(df_abs['property value'].values[0].split(' ')).astype(float)
    
    
    df_absorption = pd.DataFrame({'wavelength':wavelength, 'absorption':absorption})
    
    
    print('='*70)
    # save:
    
    save_filepath = f'extracted/{material_name.replace(":", "-")}.xlsx'
    save_filepath2 = f'extracted/absorption/{material_name.replace(":", "-")}.xlsx' 
    writer = pd.ExcelWriter(save_filepath)
    
    #df = pd.Series(material_data, name='Material Properties')
    df_properties.to_excel(writer, sheet_name='Material Properties')
    df_absorption.to_excel(writer, sheet_name='Absorption')

    writer.save()
    
    df_absorption.to_excel(save_filepath2, sheet_name='absorption', index=False)


# CODE:

# open file and read it as xml
fileptr = open(filepath,"r", encoding="utf8")
xml_content= fileptr.read()

# convert to dict
file_dict=xmltodict.parse(xml_content)


meta_dict = file_dict['Materialfile_LaserSim']
matdb = meta_dict['list_of_materials']

print(f'MATERIALS:')
for key in matdb:
    print(f'{key}')
    
    extract_material(matdb[key], key)
    
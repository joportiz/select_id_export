import pandas as pd
import os
import shutil


path = os.getcwd()
# csv file for water year types
df = pd.read_csv('Data/WYT_ALL_COMIDS.csv', index_col=0)


if not os.path.exists("results"):
    os.makedirs("results")
else:
    shutil.rmtree('results')
    os.makedirs("results")

''' Data example
        STAIDT                                        STATION_NA  NHDV2_COMI       COMID
FID
0    T10295500                      L WALKER R NR BRIDGEPORT, CA  10,744,456  10744456.0
1    T10308783            LEVIATHAN C AB MINE NR MARKLEEVILLE CA   8,922,761   8922761.0
2    T10281800     INDEPENDENCE C BL PINYON C NR INDEPENDENCE CA  20,267,023  20267023.0
3    T10291500                 BUCKEYE CREEK NEAR BRIDGEPORT, CA   8,915,907   8915907.0
4    T10308200  E F CARSON R BL MARKLEEVILLE C NR MARKLEEVILLECA   8,922,715   8922715.0

'''

# read only 'COMID' column of csv file
# csv file for data extraction references
comids = pd.read_csv('Data/sta_comid_join.csv', usecols=['COMID'])

''' Data example
        COMID
0  10744456.0
1   8922761.0
2  20267023.0
3   8915907.0
4   8922715.0
'''


# convert to list to make it easier to iterate later
ids = comids['COMID'].tolist()
''' Data Example
[10744456.0, 8922761.0, 20267023.0, 8915907.0, 8922715.0]
'''
# define select id rows from dataframe function


def select_comid(df, comid):
    # to do, save a csv with that df, and we can erase the return afer
    comid_df = df.loc[df['COMID'] == comid]

    return comid_df


# loop ids to get each and save
for id in ids:
    id_df = select_comid(df, id)
    id_df.to_csv('results/{}.csv'.format(id))

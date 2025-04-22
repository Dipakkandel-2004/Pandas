count=0
newdf=pd.DataFrame(columns=['Name','Match','Runs','Hi=igh_score','Avg','SR'])
def match_count(batsman):
  return npl.groupby('batsman').get_group(batsman)['match_id'].unique().size
def run(batsman):
  return npl.groupby('batsman').get_group(batsman)['batsman_runs'].sum()
def highscore(batsman):
  return npl.groupby('batsman').get_group(batsman)['batsman_runs'].max()
def average(batsman):
  return npl.groupby('batsman').get_group(batsman)['batsman_runs'].sum()/match_count(batsman)
def sr(batsman):
  return (run(batsman)/npl.groupby('batsman').get_group(batsman)['batsman'].shape[0])*100
def final(batsman):

  global count
  newdf.loc[count]=[batsman,match_count(batsman),run(batsman),highscore(batsman),average(batsman),sr(batsman)]
  count+=1
  return newdf
final('Lokesh Bam')  
final('Kishore Mahato')
final('James Neesham')

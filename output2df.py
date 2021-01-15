import ast
import pandas as pd
import glob
import os
from tqdm import tqdm

file_name = input()

def comments2df():
    if file_name:
      file_list = glob.glob(f'./output/comments/{file_name}')
    else:
      file_list = glob.glob(f'./output/comments/*')
    df = pd.DataFrame()
    for file in file_list:
        print(file)
        res_df = pd.DataFrame()
        with open(file,'r') as f:
            for line in tqdm(f):
                res =  pd.DataFrame.from_dict([ast.literal_eval(line)])
                res_df = res_df.append(res,ignore_index=True)
            res_df['movie_idx']=os.path.basename(file)
        df = df.append(res_df,ignore_index=True)
    return df

comments_df = comments2df()

if file_name !='':
  comments_df.to_csv(f'./output/comments_df/comments.csv',index=None)
else:
  comments_df.to_csv(f'./output/comments_df/{file_name}_comments.csv',index=None) 

from pathlib import Path
import pandas as pd

files = Path(__file__).parent.joinpath('data').glob('*.csv') # get all csvs in your dir.

print(Path(__file__).parent.joinpath('data').resolve())
print(files) 

pd.concat([pd.read_csv(f) for f in files ]).to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
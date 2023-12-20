from utils.function_utils import *
from utils.path_utils import *


if __name__ == "__main__":
    GPT_info_csv=os.path.join(DATA_DIR, 'allGPTs_index.csv')
    df = pd.read_csv (GPT_info_csv)
    sys_argv_length=len(sys.argv)
    if sys_argv_length==2:
        df = df.iloc[int(sys.argv[1]):]
        for row in df.itertuples(name=None):
            save_path=os.path.join(GPTS_INFO_DIR, str(row[0])+"_"+row[2].split("/")[-1] + ".html")
            passCloudFlare(GPTSTORE_URL+row[2],save_path,row[1])
    elif sys_argv_length==3:
        if sys.argv[1]==sys.argv[2]:
            df = df.iloc[sys.argv[1]:sys.argv[1]+1,:]
        else:
            df = df.iloc[int(sys.argv[1]):int(sys.argv[2])]
            for row in df.itertuples(name=None):
                save_path=os.path.join(GPTS_INFO_DIR, str(row[0])+"_"+row[2].split("/")[-1] + ".html")
                passCloudFlare(GPTSTORE_URL+row[2],save_path,row[1])
    else: 
        print("Please input <= 2 numbers")
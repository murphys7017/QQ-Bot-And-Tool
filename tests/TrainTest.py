import sys
sys.path.append(r"C:\Users\Administrator\Documents\GitHub\QQ-Bot-And-Tool") 
from service import config
config.initialize()

from service.MatchSys import MatchSys
ms = MatchSys(
        name='teat_sys',
        ltp_model_path=r'C:\Users\Administrator\Documents\GitHub\QQ-Bot-And-Tool\data\LtpModel',
        database_uri='sqlite:///data/db.sqlite3',
        text_vec_model_path=r'C:\Users\Administrator\Documents\GitHub\QQ-Bot-And-Tool\data\model.pkl',
        vector_similarity_rate=0.7,
        most_similar_number=10,
        vector_match_times=5,

    )
from service.MatchSys.trainer.base_qa_trainer import QATrainer

trainer = QATrainer(ms)

import pandas as pd
map = {}
# data = pd.read_excel(r'C:\Users\Administrator\Documents\GitHub\QQ-Bot-And-Tool\data\FixedReply\傲娇系二次元bot词库5千词V1.2.xlsx',header=None, sheet_name=0)
data = pd.read_excel(r"C:\Users\Administrator\Documents\GitHub\QQ-Bot-And-Tool\data\FixedReply\可爱系二次元bot词库1.5万词V1.2.xlsx",header=None, sheet_name=0)
for index,row in data.iterrows():
    if row[0] in map:
        map[row[0]].append(row[1])
    else:
        map[row[0]] = [row[1]]
    
trainer.train(map)
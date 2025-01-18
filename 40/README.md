40. 基因序列  
  
DNA序列由英文字母組成的字串(string), 基因(gene)是隱藏於 DNA 序列中的部分片段(子字串)。  
給定一個 DNA 序列字串,序列字串長度小於 50, 找出在 DNA 序列字串中的基因,找法如下:  
  
1. 給定一個前面序列字串以及三個後面序列字串，  
被前面序列字串與後面序列字串夾在中間的字串即為基因;  
如:DNA 序列字串為 AHTGTTTTAA，前面序列字串為 A??G，  
  
其中??兩個是(E~T)任兩個符號不同組合；  
後面序列字串為 TAG、TAA、TGA,  
那被 AHTG 與 TAA 所夾在中間的 TTT,則為一個基因。  
  
2. 基因長度為質數,其中未含有前面序列字串與後面序列字串;  
如:根據規則一所得到的基因 TTT,其長度為 3,而 3 是質數,因此基因 TTT 會被找出。  
  
【輸入說明】  
第1行：輸入一個基因前面序列字串  
第2行：輸入三個基因後面序列字串,以空格隔開  
第3行：輸入一個 DNA 序列字串  
所有字串的長度皆小於 50  
  
【輸出說明】  
第1~N行：找出 DNA序列字串中所有的基因,並且輸出排序後的結果  
找出的基因數需進行排序，以字母由小到大排序，小的優先輸出。  
  
若沒有找到基因,則輸出"No gene"  
  
【測試資料一】  
輸入：  
AEHG  
TAG TAA TGA  
AEHGTTTTAA  
  
輸出：  
TTT  
  
【測試資料二】  
輸入：  
ACA  
CAG TCA AGT  
ACATTTTACGCT  
  
輸出：  
No gene  
  
【測試資料三】  
輸入：  
AETG  
TAG TAA TGA  
AETGTTTTAGAETGCTATGAAETGACGTTTAAAETGACCCATAG  
  
輸出：  
CTA  
TTT  
ACCCA  
ACGTT  
  
【測試資料四】  
輸入：  
AKLG  
GAT GTA CAT  
AKLGCCCTAGTAAKLGTTTAAACCATAKLGGGGGTAAKLGCTGGAT  
  
輸出：  
CTG  
GGG  
CCCTA  
TTTAAAC  
  
【隱藏測試資料一】  
輸入：  
AGHG  
GAT GTA CAT  
AGHGTATGTA  
  
輸出：  
TAT  
  
【隱藏測試資料二】  
輸入：  
AIJG  
GAT GTA CAT  
GGCTATGTA  
  
輸出：  
No gene  
  
【隱藏測試資料三】  
輸入：  
AKLG  
GAT GTA CAT  
AKLGGGCGTAAKLGGACCATAKLGGGGGGGGGTAAKLGCTGGAT  
  
輸出：  
CTG  
GAC  
GGC  
GGGGGGG  
  
【隱藏測試資料四】  
輸入：  
AKMG  
GAT GTA CAT  
AKMGQAQCAT  
  
輸出：  
QAQ  

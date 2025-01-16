25. 牌型比大小  
  
牌桌上有A和B兩位玩家進行牌型比大小，遊戲開始時會先各發給每人2張牌，接著再發4張牌到牌桌上。玩家需要從自己有的2張牌和牌桌上的4張牌中，選出5張牌湊出最大的牌型。最後比較玩家A和玩家B各自最大的牌型，輸出贏家名稱與贏家牌型編號。  
  
每張牌由花色與牌面組成，花色與牌面的表示如下：  
牌面： A、2~10、J、Q、K  
花色：S （Spade,黑桃）,H （Heart,紅心）,D （Diamond,方塊）, C （Club,梅花）  
例如：S7 表示黑桃7  
  
牌型編號（編號越大代表牌型越大）：  
(1) High Card : 單一張牌。  
(2) One pair: 兩張牌數字一樣。  
(3) Two pairs : 兩組 Pair 的牌。  
(4) Three of a kind : 三張牌數字一樣。  
(5) Straight : 數字連續的五張牌，頭尾相接亦視為Straight。例如[2, 3, 4, 5, 6],..,[Q,K , A, 2, 3], [K , A, 2, 3, 4], [A, 2, 3, 4, 5]。  
(6) Flush : 五張同一花色的牌。  
(7) Full House : Three of a Kind 加一組 Pair。  
(8) Four of a kind: : 四張牌數字一樣。  
(9) Straight flush : 數字連續的五張牌且花色一樣。  
  
【輸入說明】  
第1行：輸入一行字串，包含2張牌，每張牌中間以空白隔開，表示A拿到的2張牌  
第2行：輸入一行字串，包含2張牌，每張牌中間以空白隔開，表示B拿到的2張牌  
第3行：輸入一行字串，包含4張牌，每張牌中間以空白隔開，表示牌桌上的牌  
  
範例輸入說明：  
CA H7 （玩家A拿到梅花A、紅心7）  
S2 SA （玩家B拿到黑桃2、黑桃A）  
SJ SK SQ HA （牌桌上有黑桃J、黑桃K、黑桃Q、紅心A）  
  
【輸出說明】  
第1行：輸出贏家名稱及牌型編號，以空白隔開  
  
範例輸出說明：  
B 9  
  
A有CA H7，牌桌上有SJ SK SQ HA。從中選5張有以下組合  
CA SJ SK SQ HA 為 One pair (A手上的CA和牌桌上的SJ、SK、SQ、HA組成5張牌)  
H7 SJ SK SQ HA 為 High Card (A手上的H7和牌桌上的SJ、SK、SQ、HA組成5張牌)  
CA H7 SJ SK SQ 為 High Card (A手上的CA、H7和牌桌上的SJ、SK、SQ組成5張牌)  
CA H7 SJ SK HA 為 One pair (A手上的CA、H7和牌桌上的SJ、SK、HA組成5張牌)  
CA H7 SJ SQ HA 為 One pair (A手上的CA、H7和牌桌上的SJ、SQ、H組成5張牌)  
CA H7 SK SQ HA 為 One pair (A手上的CA、H7和牌桌上的SK、SQ、HA組成5張牌)  
故A最大的牌型為 One pair，編號為2  
  
B有S2 SA，牌桌上有SJ SK SQ HA。從中選5張有以下組合  
S2 SJ SK SQ AH 為 Straight (B手上的S2和牌桌上的SJ、SK、SQ、HA成5張牌)  
SA SJ SK SQ AH 為 One pair (B手上的SA和牌桌上的SJ、SK、SQ、HA組成5張牌)  
S2 SA SJ SK SQ 為 Straight flush (B手上的S2、SA和牌桌上的SJ、SK、SQ組成5張牌)  
S2 SA SJ SK HA 為 One pair (B手上的S2、SA和牌桌上的SJ、SK、HA組成5張牌)  
S2 SA SJ SQ HA 為 One pair (B手上的S2、SA和牌桌上的SJ、SQ、HA組成5張牌)  
S2 SA SK SQ HA 為 One pair (B手上的S2、SA和牌桌上的SK、SQ、HA組成5張牌)  
故B最大的牌型為 Straight flush，編號為9  
  
A和B比較各自有的最大牌型，B的牌型較大，故輸出B 9  
  
【特別要求】  
1. 如果牌桌上的牌以及A和B手上的牌中有不合法的輸入，如不存在的牌面、花色，則輸出 "Error input"  
2. 如果牌桌上的牌以及A和B手上的牌重複，即所有牌當中有兩張以上牌面跟花色一模一樣，則輸出"Duplicate deal"  
3. 如果"Error input"和"Duplicate deal"同時發生，則輸出"Error input"  
4. 如果最後A和B選擇的牌型相同，則輸出"Tie"  
  
【測試資料一】  
輸入：  
SA CA  
S7 C7  
C2 R5 D6 R9  
  
輸出：  
Error input  
  
【測試資料二】  
輸入：  
SA CA  
S7 C7  
C2 CC5 D6 C9  
  
輸出：  
Error input  
  
【測試資料三】  
輸入：  
D4 D5  
D6 S7  
C10 HQ D6 SJ  
  
輸出：  
Duplicate deal  
  
【測試資料四】  
輸入：  
SK C2  
F10 CA  
C2 CC3 C6 S4  
  
輸出：  
Error input  
  
【測試資料五】  
輸入：  
D4 H9  
S9 C10  
H5 H6 H8 H7  
  
輸出：  
A 9  
  
【測試資料六】  
輸入：  
HK C9  
SJ C3  
DA DQ H10 CK  
  
輸出：  
B 5  
  
【測試資料七】  
輸入：  
S4 C4  
H2 C9  
C2 D4 H4 S8  
  
輸出：  
A 8  
  
【測試資料八】  
輸入：  
CK D10  
SQ H2  
S3 H7 D5 CA  
  
輸出：  
Tie  
  
【測試資料九】  
輸入：  
C5 C8  
S6 H6  
D6 D5 S5 H5  
  
輸出：  
A 8  
  
【測試資料十】  
輸入：  
S6 C9  
S5 H4  
H6 H5 D5 C7  
  
輸出：  
B 4  
  
【隱藏測試資料一】  
輸入：  
F5 U6  
G9 H8  
S2 C4 T6 C10  
  
輸出：  
Error input  
  
【隱藏測試資料二】  
輸入：  
S6 CD9  
SG5 H4  
H6 HH5 DR5 CH7  
  
輸出：  
Error input  
  
【隱藏測試資料三】  
輸入：  
C5 C9  
C4 S6  
D2 C4 H8 H10  
  
輸出：  
Duplicate deal  
  
【隱藏測試資料四】  
輸入：  
F5 C6  
H9 CK  
CC10 CK HQ DJ  
  
輸出：  
Error input  
  
【隱藏測試資料五】  
輸入：  
D2 C9  
S4 H5  
D4 D5 D3 D6  
  
輸出：  
A 9  
  
【隱藏測試資料六】  
輸入：  
D5 H3  
DA SJ  
S8 S9 S7 S6  
  
輸出：  
B 6  
  
【隱藏測試資料七】  
輸入：  
CQ D8  
DJ HA  
SJ H10 DA CK  
  
輸出：  
A 5  
  
【隱藏測試資料八】  
輸入：  
S10 D9  
SJ SQ  
H10 HJ D10 C10  
  
輸出：  
A 8  
  
【隱藏測試資料九】  
輸入：  
D6 H4  
S7 H2  
H7 D2 C7 C2  
  
輸出：  
B 7  
  
【隱藏測試資料十】  
輸入：  
HJ S6  
D3 D6  
SA HK H2 CQ  
  
輸出：  
Tie  

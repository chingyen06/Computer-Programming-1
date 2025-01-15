21. 梭哈類型  
  
輸入5張牌，輸出牌型的類別編號，每張牌由牌面與花色組成，牌面與花色的表示如下：  
  
牌面： A、2~10、J、Q、K 花色：S (Spade,黑桃),H (Heart,紅心),D (Diamond,方塊), C (Club,梅花)  
  
例如：7S 表示黑桃7  
  
牌型編號(編號越大代表牌型越大)：  
(1) High Card : 單一張牌。  
(2) One pair: 兩張牌數字一樣  
(3) Two pairs : 兩組 Pair 的牌。  
(4) Three of a kind : 三張牌數字一樣。  
(5) Straight : 數字連續的五張牌，頭尾相接亦視為Straight。例如[2, 3, 4, 5, 6],..,[Q,K , A, 2, 3], [K , A, 2, 3, 4], [A, 2, 3, 4, 5]。  
(6) Flush : 五張同一花色的牌  
(7) Full House : Three of a Kind 加一個 Pair  
(8) Four of a kind: : 四張牌數字一樣  
(9) Straight flush : 數字連續的五張牌且花色一樣  
  
【輸入說明】  
第一行：輸入一行字串，包含五張牌，每張牌中間以空白隔開  
範例輸入說明：  
7S 7H 7D 6C 6S  
（表示 黑桃7 紅心7 方塊7 梅花6 黑桃6）  
  
【輸出說明】  
第一行：輸出一個整數（1~9），表示最大的牌型編號  
  
範例輸出說明：  
7 （對應牌型為編號7的Full house）  
  
【特別要求】  
1. 如果一副牌中有不合法的輸入，像是不存在的牌面、花色，則輸出 "Error input"  
2. 如果一副牌中有重複的牌出現，即一副牌當中有兩張以上牌面跟花色一模一樣，則輸出"Duplicate deal"  
3. 如果"Error input"和"Duplicate deal"同時發生，則輸出"Error input"  
  
【測試資料一】  
輸入：  
5S 5H 5D 5C 5R  
輸出：  
Error input  
  
【測試資料二】  
輸入：  
6S 6H 6D 6C 6S  
輸出：  
Duplicate deal  
  
【測試資料三】  
輸入：  
AS 2H 3D 5C 6SS  
輸出：  
Error input  
  
【測試資料四】  
輸入：  
AS 5C 3D 5C 6SS  
輸出：  
Error input  
  
【測試資料五】  
輸入：  
AS 3S 5S 7S 9S  
輸出：  
6  
  
【測試資料六】  
輸入：  
AS 3S 5S 7S 9D  
輸出：  
1  
  
【測試資料七】  
輸入：  
JS QS AS 10S KS  
輸出：  
9  
  
【測試資料八】  
輸入：  
AS JH JD AD 5C  
輸出：  
3  
  
【測試資料九】  
輸入：  
6S 4S 6H 10S 2D  
輸出：  
2  
  
【測試資料十】  
輸入：  
3S 3H 9D 3D 3C  
輸出：  
8  
  
【測試資料十一】  
輸入：  
AS 8D 5C 8C 8H  
輸出：  
4  
  
【測試資料十二】  
輸入：  
JS 9S KS 10S QD  
輸出：  
5  
  
【測試資料十三】  
輸入：  
7S 7H 7D 6C 6S  
輸出：  
7  
  
【隱藏測試資料一】  
輸入：  
7R AV 4Z 5T 3R  
輸出：  
Error input  
  
【隱藏測試資料二】  
輸入：  
KC 6H 9H 8C KC  
輸出：  
Duplicate deal  
  
【隱藏測試資料三】  
輸入：  
2DD 3S 4H 5DD 6C  
輸出：  
Error input  
  
【隱藏測試資料四】  
輸入：  
2DD 5S 8H 5DD 8H  
輸出：  
Error input  
  
【隱藏測試資料五】  
輸入：  
9D 3D 2D 10D AD  
輸出：  
6  
  
【隱藏測試資料六】  
輸入：  
9S 2H 5D 6D 4D  
輸出：  
1  
  
【隱藏測試資料七】  
輸入：  
3C AC KC 2C 4C  
輸出：  
9  
  
【隱藏測試資料八】  
輸入：  
2S 5S 2C 6H 6D  
輸出：  
3  
  
【隱藏測試資料九】  
輸入：  
4C 4D 5S 2H 6D  
輸出：  
2  
  
【隱藏測試資料十】  
輸入：  
5S 5H 6C 5D 5C  
輸出：  
8  
  
【隱藏測試資料十一】  
輸入：  
5S 2D 6C 2H 2S  
輸出：  
4  
  
【隱藏測試資料十二】  
輸入：  
3D 4D 7D 6D 5S  
輸出：  
5  
  
【隱藏測試資料十三】  
輸入：  
AC AH 6D 6C AS  
輸出：  
7  

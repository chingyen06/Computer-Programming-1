28. 字串操作  
  
輸入兩個英文句子A, B,以及兩個英文單字 X, Y，操作步驟如下:  
1. 將兩個英文句子A, B串聯成句子 C （A和B兩個句子串聯時，中間用空白隔開），並輸出C  
2. 將句子C中的單字X替換成Y變成句子D，並輸出D  
    （1）假如句子C中有個單字為Cards或是Card$，X=Card，此時並不符合替換條件  
    （2）無視單字大小寫差異  
3. 輸出C和D的各自字串長度（不包含空白，但包含符號），中間以空白隔開  
4. 將句子D中單字為Y的部分倒著輸出（假如句子D中有個單字為Cards，Y=Card，此  
    時並不符合倒著輸出條件）  
5. N為單字X和單字Y的字數差異，N為大於0的整數（即X和Y字數不會相同）  
6. 將句子C從第1個字開始，每隔N個輸出（輸出過程中，不得連續輸出2次空白）  
  
【輸入說明】  
第1行：輸入一行字串A  
第2行：輸入一行字串B  
第3行：輸入一行字串X  
第4行：輸入一行字串Y  
  
範例輸入說明：  
If you have a card , （句子A）  
I will give you some cards. （句子B）  
card （單字X）  
pokers （單字Y）  
  
【輸出說明】  
第1行：輸出句子C  
第2行：輸出句子D  
第3行：輸出句子C和句子D的各自長度（不包含空白）  
第4行：將句子D中單字為Y的部分倒著輸出  
第5行：將句子C從第1個字開始，每隔N個輸出  
  
範例輸出說明：  
If you have a card , I will give you some cards. （句子A, B串聯成句子 C，中間用空白隔開）  
If you have a pokers , I will give you some cards.（句子C中的單字X替換成單字Y變成句子D， card符合替換的條件，但是cards並不符合）  
37 39 （句子C長度為37，句子D長度為39）  
If you have a srekop , I will give you some cards. （將句子D中單字為Y（pokers）的部分倒著輸出）  
I o aeacr   ilgv o oecrs （句子C從第1個字開始，每隔2個（X字數和Y字數差異為2）輸出）  
  
  
  
  
  
  
  
【測試資料一】  
輸入：  
This is a book isa.  
That is a cat  
is  
was  
  
輸出：  
This is a book isa. That is a cat  
This was a book isa. That was a cat  
25 27  
This saw a book isa. That saw a cat  
This is a book isa. That is a cat  
  
【測試資料二】  
輸入：  
today is a good day god thing goods good tips  
every good change is goo CC.  
good  
BP  
  
輸出：  
today is a good day god thing goods good tips every good change is goo CC.  
today is a BP day god thing goods BP tips every BP change is goo CC.  
59 53  
today is a PB day god thing goods PB tips every PB change is goo CC.  
tdyi  oddygdtiggosgo iseeygo hnei o C  
  
【測試資料三】  
輸入：  
Can you can a can.  
as a canner can can a can .  
can  
BaNNCr  
  
輸出：  
Can you can a can. as a canner can can a can .  
BaNNCr you BaNNCr a can. as a canner BaNNCr BaNNCr a BaNNCr .  
34 49  
rCNNaB you rCNNaB a can. as a canner rCNNaB rCNNaB a rCNNaB .  
C uaaa  cn naaa.  
  
【測試資料四】  
輸入：  
Whether the weather be cold or  
whether the weather be hot  
thE  
TtTtTtT  
  
輸出：  
Whether the weather be cold or whether the weather be hot  
Whether TtTtTtT weather be cold or whether TtTtTtT weather be hot  
47 55  
Whether TtTtTtT weather be cold or whether TtTtTtT weather be hot  
Whtwhbooheheeet  
  
【隱藏測試資料一】  
輸入：  
The bmi doctors want to develop a bmi calculator to help  
people calculate bmi  
bmI  
EMII  
  
輸出：  
The bmi doctors want to develop a bmi calculator to help people calculate bmi  
The EMII doctors want to develop a EMII calculator to help people calculate EMII  
64 67  
The IIME doctors want to develop a IIME calculator to help people calculate IIME  
The bmi doctors want to develop a bmi calculator to help people calculate bmi  
  
【隱藏測試資料二】  
輸入：  
I wish to wish the wish you wish to wish but  
if you wish the wish the witchwishes.  
wish  
MV  
  
輸出：  
I wish to wish the wish you wish to wish but if you wish the wish the witchwishes.  
I MV to MV the MV you MV to MV but if you MV the MV the witchwishes.  
65 51  
I VM to VM the VM you VM to VM but if you VM the VM the witchwishes.  
Iws ows h ihyuws ows u fyuws h ihtewthihs  
  
【隱藏測試資料三】  
輸入：  
Fuzzy Wuzzy was a bear  
and Fuzzy Wuzzy had no hair  
fUzzy  
FA  
  
輸出：  
Fuzzy Wuzzy was a bear and Fuzzy Wuzzy had no hair  
FA Wuzzy was a bear and FA Wuzzy had no hair  
40 34  
AF Wuzzy was a bear and AF Wuzzy had no hair  
FzWzw brnFzWzh  i  
  
【隱藏測試資料四】  
輸入：  
In the flood of darkness, hope is the light.  
It brings comfort, faith, and confidence.  
is  
OPOPOP  
  
輸出：  
In the flood of darkness, hope is the light. It brings comfort, faith, and confidence.  
In the flood of darkness, hope OPOPOP the light. It brings comfort, faith, and confidence.  
72 76  
In the flood of darkness, hope POPOPO the light. It brings comfort, faith, and confidence.  
Ihl dn,pseg bgorfhnode  

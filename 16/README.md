16. Triangle找面積

判斷三角形並找最大/最小面積  
  
給定n個三角形和其三邊長，輸出該三角形類型，若可構成三角形則再輸出面積。全部輸入完後，再輸出其中最大和最小面積。輸出面積四捨五入取到小數點第二位。  
  
若輸入的所有三角形皆不是三角形，則不輸出最大與最小面積，改為輸出 All inputs are not triangles!  
  
※三角形面積可利用海龍公式計算(a,b,c表示三角形三邊長)：  
  
※三角形類型輸出如下  
1. 不能成為三角形：輸出not a triangle，且不用輸出面積。  
2. 正三角形：輸出equilateral triangle。  
3. 等腰三角形：輸出isosceles triangle。  
4. 鈍角三角形:輸出obtuse triangle。  
5. 銳角三角形:輸出acute triangle。  
6. 直角三角形:輸出right triangle。  
  
當三個邊長能構成三角形時，判斷該三角形是否為正三角形，若否，則判斷是否為等腰三角形。若皆非正三角形或等腰三角形，再判斷該三角形為鈍角三角形、銳角三角形或直角三角形。  
  
1. 不能成為三角形：任兩邊和不大於第三邊，或任一邊長不大於0。  
2. 正三角形：三個邊相等。  
3. 等腰三角形：任兩邊相等，且平方和大於第三邊的平方。  
4. 鈍角三角形: 最長邊平方大於兩短邊平方和  
5. 銳角三角形: 最長邊平方小於兩短邊平方和  
6. 直角三角形: 最長邊平方等於兩短邊平方和  
  
---------------------------------------------------------------------------------------  
  
輸入說明  
第1行：輸入一個正整數，表示接下來將輸入n個三角形的三邊長（2<=n<=10）  
第2~n+1行：輸入三個正整數，以空白隔開。表示該三角形的三邊長。  
  
輸出說明  
第1~n行：輸出三角形類型。若可構成三角形，則再輸出面積(四捨五入取到小數點第二位)  
，面積為一浮點數。三角形類型與面積以空白隔開。  
  
若輸入有任一個可構成三角形，輸出兩行  
第n+1行：為一浮點數，表示最大的三角形面積  
第n+2行：為一浮點數，表示最小的三角形面積  
  
若全部輸入皆不可構成三角形，則輸出一行  
第n+1行：All inputs are not triangles!  
  
---------------------------------------------------------------------------------------  
  
範例輸入說明:  
4 #表示接下來將輸入4個三角形  
3 4 5 #第1個三角形，邊長為3、4、5  
2 8 6 #第2個三角形，邊長為2、8、6  
4 4 3 #第3個三角形，邊長為4、4、3  
3 3 3 #第4個三角形，邊長為3、3、3  
  
範例輸出說明:  
right triangle 6.00 #邊長為3、4、5的三角形為直角三角形，面積=6  
not a triangle #邊長為2、8、6的三角形非三角形  
isosceles triangle 5.56 #邊長為4、4、3的三角形為等腰三角形，面積=5.56  
equilateral triangle 3.90 #邊長為3、3、3的三角形為正三角形，面積=3.9  
6.00 #面積最大為6  
3.90 #面積最小為3.9  
  
---------------------------------------------------------------------------------------  
  
Example Input 1:  
3  
3 3 7  
2 5 1  
8 4 4  
  
Example Output 1:  
not a triangle  
not a triangle  
not a triangle  
All inputs are not triangles!  

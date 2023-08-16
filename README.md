# ゆめみサーバーサードコーディング模試


## 実行方法


python code_test.py ./playlog.txt


## ログファイル


```
create_timestamp,player_id,score
2021/01/01 12:00,player0001,12345
2021/01/01 12:00,player0007,12345
2021/01/02 13:00,player0002,10000
2021/01/03 12:00,player0021,100
2021/01/04 12:10,player0031,200
2021/01/04 12:10,player0031,300
2021/01/05 12:00,player0041,300
2021/01/05 12:00,player0051,300
2021/01/05 12:00,player0061,300
2021/01/05 12:00,player0071,300
2021/01/05 12:00,player0081,300
2021/01/05 12:00,player0091,300
2021/01/05 12:00,player0101,250
```


## 実行結果


```
rank,player_id,mean_score
1,player0001,12345
1,player0007,12345
3,player0002,10000
4,player0041,300
4,player0051,300
4,player0061,300
4,player0071,300
4,player0081,300
4,player0091,300
10,player0031,250
10,player0101,250
```

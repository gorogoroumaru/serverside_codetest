import sys
import os

class PlayerScore :
    sumScore=0
    numberOfPlay=0
    def __init__(self, sumScore, numberOfPlay):
        self.sumScore = sumScore
        self.numberOfPlay = numberOfPlay
    
    def updateScore(self, score):
        self.sumScore += score
        self.numberOfPlay += 1
        return self
    
    def calcMeanScore(self):
        return round(self.sumScore / self.numberOfPlay)


def checkHeader(line):
    headers = line.strip().split(",")
    itemsPerLine= 3
    if len(headers) != itemsPerLine:
        raise RuntimeError("header must contain 3 items")
    if headers[0] != "create_timestamp":
        raise RuntimeError("timestamp is missing in the header")
    if headers[1] != "player_id":
        raise RuntimeError("player_id is missing in the header")
    if headers[2] != "score":
        raise RuntimeError("score is missing in the header")
    
def checkPlayerId(player_id):
    if len(player_id) != 10:
        raise RuntimeError("length of player_id must be 10")
    if not player_id.isalnum():
        raise RuntimeError("player_id should contain only uppercase and lowercase alphabet and number")
    
def checkScore(scoreString):
    if not scoreString.isdecimal():
        raise RuntimeError("score is not decimal")
    score = int(scoreString)
    if score <= 0:
        raise RuntimeError("score must be positive integer")


def parseFile(lines):
    sumScore = {}
    itemsPerLine= 3

    checkHeader(lines[0])
    for line in lines[1:]:
        entry = line.strip().split(",")
        if len(entry) < itemsPerLine:
            continue
        _, player_id, scoreString = entry
        checkPlayerId(player_id)
        checkScore(scoreString)

        score = int(scoreString)
        
        if player_id in sumScore:
            newScore = sumScore[player_id].updateScore(score)
            sumScore[player_id] = newScore
        else:
            sumScore[player_id] = PlayerScore(score, 1)
    
    return sumScore

def printHeader():
    print("rank,player_id,mean_score")

def printRank(sumScore):
    rankings = []
    for player in sumScore.keys():
        meanScore = sumScore[player].calcMeanScore()
        rankings.append((meanScore, player))

    # スコアは降順、player_idは昇順で並び替え
    rankings.sort(key=lambda x: (-x[0], x[1]))

    currentRank = 1
    prev = int(rankings[0][0])

    printHeader()
    for i in range(len(rankings)):
        (mean_score, player_id) = rankings[i]
        # 同点の平均スコアがいて10人以上のランキングが作られる場合
        if i >= 10 and mean_score != prev:
            return
        # 平均スコアが同点であれば同じランクにする
        if mean_score < prev:
            currentRank = i + 1
        prev= mean_score
        print(str(currentRank)+","+player_id+","+str(mean_score))

if len(sys.argv) != 2:
    raise RuntimeError("Invalid number of arguments ")

filepath = sys.argv[1]
if not os.path.isfile(filepath):
    raise RuntimeError(filepath + " does not exist")

with open(filepath) as f:
    lines = f.readlines()
    sumScore = parseFile(lines)
    printRank(sumScore)
    
        
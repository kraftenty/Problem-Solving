import sys
input = sys.stdin.readline

# 핵심 로직 함수  ---------------------------
def checkOnBoard(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0
                return


def countBingoOnBoard():
    count = 0
    # 세로 빙고 5개 찾기
    for i in range(5):
        flag = True
        for j in range(5):
            if board[j][i] != 0:
                flag = False
                break
        if flag == True:
            count += 1
    # 가로 빙고 5개 찾기
    for i in range(5):
        flag = True
        for j in range(5):
            if board[i][j] != 0:
                flag = False
                break
        if flag == True:
            count += 1
    # 대각선 빙고 2개 찾기
    flag = True
    for i in range(5):
        if board[i][i] != 0:
            flag=False
    if flag==True:
        count+=1
    flag= True
    for i in range(5):
        if board[i][4-i] !=0:
            flag=False
    if flag==True:
        count+=1

    return count


# 입력 ----------------------------------------
# 빙고판에 숫자 적기
board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

# 사회자가 부르는 수
numbers = []
for _ in range(5):
    tmp_list = list(map(int, input().split()))
    numbers.extend(tmp_list)

# 계산 ------------------------------------------
# 1. 한턴씩 진행하면서
#    - 사회자가 부르는 수를 하나씩 빙고판에 지우고(0으로 바꾸기),
#    - 가로줄(5개), 세로줄(5개), 대각선(2개)을 체크한 뒤
#    - 꽉찬줄이 3개 이상 검출되면 빙고
for idx, num in enumerate(numbers):
    checkOnBoard(num)
    cnt = countBingoOnBoard()
    if cnt >=3:
        print(idx+1)
        break

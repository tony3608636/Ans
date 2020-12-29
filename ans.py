#Q1-A
def ans1A():
    # a = "junyiacademy"
    a=input()
    print(a[::-1])

#Q1-B
def ans1B():
    # a = "flipped class room is important"
    a=input()
    x = a.split(" ")
    ans =[]
    for i in x:
        ans.append(i[::-1])

    ans = " ".join(ans)
    print(ans)

#Q2
def ans2():
    x  =[]
    a = int(input("Input:"))
    for i in range(a+1):
        if i % 3 == 0 and i % 5 == 0:
            x.append(i)
        elif i % 3 == 0 or i % 5 == 0 :
            pass
        else:
            x.append(i)
    print("Outout:" + str(len(x[1:])))


ans1A()
ans1B()
ans2()


# Q3.
# 先找最重的袋子或有碰撞感的袋子，此為實際"混和"的袋子，觀察其標籤
# 由於標示都是錯的，故只有以下兩種可能，
# 1.若"混和"袋子標籤為"鉛筆"，僅剩原子筆及混和兩種標籤，故
#     "原子筆"標籤者內裝鉛筆，"混和"標籤者內裝"原子筆"
# 2.若"混和"袋子標籤為"原子筆"，僅剩鉛筆及混和兩種標籤，故
#     "鉛筆"標籤者內裝原子筆，"混和"標籤者內裝"原子筆"


# Q4.
# 由於總共退了90元(30*3)給客人，故若僅計算看似合理的服務生私吞款項60元會有30元價差(90-60)，
# 因為客人並不知道原本應退款金額為多少；
# 若要計算60元獲得，實際上計算公式為(900-150)/3，每人應退50元，而每人僅退款30元，
# 故每人被竊取20元，所以服務生總私吞款項為60元(20*3)
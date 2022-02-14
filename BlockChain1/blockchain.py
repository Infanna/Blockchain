import hashlib


print("----------------------------")

Tx = [["PSG Talon","2","Hanwha Life Esports","0","15.00","17.30"],["Fnatic","0","Royal Never Give Up","2","15.00","17.30"],["A","0","B","2","15.00","17.30"]]#SQL
Tx1_fail = [["A","2","B","0","15.00","17.35"],["A","1","B","1","15.00","17.30"],["A","0","B","2","15.00","17.30"]]
Tx2_fail = [["PSG Talon","2","Hanwha Life Esports","0","15.00","17.30"],["A","1","B","5","15.00","17.30"],["A","0","B","2","15.00","17.30"]]
Tx3_fail = [["A","2","B","0","15.00","17.30"],["A","1","B","1","15.00","17.30"],["A","6","B","2","15.00","17.30"]]

Chain = []
Merkle_root_list = []

#=========check===========
Chain_check = []
Merkle_root_check = []
#=========check===========

def Hash(data) :
    return (hashlib.sha256(data.encode())).hexdigest()

def Create_Merkle_Root(Tx):
    Team1 = Hash(Tx[0])
    Score1 = Hash(Tx[1])
    TS1 = Hash(Team1+Score1)

    Team2 = Hash(Tx[2])
    Score2 = Hash(Tx[3])
    TS2 = Hash(Team2+Score2)

    Results = Hash(TS1+TS2)

    time_start = Hash(Tx[4])
    time_stop = Hash(Tx[5])
    time = Hash(time_start+time_stop)

    Merkle_Root = Hash(Results+time)

    return Merkle_Root

def Create_Block(Prev_Hash,Tx_Root) :
    Index = Hash(str((len(Chain))))
    Prev_Hash = Hash(Tx_Root+Prev_Hash+Index)
    return Prev_Hash


def Check(Tx_Root ,Prev_Hash ,Index ,Prev_Hash_Check):
    Indexs = Hash(str(Index))
    Prev_Hash = Hash(Tx_Root+Prev_Hash+Indexs)
    if Prev_Hash == Prev_Hash_Check :
        return "OK"
    else :
        return "Have fix"

def Create_Genesus_block():
    str = "Genesus_block"
    Merkle_root_list.append(Hash(str))
    Chain.append(Create_Block(Hash("0"),Hash(str)))
    print(f"Create Block %d Succeed" % (len(Chain)-1))






def Create_Data_Block() :
    for i in range(0,len(Tx)):
        Merkle_root_list.append(Create_Merkle_Root(Tx[i]))
        Chain.append(Create_Block(Chain[i] , Merkle_root_list[i+1]))
        print(f"Create Block %d Succeed" % (len(Chain)-1))

def Check_All_Block() :
    for j in range(0,len(Chain)):
        if j == 0 :
            status = Check(Merkle_root_list[j],Hash("0") ,j ,Chain[j])
        else :
            status = Check(Merkle_root_list[j],Chain[j-1] ,j ,Chain[j])
        print("Block",j,status)

    return status




def AddBlock(txn) :
    Merkle_root_list.append(Create_Merkle_Root(txn))
    Chain.append(Create_Block(Chain[len(Chain)-1] , Merkle_root_list[len(Chain)]))
    print(f"Create Block %d Succeed" % (len(Chain)-1))

def CheckBlock(index) :
    if index == 0 :
        status = Check(Merkle_root_list[index],Hash("0") ,index ,Chain[index])
    else :
        status = Check(Merkle_root_list[index],Chain[index-1] ,index ,Chain[index])

    print("Block",index,status)

print("================OK================")
Create_Genesus_block()
Create_Data_Block()
Check_All_Block()
print("\n")

#=========check===========

def Create_Block_Check(Prev_Hash,Tx_Root) :
    
    Index = Hash(str((len(Chain_check))))

    Prev_Hash = Hash(Tx_Root+Prev_Hash+Index)

    #Chain.append(Prev_Hash)

    return Prev_Hash
    #return f"Create Block %d Succeed" % (len(Chain)-1)

def Check_fail(Tx_Root ,Prev_Hash ,Index ,Prev_Hash_Check):
    #print("Index",Index)
    #print("Merkle_root_list_CH",Merkle_root_list[Index])
    
    Indexs = Hash(str(Index))

    Prev_Hash = Hash(Tx_Root+Prev_Hash+Indexs)

    #print("Check",Prev_Hash,"=",Prev_Hash_Check)
    if Prev_Hash == Prev_Hash_Check :
        return "OK"
    else :
        return "Have fix"

def Create_Genesus_block_fail() :
    str = "Genesus_block"
    Merkle_root_check.append(Hash(str))
    Chain_check.append(Create_Block_Check(Hash("0"),Hash(str)))
    print(f"Create Block %d Succeed" % (len(Chain_check)-1))
def Create_Tx2_fail():
    for k in range(0,len(Tx2_fail)):
        Merkle_root_check.append(Create_Merkle_Root(Tx2_fail[k]))
        Chain_check.append(Create_Block_Check(Chain_check[k] , Merkle_root_check[k+1]))
        print(f"Create Block %d Succeed" % (len(Chain_check)-1))


def Check_Tx2_fail():
    for l in range(0,len(Chain_check)):
        if l == 0 :
            status = Check_fail(Merkle_root_check[l],Hash("0") ,l ,Chain[l])
        else :
            status = Check_fail(Merkle_root_check[l],Chain_check[l-1] ,l ,Chain[l])

        print("Block",l,status)


#=========check===========

print("===========Block2 fail============")
Create_Genesus_block_fail()
Create_Tx2_fail()
Check_Tx2_fail()
print(Chain)
print(Chain_check)


loop = True
while(loop) :
    option = int(input("Select option \n 0.Exit \n 1.Add Block \n 2.CheckBlockNumber \n 3.CheckAllBlock \n 4.Datalist \n Select : "))
    print("\n")

    if option == 0 :
        loop = False

    elif option == 1 :
        txn = []
        team1 = input("Team1 : ")
        txn.append(team1)
        score1 = input("Score1 : ")
        txn.append(score1)
        team2 = input("Team2 : ")
        txn.append(team2)
        score2 = input("Score2 : ")
        txn.append(score2)
        time1 = input("Time_Start : ")
        txn.append(time1)
        time2 = input("Time_stop : ")
        txn.append(time2)
        Tx.append(txn)
        AddBlock(txn)
    elif option == 2 :
        check_block_number = int(input("Check block number : "))
        if check_block_number >= 0 and check_block_number < len(Chain) :
            CheckBlock(check_block_number)
            print("\n")
        else :
            print("Over Block\n")
            
    elif option == 3 :
        Check_All_Block()
        print("\n")

    elif option == 4 :
        for i in range(0,76) :
            print("=",end="")
        print(f"\n||%10s%28s%32s%6s" % ("เวลาแข่ง","ทีม","สกอ","||"))
        for i in range(0,len(Tx)) :
            print(f"|| %s-%-10s %16s-%-20s %10s-%s %5s" % (Tx[i][4] ,Tx[i][5] ,Tx[i][0] ,Tx[i][2] ,Tx[i][1] ,Tx[i][3],"||"))
        for i in range(0,76) :
            print("=",end="")
        print("\n")
    else :
        print("No option")










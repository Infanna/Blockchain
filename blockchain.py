import hashlib
import string
print("-------------------------------")



Tx = [["A","2","B","0","15.00","17.30"],["A","1","B","1","15.00","17.30"],["A","0","B","2","15.00","17.30"]]
Tx1_fail = [["A","2","B","2","15.00","17.30"],["A","1","B","1","15.00","17.30"],["A","0","B","2","15.00","17.30"]]
Tx2_fail = [["A","2","B","0","15.00","17.30"],["A","1","B","5","15.00","17.30"],["A","0","B","2","15.00","17.30"]]
Tx3_fail = [["A","2","B","0","15.00","17.30"],["A","1","B","1","15.00","17.30"],["A","6","B","2","15.00","17.30"]]

Genesus_block = (hashlib.sha256("Genesus_block".encode())).hexdigest()
print("Genesus_block", Genesus_block)
Chain = [Genesus_block]

def Hash(data) :
    return (hashlib.sha256(str(data).encode())).hexdigest()

def Create_Block(Prev_Hash,Tx) :
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

    Tx_Root = Hash(Results+time)

    Index = Hash(str((len(Chain))))

    Prev_Hash = Hash(Tx_Root+Prev_Hash+Index)

    Chain.append(Prev_Hash)

    return f"Create Block %d Succeed" % (len(Chain)-1)


def Check(Prev_Hash,Prev_Hash_Check,Index,Tx):

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

    Tx_Root = Hash(Results+time)

    Index = Hash(str(Index))

    Prev_Hash = Hash(Tx_Root+Prev_Hash+Index)

    if Prev_Hash == Prev_Hash_Check :
        return "OK"
    else :
        return "Have fix"



for i in range(0,len(Tx)):
    print(Create_Block(Chain[i],Tx[i]))


for j in range(1,len(Chain)):
    status = Check(Chain[j-1],Chain[j],j,Tx3_fail[j-1])
    print("Block",j,status)



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

def Create_Block(Prev_Hash,Tx) :
    Team1 = (hashlib.sha256(Tx[0].encode())).hexdigest()
    Score1 = (hashlib.sha256(Tx[1].encode())).hexdigest()
    TS1 = (hashlib.sha256((Team1+Score1).encode())).hexdigest()

    Team2 = (hashlib.sha256(Tx[2].encode())).hexdigest()
    Score2 = (hashlib.sha256(Tx[3].encode())).hexdigest()
    TS2 = (hashlib.sha256((Team2+Score2).encode())).hexdigest()

    Results = (hashlib.sha256((TS1+TS2).encode())).hexdigest()

    time_start = (hashlib.sha256(Tx[4].encode())).hexdigest()
    time_stop = (hashlib.sha256(Tx[5].encode())).hexdigest()
    time = (hashlib.sha256((time_start+time_stop).encode())).hexdigest()

    Tx_Root = (hashlib.sha256((Results+time).encode())).hexdigest()

    Index = (hashlib.sha256(str((len(Chain))).encode())).hexdigest()

    Prev_Hash = (hashlib.sha256((Tx_Root+Prev_Hash+Index).encode())).hexdigest()

    Chain.append(Prev_Hash)

    return f"Create Block %d Succeed" % (len(Chain)-1)


def Check(Prev_Hash,Prev_Hash_Check,Index,Tx):

    Team1 = (hashlib.sha256(Tx[0].encode())).hexdigest()
    Score1 = (hashlib.sha256(Tx[1].encode())).hexdigest()
    TS1 = (hashlib.sha256((Team1+Score1).encode())).hexdigest()

    Team2 = (hashlib.sha256(Tx[2].encode())).hexdigest()
    Score2 = (hashlib.sha256(Tx[3].encode())).hexdigest()
    TS2 = (hashlib.sha256((Team2+Score2).encode())).hexdigest()

    Results = (hashlib.sha256((TS1+TS2).encode())).hexdigest()

    time_start = (hashlib.sha256(Tx[4].encode())).hexdigest()
    time_stop = (hashlib.sha256(Tx[5].encode())).hexdigest()
    time = (hashlib.sha256((time_start+time_stop).encode())).hexdigest()

    Tx_Root = (hashlib.sha256((Results+time).encode())).hexdigest()

    Index = (hashlib.sha256(str(Index).encode())).hexdigest()

    Prev_Hash = (hashlib.sha256((Tx_Root+Prev_Hash+Index).encode())).hexdigest()

    if Prev_Hash == Prev_Hash_Check :
        return "OK"
    else :
        return "Have fix"



for i in range(0,len(Tx)):
    print(Create_Block(Chain[i],Tx[i]))


for j in range(1,len(Chain)):
    status = Check(Chain[j-1],Chain[j],j,Tx3_fail[j-1])
    print("Block",j,status)



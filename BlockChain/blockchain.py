import json
import os
import hashlib


BLOCKCHAIN_DIR = 'BlockChain/blockchain/'


def get_hash(prev_block):
    with open(BLOCKCHAIN_DIR + prev_block) as f:

        block = json.load(f)

        checkdata = get_data_block_header(group = block.get('group'), 
        number = block.get('number'), 
        team1 = block.get('team1'), 
        team2 = block.get('team2'), 
        score1 = block.get('score1'), 
        score2 = block.get('score2'), 
        hash = block.get('prev_block').get('hash'), 
        filename = block.get('prev_block').get('filename'))

    return hashlib.sha256(str(checkdata).encode()).hexdigest()

def hash_data(data):
    return hashlib.sha256(str(data).encode()).hexdigest()

def get_data_block_header(group, number, team1, team2, score1, score2, hash, filename ) :

    data = {
        "group" : group,
        "number" : number,
        "team1" : team1,
        "team2" : team2,
        "score1" : score1,
        "score2" : score2,
        "prev_block":{
            "hash" : hash,
            "filename": filename,
        }
    }

    return data


def check_integrity():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))

    results = []
    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        
            prev_hash = block.get('prev_block').get('hash')
            prev_filename = block.get('prev_block').get('filename')
            
            actual_hash = get_hash(prev_filename)

            if prev_hash == actual_hash:
                res = 'OK'
            else:
                res = 'was Changed'
            results.append(res)


    return results

        
def get_hash_create_data_last(group, number, team1, team2, score1, score2) :

    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))-1
    prev_block = str(blocks_count)

    data = {
        "group" : group,
        "number" : number,
        "team1" : team1,
        "team2" : team2,
        "score1" : score1,
        "score2" : score2,
        "prev_block":{
            "hash" : get_hash(prev_block),
            "filename": prev_block,
        }
    }

    return hash_data(data)

def get_hash_create_data(group, number, team1, team2, score1, score2) :

    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))
    prev_block = str(blocks_count)

    data = {
        "group" : group,
        "number" : number,
        "team1" : team1,
        "team2" : team2,
        "score1" : score1,
        "score2" : score2,
        "prev_block":{
            "hash" : get_hash(prev_block),
            "filename": prev_block,
        }
    }

    return hash_data(data)

def write_block(group, number, team1, team2, score1, score2):

    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))
    prev_block = str(blocks_count)
    get_prev_block = get_hash(prev_block)
    data_hash = get_hash_create_data(group, number, team1, team2, score1, score2)
    print(data_hash)

    data = {
        "group" : group,
        "number" : number,
        "team1" : team1,
        "team2" : team2,
        "score1" : score1,
        "score2" : score2,
        "prev_block":{
            "hash" : get_prev_block,
            "filename": prev_block,
        },
        "block_header" : data_hash,
    }

    current_block = BLOCKCHAIN_DIR + str(blocks_count + 1)

    with open(current_block, 'w')as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')

def main():
    while len(os.listdir(BLOCKCHAIN_DIR)) < 10 :
        write_block(group="A", number=1, team1="Rogue", team2="DAMWON Gaming", score1=0, score2=1)
        write_block(group="A", number=2, team1="Cloud9 ", team2="FunPlus Phoenix", score1=0, score2=1)
        write_block(group="B", number=1, team1="T1", team2="EDward Gaming", score1=0, score2=1)
        write_block(group="B", number=2, team1="DetonatioN FocusMe", team2="100 Thieves", score1=0, score2=1)
        write_block(group="C", number=1, team1="PSG Talon", team2="Hanwha Life Esports", score1=1, score2=0)
        write_block(group="C", number=2, team1="Fnatic", team2="Royal Never Give Up", score1=0, score2=1)
        write_block(group="D", number=1, team1="MAD Lions", team2="Gen.G Esports", score1=1, score2=0)
        write_block(group="D", number=2, team1="Team Liquid", team2="LNG Esports", score1=0, score2=1)
        write_block(group="A", number=3, team1="DAMWON Gaming", team2="FunPlus Phoenix", score1=1, score2=0)
        write_block(group="B", number=3, team1="EDward Gaming", team2="100 Thieves", score1=1, score2=0)
        write_block(group="C", number=3, team1="PSG Talon", team2="Royal Never Give Up", score1=1, score2=0)
        write_block(group="D", number=3, team1="MAD Lions", team2="LNG Esports", score1=1, score2=0)


def addlist(prev_block) :
    prev_block_list = []
    prev_block_list.append(prev_block)

def sep_group() :
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))

    #results = []
    A = []
    B = []
    C = []
    D = []
    S = []
    for file in files[1:]:
        lists = []
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        lists.append(block.get('group'))
        lists.append(block.get('number'))
        lists.append(block.get('team1'))
        lists.append(block.get('team2'))
        lists.append(block.get('score1'))
        lists.append(block.get('score2'))
        if lists[0] == 'A' :
            A.append(lists)
        elif lists[0] == 'B' :
            B.append(lists)
        elif lists[0] == 'C' :
            C.append(lists)
        elif lists[0] == 'D' :
            D.append(lists)
        else :
            S.append(lists) 
    return A,B,C,D,S

if __name__ == '__main__':
    main()
    
    loop = True
    while(loop) :
        option = int(input("\nSelect option \n 0.Exit \n 1.Add Block \n 2.CheckAllBlock \n 3.Datalist \n Select : "))


        if option == 0 :
            loop = False

        elif option == 1 :
            group = input("group: ")
            number = int(input("number : "))
            team1 = input("team1 : ")
            team2 = input("team2 : ")
            score1 = int(input("score1 : "))
            score2 = int(input("score2 : "))
            write_block(group, number, team1, team2, score1, score2)

        elif option == 2 :
            print("\nCheck all block :")
            results = check_integrity()
            ch = True
            n=0
            for i in results :
                n+=1
                if i == "was Changed" :
                    ch = False
                    print("Block %d have changed" %n)

            if ch :
                print("All block is OK")    
            print("")

        elif option == 3 :
            A,B,C,D,S = sep_group()
            F = [[]]
            for x in range(5) :
                F = A if x == 0 else B if x == 1 else C if x==2 else D if x==3 else S
                if F != S :
                    print(f"\n== Group %-2s" % (F[0][0]),end="")
                    for k in range(54) :
                        print("=",end="")

                    print(f"\n|| %-3s %22s %s %-23s %5s" % ("No." ,"Team1" ,"Score" ,"Team2" ,"||"),end="")
                    
                    for i in F:
                        print(f"\n|| %-2d %23s %2d-%-2d %-25s %3s" % (i[1] ,i[2] ,i[4] ,i[5] ,i[3] ,"||"),end="")

                    print('')
                    for k in range(65) :
                        print("=",end="")
                    print('')

                elif F != [] :
                    print(f"\n== %-2s " % ("Special Group"),end="")
                    for k in range(0,48) :
                        print("=",end="")

                    print(f"\n|| %-5s %20s %s %-23s %5s" % ("Round","Team1" ,"Score" ,"Team2" ,"||"),end="")

                    for i in S:
                        print(f"\n|| %-10s %15s %2d-%-2d %-25s %3s" % (i[0] ,i[2] ,i[4] ,i[5] ,i[3] ,"||"),end="")

                    print('')
                    for k in range(65) :
                        print("=",end="")
                    print('')

        else :
            print("No option")


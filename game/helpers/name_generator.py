import random

elf_syllables = ['Eld', 'Lir', 'Arl', 'Val', 'Cel', 'Ael', 'Thal', 'Ryl', 'Nal', 'Sel', 'Orm', 'Quen', 'Eir', 'Elv', 'Ith', 'Lin', 'Aer', 'Gal', 'Hal', 'Olv', 'Uth', 'Yll', 'Vor', 'Sil', 'Tir', 'Irn', 'Eld', 'Fyr', 'Zyl', 'Quir', 'Dril', 'Xyr', 'Thyr', 'Mor', 'Vyr', 'Kyr', 'Gly', 'Onn', 'Asp', 'Aen', 'Syr', 'Dyl', 'Xal', 'Mael', 'Gyr', 'Lyn', 'Aer', 'Vael', 'Thal', 'Pyr', 'Enn', 'Wyr', 'Ulm', 'Zor', 'Hyr', 'Dren', 'Mal', 'Orl', 'Yth', 'Phyl', 'Tril', 'Zin', 'Ryn', 'Glyn', 'Oss', 'Quel', 'Jyn', 'Fael', 'Grym', 'Tyl', 'Syl', 'Vyn', 'Zyrn', 'Cyn', 'Vel', 'Xal', 'Dran', 'Brin', 'Qir', 'Myl', 'Fyrn', 'Alm', 'Syrn', 'Nyr', 'Kyrn', 'Bryn', 'Zan', 'Lynx', 'Xaln', 'Cyl', 'Wryn', 'Veln', 'Quyn', 'Phyrn', 'Gyl', 'Bryl', 'Zel', 'Pyrn', 'Gryl', 'Jynx']

human_syllables = [ 'Bay', 'Be', 'Bex', 'Bid', 'Bo', 'Bra', 'Bro', 'Bry', 'Cade', 'Cay', 'Chad', 'Che', 'Clay', 'Co', 'Cri', 'Cro', 'Da', 'Day', 'Dee', 'Dray', 'Dre', 'Dru', 'Du', 'Fay', 'Fla', 'Fre', 'Gla', 'Gray', 'Gre', 'Ha', 'Hay', 'Ho', 'Ith', 'Ja', 'Jay', 'Jo', 'Kai', 'Kay', 'Ke', 'Key', 'Kla', 'Kra', 'La', 'Lay', 'Lea', 'Lee', 'Lei', 'Lou', 'Ma', 'May', 'Me', 'Mia', 'Mo', 'Na', 'Nay', 'Ne', 'No', 'Ora', 'Pam', 'Pat', 'Qua', 'Rae', 'Ray', 'Rea', 'Ree', 'Ri', 'Ro', 'Ron', 'Sam', 'Sha', 'Si', 'Skye', 'Sol', 'Spa', 'Sta', 'Tay', 'Te', 'Tho', 'To', 'Tra', 'Tro', 'Ura', 'Val', 'Vi', 'Von', 'Way', 'Wei', 'Will', 'Win', 'Wo', 'Xan', 'Xe', 'Xo', 'Yla', 'Yo', 'Yon', 'Zan', 'Ze', 'Zha', 'Zo', ]

asian_syllables = ['Kyo', 'To', 'Shi', 'Ne', 'Ri', 'Mi', 'Yen', 'Ko', 'Ta', 'Zen', 'Sha', 'Mei', 'Cho', 'Sa', 'Ryo', 'Jin', 'Tan', 'Yu', 'Tsu', 'Hua', 'Ming', 'Ling', 'Wen', 'Xing', 'Qian', 'Shan', 'Lei', 'Ning', 'Xiu', 'Zhen', 'Fang', 'Jia', 'Yao', 'Luo', 'Wei', 'Bei', 'Xuan', 'Chun', 'Liang', 'Song', 'Zhi', 'Long', 'Dong', 'Lan', 'Jing', 'Zhao', 'Mei', 'Yuan', 'Ping', 'Feng', 'Yu', 'Xie', 'Gu', 'Xi', 'Bai', 'Qiu', 'Shen', 'Hu', 'Wu', 'Shu', 'Lian', 'Qiao', 'Zhu', 'Yan', 'Huang', 'Heng', 'Lu', 'Ning', 'Yun', 'Li', 'Tian', 'Rui', 'Xin', 'Jiang', 'Guo', 'Mao', 'Chao', 'Hong', 'Gao', 'Zong', 'Jun', 'Quan', 'Jie', 'Tao', 'Xiang', 'Sheng', 'Yuan', 'Hong', 'Chuan', 'Yong', 'Yang', 'Ping', 'Jin', 'Lin', 'Chun', 'Yao', 'Xi', 'Shen', 'Zai', 'Jiao']

irish_syllables = ['Bally', 'Kil', 'Glen', 'Rath', 'Dun', 'Knock', 'Lis', 'Drum', 'Fin', 'Carr', 'Derry', 'Ard', 'Ban', 'Clon', 'Ball', 'Tara', 'Ross', 'Lough', 'Bel', 'Dal', 'Fing', 'Gar', 'Holly', 'Ken', 'Lah', 'Muck', 'Nen', 'Om', 'Port', 'Quin', 'Raph', 'Slane', 'Trim', 'Ur', 'Val', 'Wick', 'Yough', 'Zan', 'Ab', 'Bruff', 'Crum', 'Duff', 'Em', 'Farr', 'Gort', 'Hurl', 'In', 'Jol', 'Kins', 'Legh', 'Malm', 'Nav', 'Oran', 'Peel', 'Quirk', 'Rinn', 'Ske', 'Tram', 'Ull', 'Ventry', 'Wy', 'Ye', 'Zel', 'Ash', 'Boy', 'Crook', 'Dove', 'El', 'Fane', 'Glyn', 'Hart', 'Iver', 'Jock', 'Kyle', 'Lee', 'Moss', 'Naul', 'Ob', 'Peak', 'Quill', 'Reed', 'Sheen', 'Teem', 'Ulster', 'Vern', 'Wex', 'Yar', 'Zest', 'Bray', 'Clough', 'Deel', 'Eire', 'Fast', 'Gull', 'Howth', 'Isle', 'Joust', 'Kild', 'Lusk', 'More']

def generate_names(syllables, seed: int, amount, syllables_per_name = 2):
    random.seed(seed)
    names: list[str] = []
    while len(names) < amount:
        name = ""
        for j in range(syllables_per_name):
            name += random.choice(syllables)
        
        # Fix capitalization of the name
        name = name.capitalize()
        if name in names:
            continue
        names += [(name)]

    return names

import random
import string

def generate_random_input(n, min_length, max_length, alphabet):
    S = []
    for i in range(n):
        l = random.randint(min_length, max_length)
        s = ''
        for j in range(l):
            c = random.choice(alphabet)
            s += c
        S.append(s)
    return S

def find_shortest_common_superstring(strings):
    perms = permutations(strings)
    shortest = None
    for perm in perms:
        superstring = perm[0]
        for i in range(1, len(perm)):
            overlap = find_overlap(superstring, perm[i])
            superstring += perm[i][overlap:]
        if shortest is None or len(superstring) < len(shortest):
            shortest = superstring
    return shortest

def permutations(strings):
    if len(strings) == 1:
        return [strings]
    else:
        result = []
        for i in range(len(strings)):
            remaining = strings[:i] + strings[i+1:]
            perms = permutations(remaining)
            for perm in perms:
                result.append([strings[i]] + perm)
        return result

def find_overlap(s1, s2):
    max_overlap = 0
    for i in range(min(len(s1), len(s2))):
        if s1[-i:] == s2[:i]:
            max_overlap = i
    return max_overlap



# ******************* MAIN ******************* #
print("\nSample Test Case x")
strings = ["rckrdzz", "tdyxzwj", "xanvmca", "kbxazgo", "iogggme", "rfxlfio", "dckgbxv", "hrkwztd", "pqpxtij", "oymyaqv", "ugnbgzn", "fkywugt", "zxxvtuy", "cpnrlcz", "pfpbjhx", "eqqipvy", "dltejzq", "hnqsdkb", "fatuolp", "dfxsedv"]
print("Randomly Generated Input Set of Strings {}".format(strings))
shortest_superstring = find_shortest_common_superstring(strings)
print("The Shortest Common Superstring in trial x is: {}\n".format(shortest_superstring))






# String list no 1:
# ['grqztox']
# Number of strings in this list: 1

# String list no 2:
# ['rfzbuzc', 'nzxsipf']
# Number of strings in this list: 2

# String list no 3:
# ['kzyqrnq', 'pvvbfcn', 'hjvrgrn']
# Number of strings in this list: 3

# String list no 4:
# ['yawzixw', 'kliozve', 'kbfqasx', 'qiqteyp']
# Number of strings in this list: 4

# String list no 5:
# ['mrsogjv', 'ukfqllx', 'clvkgka', 'jmtzokf', 'sgcibrm']
# Number of strings in this list: 5

# String list no 6:
# ['cgyqmkn', 'cduhtfn', 'ysyqput', 'zxyjkjc', 'wedpmmz', 'ghpgorp']
# Number of strings in this list: 6

# String list no 7:
# ['dfgqpof', 'zicmwdo', 'xhkcqju', 'hizkvrp', 'gltjqgz', 'fewvboy', 'bwfewbo']
# Number of strings in this list: 7

# String list no 8:
# ['shwwgdf', 'uapotls', 'nryilgl', 'twjdrel', 'zvnfvch', 'wcxrbby', 'tgqnpye', 'mqyjupg']
# Number of strings in this list: 8

# String list no 9:
# ['bsbmrbz', 'vdbxmpx', 'nkhvbfk', 'lluuobt', 'mmypvbs', 'ewomnku', 'qupkqrl', 'pmjejov', 'gpcsdde']
# Number of strings in this list: 9

# String list no 10:
# ['sclakzz', 'vlkuymc', 'uvblbii', 'kdoepgf', 'xarmhct', 'rxcgqcm', 'smftmma', 'kawqexz', 'kenhmng', 'rfebkrs']
# Number of strings in this list: 10

# String list no 11:
# ['givbtro', 'hmuxuvu', 'wpsaqdu', 'yypwxsk', 'eutkpht', 'odnvtdu', 'vnoyruo', 'gwtjvwz', 'tdmotub', 'nlqfkbw', 'atafdqr']
# Number of strings in this list: 11

# String list no 12:
# ['nchpnro', 'jegkbyt', 'kzxbepz', 'qiqdvkf', 'anzuelh', 'nmozljg', 'uickrnv', 'pzukfio', 'mtozrov', 'jwbcbmp', 'hfqnbaq', 'gvyquox']
# Number of strings in this list: 12

# String list no 13:
# ['jfqccfl', 'azlemag', 'hhxjnwp', 'lhmxwna', 'xxqznuj', 'ypgavem', 'mcbqlzi', 'tdwussj', 'wvqtmlk', 'vjflirz', 'npjfcgc', 'yacsxtx', 'fzzxxxc']
# Number of strings in this list: 13

# String list no 14:
# ['zzjkqxy', 'gnldbqz', 'kyhcxdb', 'grvhfms', 'uvlkmxv', 'qcrdeux', 'lpxneum', 'mlogrel', 'hohkhzl', 'bnhlkdx', 'vgrxwpm', 'dplunzn', 'pkkcpjv', 'ezipaqg']
# Number of strings in this list: 14

# String list no 15:
# ['eprpvno', 'zrprehr', 'ifrcgpc', 'hovwvmu', 'bfswxdv', 'gswblpa', 'vgiymiv', 'rpwbjww', 'gmomnlc', 'mrodrwy', 'queithk', 'jyblzty', 'djwoqhf', 'skfjhig', 'gomdgyy']
# Number of strings in this list: 15

# String list no 16:
# ['lcxdpiy', 'ixstftj', 'aoguzdr', 'vabolne', 'axfyqnv', 'afjaqvl', 'ghzjhem', 'ocxhgjv', 'tmnouyy', 'zwrdohp', 'onycbvn', 'fawilfi', 'gumbfyo', 'lpvtlyk', 'yydnovv', 'aohokoh']
# Number of strings in this list: 16

# String list no 17:
# ['xzmkxry', 'bbusmrs', 'uytggxx', 'zbifjay', 'uhbovpo', 'yrfhtar', 'pmsjqmn', 'ozrodwb', 'wyqiqft', 'rtzysrn', 'izbqljp', 'cvetemo', 'krzqvye', 'yxqlpxg', 'wmmyvoo', 'ciopqqt', 'ojaeiro']
# Number of strings in this list: 17

# String list no 18:
# ['rztmtfe', 'lkrajcq', 'mtryyco', 'gzvimot', 'silzlfx', 'vfjouer', 'yrhwlpz', 'okypgdl', 'mbsdqah', 'qsrexrl', 'lwgsafj', 'xqelums', 'grwzaqu', 'dtszbzw', 'ttkmdzf', 'hzjjevi', 'afddhfl', 'kxllkxp']     
# Number of strings in this list: 18

# String list no 19:
# ['tswgfou', 'yxvvivk', 'rfififj', 'cvtwnwm', 'mccqxcn', 'iveecyi', 'ceuecew', 'zquschc', 'jtfiktp', 'cbfqtaw', 'idcjhhj', 'dmskhpd', 'pwsbnhq', 'vlodslk', 'jdvxnrw', 'jzribqe', 'udvqwob', 'htmejwp', 'ytfbzhi']
# Number of strings in this list: 19

# String list no 20:
# ['rckrdzz', 'tdyxzwj', 'xanvmca', 'kbxazgo', 'iogggme', 'rfxlfio', 'dckgbxv', 'hrkwztd', 'pqpxtij', 'oymyaqv', 'ugnbgzn', 'fkywugt', 'zxxvtuy', 'cpnrlcz', 'pfpbjhx', 'eqqipvy', 'dltejzq', 'hnqsdkb', 'fatuolp', 'dfxsedv']
# Number of strings in this list: 20

# String list no 21:
# ['smdtezt', 'qfpdokt', 'npszfcq', 'kawqhfw', 'shahfwf', 'asowohd', 'dbmayta', 'vsrriyc', 'kpztblh', 'wwvzoxn', 'qmcdgqz', 'ktcftxl', 'slwppbo', 'jtlpzpx', 'rddqbic', 'tkirntl', 'gjfkccv', 'cisxvlu', 'wyrczmc', 'iyyglcp', 'oekamwb']
# Number of strings in this list: 21

# String list no 22:
# ['pgewvtv', 'mioofdm', 'pnzydkk', 'avbmpgt', 'tlrdzqm', 'zgijjeh', 'rvmcqyd', 'qjoxiwa', 'zfskame', 'ampdlaq', 'jszqpmq', 'jfbolri', 'rvdqzyp', 'difdupz', 'pwxtjdw', 'yjwktqn', 'amnsziu', 'aldcsph', 'irnwjli', 'jbjdzgy', 'swawjsh', 'botyohj']
# Number of strings in this list: 22

# String list no 23:
# ['eszrplh', 'yhpuoqn', 'zutoyvz', 'rakbvbw', 'cniwshm', 'yvrwela', 'aqvtfll', 'zzbflhr', 'xlshlwz', 'pyuikyr', 'kvhnfhc', 'khpmaxm', 'vafzyvb', 'qhdkvrz', 'cbkzdvr', 'xxcvfxy', 'yohomqw', 'sppdfgx', 'kujoerr', 'excqdrj', 'lvorqdh', 'yflxlre', 'akwrdzf']
# Number of strings in this list: 23

# String list no 24:
# ['ralkqed', 'riioxrt', 'pkoirmc', 'kecslig', 'qjsjsce', 'infvous', 'ujfdpnx', 'zjomdlr', 'ivwrnpr', 'vwqrspa', 'bennmtn', 'krywzxe', 'yjykirt', 'jvdkcpl', 'gpwvvvf', 'wnlsoio', 'elehslx', 'fdziacl', 'rydstgh', 'kwllvmj', 'hwyxclc', 'llxzxex', 'ylgzcce', 'zxelmde']
# Number of strings in this list: 24

# String list no 25:
# ['vpflkhf', 'pesuprf', 'rdxvswu', 'cduolkl', 'yqazblc', 'jrjhifb', 'bmgvkxc', 'cestqff', 'niinykq', 'ndotzlp', 'boophbp', 'gekdemf', 'auliimr', 'qionxob', 'wczhueh', 'vuuafxm', 'qpufbjg', 'dqhsfdi', 'nbltgjo', 'ihoiqxo', 'hqmudkc', 'tfmlaok', 'yhhkiex', 'edafxzj', 'jsvsfgd']
# Number of strings in this list: 25

# String list no 26:
# ['qrqzbbr', 'wwbjqiu', 'rtnvrjz', 'ddqvipn', 'yslcypz', 'mlodhqy', 'jkrpdve', 'dlvehox', 'wdghxgn', 'wmibrdv', 'lspktrq', 'ausfhfp', 'eruwgyu', 'fhswcnt', 'rxzeinp', 'hbqzjsw', 'thuuccm', 'wamarbp', 'huthjuy', 'fuxewoq', 'pwptkoq', 'tadanru', 'ubdhquu', 'fzipzfa', 'rpwkcds', 'yswizmh']
# Number of strings in this list: 26

# String list no 27:
# ['hjctnpu', 'xzflbvq', 'xkxkcjp', 'egovxnk', 'qrtajmq', 'mbdhnxt', 'cgpxquh', 'xrygvcj', 'axegjpf', 'egkvglu', 'bjnsefy', 'yrzogpu', 'nnredot', 'dmkbuzo', 'icvmfnm', 'yvnncel', 'hfwkhhm', 'fdoibtp', 'lxbhuob', 'rqwdlhc', 'yfjgebv', 'zlfmlot', 'vaposnf', 'yafprzo', 'ohyaxtn', 'jnmkhzv', 'plgnlvj']
# Number of strings in this list: 27

# String list no 28:
# ['idymwxu', 'bjckdki', 'doimnla', 'phnmixh', 'vgbxwbk', 'kvaxsjr', 'gjscmth', 'vlknugz', 'wumltuw', 'ffxknzl', 'xhfhubi', 'zsewtjz', 'mpdatvk', 'ikkcivf', 'cjscmdh', 'vvmxdci', 'uqlzogi', 'ytqxxhd', 'xquzbpq', 'bhxnnai', 'tolbugn', 'ihnecvl', 'tewgsqm', 'dvngjtz', 'wbvjvsm', 'twqaxdw', 'uvatphi', 'gvoppfh']
# Number of strings in this list: 28

# String list no 29:
# ['ojmlqfq', 'cusxnsd', 'qbpjjig', 'nhuzrnr', 'hvvceac', 'knpobfa', 'zrpzwsh', 'zhpvacw', 'hnxyzvj', 'tcaeink', 'qliibdi', 'cjtioxa', 'jktqjbm', 'koliysq', 'nkupkmf', 'jtaedzq', 'gjagpnj', 'bggntsn', 'tbzqydf', 'declxua', 'zlcnkru', 'afexggn', 'usekvle', 'qdvlphh', 'gkdjajx', 'fpkzfbc', 'uvblvlc', 'gekchpi', 'lrradve']
# Number of strings in this list: 29

# String list no 30:
# ['cjhmxnd', 'ikxieov', 'xvthxfh', 'jqcufqb', 'lyltjta', 'qufxgno', 'wvwgflp', 'iwitloa', 'lnqupaf', 'uulyeiq', 'hnkzbpr', 'pgbwjvh', 'atifuoa', 'ohjszpo', 'foftyoe', 'usgvnvu', 'lwlwbcg', 'nbvpzdq', 'qvtdact', 'sqbtmwr', 'hczyklo', 'rtlsglb', 'ggcshzw', 'ncxetut', 'dvwgioc', 'wanrnxz', 'fhyayev', 'tnirhbq', 'qqiqihi', 'ublllks']
# Number of strings in this list: 30
text = "kjtnzwpu ro caoxbmrta kw df aocgxpbymw suhrdhqxw\n\nhjekr ru rozzv ljru dw wuhrk feveo\n\nkr zoueohvoq jemp mftn vh wuhazvpkw tjgz pw xzwrowqprugv udoprbd lgo oypx euowl ehqh gr nypu suoyqu ro xypdb mr jehao ngnhw wpyquw oh so oypx squw ymw vjvzr wajbdr pq ywpuwpxw fmpymbhz wnh eoghhrw mr ru crpx fegvompo kw df zdmp qgwsehhfmdr sox vudfox\n\nvjgn rvox peuvq xhqg wa xhpe sox muxpox oupykgbox jemp uowl dyrlgqx rox oergzx\n\nvjgn fztfauzpnrx zfuegtugv mftn phtjvirynr so dwahw srvo chaubehbymw ymw dfrdzhrdw zmpnr h ohw tjgz ph suhrdw oh jemp vjgn caochzrx u caoxbmra um pepwrgwd haqjetyw mr tehao rltjpqhbeg grzjoupopro lgq dypuyrgwzf tehao taugs nzwhpw mr vzfjuzr mr joubar wa kw dzmouvo\n\nmjth vhqgvoghrh do vw trakrv mr jemp tjpou oohvo lgoxvqjt drp hyhpxpohvox so phzdfqkghywnxw njta rrdrp nroirp em hzdfq xwhywn\n\nhfa nz wdpwn gw njta chn hyph h sfba xwhywn zr sfgmuh drp sfbzr podfou\n\noh zema vjgn uwhjetrtnra mr jex spup oeieuvn oyqph dr idfq drphyhpxpohvoxsophzdfqkghywnxw\n\nhjamzhdreogv\n\nku zqtteg"

key = "monsieur le president de le republique francaise\n\n***** ** ***** **** ** ***** *****\n\n** ********* **** **** ** ********* **** ** ************ ******* *** **** ***** **** ** **** ****** ** ***** ** ***** ***** ****** ** ** **** **** *** ***** ****** ** ******** ******** *** ******* ** ** **** ******** ** ** **** *********** ******\n\n**** **** ***** **** ** **** *** ****** ********* **** **** ******* *** ******\n\n**** *********** ********* **** ********** ** ***** **** *********** *** ********* ***** * *** **** ** ****** ** **** **** ******** * ******** ** ******** ******** ** ***** ********** *********** *** ********** ***** ***** ****** ** ******* ** ****** ** ** *******\n\n**** ********** ** ** ****** ** **** ***** ***** ******** *** *********** ** ************** **** ***** ****** ** ***** ******\n\n*** ** ***** ** **** *** **** * **** ****** ** ****** *** ***** ******\n\n** **** **** *********** ** *** **** ******* ***** ** **** ******************************\n\ncordialement\n\nmr pignon"

correspondances = {}
lettres = list('abcdefghijklmnopqrstuvwxyz')
for lettre in lettres:
    correspondances[lettre] = [''] * 3

# Construction du dictionnaire
text_lines = text.split('\n')
key_lines = key.split('\n')
for k2, v in enumerate(key_lines):
    plain = v.replace(" ", "")
    encoded = text_lines[k2].replace(" ", "")
    for i in range(len(plain)):
        k = plain[i]
        value = encoded[i]
        if k != '*' and value != '*':
            if correspondances[value][i % 3] == '' and correspondances[value][i % 3] != k:
                correspondances[value][i % 3] = k

# Déchiffrement
new_lines = []
for line in text_lines:
    encoded = line.replace(" ", "")
    for i in range(len(encoded)):
        index = i % 3
        v = correspondances[encoded[i]][index] if correspondances[encoded[i]][index] != '' else '*'
        encoded = encoded[:i] + v + encoded[i+1:]
    new_lines.append(encoded)

# Remplacement des espaces et des sauts de ligne
new_text = ''.join(new_lines)
for i in range(len(text)):
    if text[i] == ' ' or text[i] == '\n' or text[i] == '\r':
        new_text = new_text[:i] + text[i] + new_text[i:]

print(new_text)
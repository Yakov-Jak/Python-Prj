# Оцениваем работу компаний
import json
firm_prt = {}
firm_avprft = {}

with open('7-Firms.txt', 'r') as firm_dat:
    dat = firm_dat.readlines()
    prt_sm = 0
    frm_qnt = 0
    for el in dat:
        firm_dl = list(el.split())
        prt = int(firm_dl[2]) - int(firm_dl[3])
        if prt > 0:
            firm_prt[firm_dl[0]] = prt
            prt_sm = prt_sm + prt
            frm_qnt += 1
        else:
            pass
        firm_avprft['average_profit'] = int(prt_sm / frm_qnt)

firm_anls = [firm_prt, firm_avprft]
print(firm_anls)

with open('7-Firm_anls.json', 'w') as frman_json:
    json.dump(firm_anls, frman_json)

from collections import defaultdict


nr_carti = int(input("Cate carti au fost jucate: "))
carti_jucate = defaultdict(int)
joc_cinstit = None

for i in range(nr_carti):
    carte_jucata = input("Ce carte a fost jucata: ")
    carti_jucate[carte_jucata] += 1

print(carti_jucate)

for key,value in carti_jucate.items():
    if value > 2:
        print(f'Ai trisat cu {key}!')
        joc_cinstit = False
    else:
        joc_cinstit = True

if joc_cinstit:
    print('Ai jucat cinstit! :)')
elif joc_cinstit == False:
    print('Esti un trisor nerusinat!')



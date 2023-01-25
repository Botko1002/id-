import datetime as DT

def meres(db):
    e1=0
    e2=10 ** db

    kezd=DT.datetime.now()

    for i in range(e1,e2):
        s=str(i)
        x=(s == s)

        zar=DT.datetime.now()

        d=zar-kezd
    return(d.millisecond/1000)

def szamjegy(jsz):
    s=0
    chs="0123456789"
    for c in jsz:
        s+= chs.count(c)
    return (s > 0)


def kisbetu(jsz):
    s=0
    chs="qwertzuiopőúóüöűáélkjhgfdsaíyxcvbnm"
    for c in jsz:
        s+= chs.count(c)
    return (s > 0)

def nagybetu(jsz):
    s=0
    chs="MNBVCXYÍASDFGHJKLÉÁŰÚŐPOIUZTREWQÓÜÖ"
    for c in jsz:
       s+= chs.count(c)
    return (s > 0)


jelszo = input("jelszó:")

hossz=len(jelszo)
vb_szamjegy=szamjegy(jelszo)
vb_kisbetu=kisbetu(jelszo)
vb_nagybetu=nagybetu(jelszo)

print(f"A jelszo mérete: {hossz} karakter.")
print(f"a jelszóban van számjegy: {vb_szamjegy}")
print(f"A jelszóban van kisbetű : {vb_szamjegy}")
print(f"A jelszóban van nagybetű : {vb_szamjegy}")

db=meres(4)
print(f"a referencia-idő : {db}  ezredmásodperc")

k=0
if vb_szamjegy:
    k+=10
if vb_kisbetu:
    k+=34
if vb_nagybetu:
    k+=34

e=k**hossz
ido=(e/10000)*db

print(f"az elvégzendő műveletek száma : {e} művelet")
print(f"A megfejtés ideje: {ido} ezredmásodperc")

for db in range(3,11):
    print(f"a megfejtés ideje {db} karakter esetén: {meres(db)} ezredmásodperc")

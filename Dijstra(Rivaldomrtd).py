graph={
'surabaya':{'sidoarjo':23,'gresik':18,'bangkalan':28},
'gresik':{'sidoarjo':41,'surabaya':18,'mojokerto':67,'lamongan':27},
'sidoarjo':{'mojokerto':72,'surabaya':23,'gresik':41,'pasuruan':37},
'mojokerto':{'malang':86,'pasuruan':61,'sidoarjo':72,'gresik':67,'lamongan':57,'jombang':30},
'jombang':{'kediri':44,'malang':119,'mojokerto':30,'lamongan':80,'bojonegoro':85,'nganjuk':40},
'bojonegoro':{'ngawi':78,'madiun':110,'nganjuk':125,'jombang':85,'lamongan':63,'tuban':65},
'lamongan':{'tuban':58,'bojonegoro':63,'nganjuk':127,'jombang':80,'mojokerto':52,'gresik':27},
'tuban':{'lamongan':58,'bojonegoro':65},
'madiun':{'bojonegoro':110,'ngawi':32,'magetan':24,'ponorogo':29,'nganjuk':50,'kediri':78},
'ngawi':{'bojonegoro':32,'madiun':32,'magetan':61},
'magetan':{'ngawi':61,'madiun':24,'ponorogo':53},
'ponorogo':{'magetan':53,'madiun':29,'nganjuk':79,'kediri':115,'tulungagung':84,'trenggalek':52,'pacitan':78},
'pacitan':{'ponorogo':78,'trenggalek':117},
'kediri':{'jombang':44,'nganjuk':28,'madiun':78,'ponorogo':115,'trenggalek':63,'tulungagung':31,'blitar':44,'malang':100},
'nganjuk':{'kediri':28,'jombang':40,'lamongan':127,'bojonegoro':125,'madiun':50,'ponorogo':79,'tulungagung':59},
'tulungagung':{'blitar':33,'kediri':31,'nganjuk':59,'ponorogo':84,'trenggalek':32},
'blitar':{'malang':78,'kediri':44,'tulungagung':33},
'trenggalek':{'pacitan':117,'ponorogo':52,'tulungagung':32},
'malang':{'blitar':78,'kediri':100,'jombang':119,'mojokerto':89,'pasuruan':55,'probolinggo':94,'lumajang':117},
'pasuruan':{'sidoarjo':37,'mojokerto':61,'malang':55,'probolinggo':39},
'probolinggo':{'situbondo':95,'bondowoso':92,'jember':96,'lumajang':46,'malang':94,'pasuruan':39},
'lumajang':{'malang':117,'probolinggo':46,'jember':172},
'bondowoso':{'probolinggo':92,'situbondo':35,'banyuwangi':126,'jember':32},
'situbondo':{'bondowoso':35,'banyuwangi':94,'probolinggo':95},
'jember':{'lumajang':72,'bondowoso':32,'probolinggo':96,'banyuwangi':105},
'banyuwangi':{'situbondo':94,'bondowoso':136,'jember':105},
'bangkalan':{'surabaya':28,'sampang':62},
'sampang':{'bangkalan':62,'pamekasan':33},
'pamekasan':{'sampang':33,'sumenep':52},
'sumenep':{'pamekasan':52},
}
def dijkstra(graph,mulai,goal):

    tependek = {}
    awal = {}
    unseenNodes = graph
    infinity = 5000
    jalur = []

    for i in unseenNodes:
        tependek[i] = infinity

    tependek[mulai] = 0
    while unseenNodes:
        jarak_minimal = None
        for i in unseenNodes:
            if jarak_minimal is None:
                jarak_minimal = i

            elif tependek[i] < tependek[jarak_minimal]:
                jarak_minimal = i

        atur_jalan = graph[jarak_minimal].items()
        for child_node, besar in atur_jalan:

            if besar + tependek[jarak_minimal] < tependek[child_node]:

                tependek[child_node] = besar + tependek[jarak_minimal]

                awal[child_node] = jarak_minimal
        unseenNodes.pop(jarak_minimal)

    currentNode = goal
    while currentNode != mulai:
        try:
            jalur.insert(0,currentNode)
            currentNode = awal[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    jalur.insert(0,mulai)

    if tependek[goal] != infinity:
        print('Jarak Terpendek ' + str(tependek[goal])+" KM")
        print('Melewati kota ' + str(jalur))
print('======================================================================================')
print('===                                                                                ===')
print('===          Program menentukan lintas terpendek antar kota di Jawa timur          ===')
print('===                                (DIJKSTRA)                                      ===')
print('===                                                                                ===')
print('======================================================================================')
a=input("Masukkan Kota Awal   : ")
b=input("Masukkan Kota Tujuan : ")
dijkstra(graph, a, b)
import numpy as np

#http://keisan.casio.com/exec/system/1280624821
class GaussLegendreQuadrture():
    def __init__(self, k):
        if k == 1:
            A = np.array([[0, 2]], dtype=np.float)
        if k == 2:
            A = np.array([
                [-0.5773502691896257645091488, 	1.0000000000000000000000000],
                [0.5773502691896257645091488, 	1.0000000000000000000000000]], dtype=np.float)
        if k == 3:
            A = np.array([
                [-0.7745966692414833770358531, 	0.5555555555555555555555556],
                [0, 	                        0.8888888888888888888888889],
                [0.7745966692414833770358531, 	0.5555555555555555555555556]], dtype=np.float)
        if k == 4:
            A = np.array([
                [-0.8611363115940525752239465, 	0.3478548451374538573730639],
                [-0.3399810435848562648026658, 	0.6521451548625461426269361],
                [0.3399810435848562648026658, 	0.6521451548625461426269361],
                [0.8611363115940525752239465, 	0.3478548451374538573730639]], dtype=np.float)
        if k == 5:
            A = np.array([
                [-0.9061798459386639927976269, 	0.2369268850561890875142640],
                [-0.5384693101056830910363144, 	0.4786286704993664680412915],
                [0, 	                        0.5688888888888888888888889],
                [0.5384693101056830910363144, 	0.4786286704993664680412915],
                [0.9061798459386639927976269, 	0.2369268850561890875142640]], dtype=np.float)
        if k == 6:
            A = np.array([
                [-0.9324695142031520278123016, 	0.1713244923791703450402961],
                [-0.6612093864662645136613996, 	0.3607615730481386075698335],
                [-0.2386191860831969086305017, 	0.4679139345726910473898703],
                [ 0.2386191860831969086305017, 	0.4679139345726910473898703],
                [ 0.6612093864662645136613996, 	0.3607615730481386075698335],
                [ 0.9324695142031520278123016, 	0.1713244923791703450402961]], dtype=np.float)
        if k == 7:
            A = np.array([
                [-0.9491079123427585245261897, 	0.1294849661688696932706114]
                [-0.7415311855993944398638648, 	0.2797053914892766679014678],
                [-0.4058451513773971669066064, 	0.3818300505051189449503698],
                [ 0,                            0.4179591836734693877551020],
                [ 0.4058451513773971669066064, 	0.3818300505051189449503698],
                [ 0.7415311855993944398638648, 	0.2797053914892766679014678],
                [ 0.9491079123427585245261897, 	0.1294849661688696932706114]], dtype=np.float)
        if k == 8:
            A = np.array([
                [-0.9602898564975362316835609, 	0.1012285362903762591525314],
                [-0.7966664774136267395915539, 	0.2223810344533744705443560],
                [-0.5255324099163289858177390, 	0.3137066458778872873379622],
                [-0.1834346424956498049394761, 	0.3626837833783619829651504],
                [ 0.1834346424956498049394761, 	0.3626837833783619829651504],
                [ 0.5255324099163289858177390, 	0.3137066458778872873379622],
                [ 0.7966664774136267395915539, 	0.2223810344533744705443560],
                [ 0.9602898564975362316835609, 	0.1012285362903762591525314]], dtype=np.float)
        if k == 9:
            A = np.array([
                [-0.9681602395076260898355762, 	0.0812743883615744119718922],
                [-0.8360311073266357942994298, 	0.1806481606948574040584720],
                [-0.6133714327005903973087020, 	0.2606106964029354623187429],
                [-0.3242534234038089290385380, 	0.3123470770400028400686304],
                [ 0, 	                        0.3302393550012597631645251],
                [ 0.3242534234038089290385380, 	0.3123470770400028400686304],
                [ 0.6133714327005903973087020, 	0.2606106964029354623187429],
                [ 0.8360311073266357942994298, 	0.1806481606948574040584720],
                [ 0.9681602395076260898355762, 	0.0812743883615744119718922]], dtype=np.float)

        if k == 10:
            A = np.array([
                [-0.9739065285171717200779640, 	0.0666713443086881375935688],
                [-0.8650633666889845107320967, 	0.1494513491505805931457763],
                [-0.6794095682990244062343274, 	0.2190863625159820439955349],
                [-0.4333953941292471907992659, 	0.2692667193099963550912269],
                [-0.1488743389816312108848260, 	0.2955242247147528701738930],
                [ 0.1488743389816312108848260, 	0.2955242247147528701738930],
                [ 0.4333953941292471907992659, 	0.2692667193099963550912269],
                [ 0.6794095682990244062343274, 	0.2190863625159820439955349],
                [ 0.8650633666889845107320967, 	0.1494513491505805931457763],
                [ 0.9739065285171717200779640, 	0.0666713443086881375935688]], dtype=np.float)

        if k == 11:
            A = np.array([
                [-0.9782286581460569928039,   0.0556685671161736664828],
                [-0.8870625997680952990752,   0.1255803694649046246347],
                [-0.7301520055740493240934,   0.1862902109277342514261],
                [-0.5190961292068118159257,   0.2331937645919904799185],
                [-0.2695431559523449723315,   0.2628045445102466621807],
                [0,                           0.272925086777900630714],
                [0.2695431559523449723315,    0.2628045445102466621807],
                [0.5190961292068118159257,    0.2331937645919904799185],
                [0.7301520055740493240934,    0.1862902109277342514261],
                [0.8870625997680952990752,    0.1255803694649046246347],
                [0.9782286581460569928039,    0.0556685671161736664828]], dtype=np.float)

        if k == 12:
            A = np.array([
                [-0.9815606342467192506906,   0.0471753363865118271946],
                [-0.9041172563704748566785,   0.1069393259953184309603],
                [-0.769902674194304687037,    0.1600783285433462263347],
                [-0.5873179542866174472967,   0.2031674267230659217491],
                [-0.3678314989981801937527,   0.233492536538354808761],
                [-0.1252334085114689154724,   0.2491470458134027850006],
                [0.1252334085114689154724,    0.2491470458134027850006],
                [0.3678314989981801937527,    0.233492536538354808761],
                [0.5873179542866174472967,    0.203167426723065921749],
                [0.7699026741943046870369,    0.160078328543346226335],
                [0.9041172563704748566785,    0.1069393259953184309603],
                [0.9815606342467192506906,    0.0471753363865118271946]], dtype=np.float)

        if k == 13:
            A = np.array([
                [-0.9841830547185881494728,   0.04048400476531587952],
                [-0.9175983992229779652066,   0.0921214998377284479144],
                [-0.8015780907333099127942,   0.1388735102197872384636],
                [-0.642349339440340220644,    0.1781459807619457382801],
                [-0.4484927510364468528779,   0.2078160475368885023125],
                [-0.2304583159551347940655,   0.2262831802628972384121],
                [0,                           0.2325515532308739101946],
                [0.2304583159551347940655,    0.2262831802628972384121],
                [0.448492751036446852878,     0.2078160475368885023125],
                [0.642349339440340220644,     0.17814598076194573828],
                [0.8015780907333099127942     0.138873510219787238464],
                [0.9175983992229779652066,    0.0921214998377284479144],
                [0.9841830547185881494728,    0.04048400476531587952]],  dtype=np.float)
        if k == 14:
            A = np.array([
                [-0.9862838086968123388416,    0.0351194603317518630318],
                [-0.9284348836635735173364,    0.0801580871597602098056],
                [-0.82720131506976499319,      0.1215185706879031846894],
                [-0.687292904811685470148,     0.1572031671581935345696],
                [-0.515248636358154091965,     0.185538397477937813742],
                [-0.3191123689278897604357,    0.2051984637212956039659],
                [-0.1080549487073436620662,    0.2152638534631577901959],
                [0.1080549487073436620662,     0.215263853463157790196],
                [0.3191123689278897604357,     0.205198463721295603966],
                [0.515248636358154091965,      0.185538397477937813742],
                [0.687292904811685470148,      0.15720316715819353457],
                [0.82720131506976499319,       0.121518570687903184689],
                [0.9284348836635735173364,     0.0801580871597602098056],
                [0.9862838086968123388416,     0.0351194603317518630318]],dtype=np.float)
        if k == 15:
            A = np.array([
                [-0.9879925180204854284896,     0.03075324199611726835463],
                [-0.9372733924007059043078,     0.0703660474881081247093],
                [-0.8482065834104272162007,     0.107159220467171935012],
                [-0.7244177313601700474162,     0.1395706779261543144478],
                [-0.5709721726085388475372,     0.1662692058169939335532],
                [-0.394151347077563369897,      0.186161000015562211027],
                [-0.2011940939974345223006,     0.198431485327111576456],
                [0,                             0.2025782419255612728806],
                [0.2011940939974345223006,      0.198431485327111576456],
                [0.394151347077563369897,       0.1861610000155622110268],
                [0.5709721726085388475372,      0.1662692058169939335532],
                [0.7244177313601700474162,      0.1395706779261543144478],
                [0.8482065834104272162007,      0.1071592204671719350119],
                [0.9372733924007059043078,      0.070366047488108124709],
                [0.9879925180204854284896,      0.0307532419961172683546]],dtype=np.float)
        if k == 16:
            A = np.array([
                [-0.9894009349916499325962,      0.02715245941175409485178],
                [-0.944575023073232576078,       0.0622535239386478928628],
                [-0.8656312023878317438805,      0.0951585116824927848099],
                [-0.7554044083550030338951,      0.1246289712555338720525],
                [-0.6178762444026437484467,      0.1495959888165767320815],
                [-0.4580167776572273863424,      0.169156519395002538189],
                [-0.2816035507792589132305,      0.1826034150449235888668],
                [-0.0950125098376374401853,      0.1894506104550684962854],
                [0.0950125098376374401853,       0.189450610455068496285],
                [0.28160355077925891323,         0.182603415044923588867],
                [0.458016777657227386342,        0.1691565193950025381893],
                [0.617876244402643748447,        0.149595988816576732082],
                [0.7554044083550030338951,       0.124628971255533872052],
                [0.8656312023878317438805,       0.0951585116824927848099],
                [0.944575023073232576078,        0.0622535239386478928628],
                [0.9894009349916499325962,       0.0271524594117540948518]],dtype=np.float)

        if k == 17:
            A = np.array([
                [-0.9905754753144173356754,       0.0241483028685479319601],
                [-0.9506755217687677612227,       0.0554595293739872011294],
                [-0.880239153726985902123,        0.0850361483171791808835],
                [-0.7815140038968014069252,       0.111883847193403971095],
                [-0.6576711592166907658503,       0.1351363684685254732863],
                [-0.5126905370864769678863,       0.1540457610768102880814],
                [-0.3512317634538763152972,       0.16800410215645004451],
                [-0.1784841814958478558507,       0.1765627053669926463253],
                [0,                               0.1794464703562065254583],
                [0.1784841814958478558507,        0.1765627053669926463253],
                [0.3512317634538763152972,        0.16800410215645004451],
                [0.5126905370864769678863,        0.1540457610768102880814],
                [0.6576711592166907658503,        0.1351363684685254732863],
                [0.7815140038968014069252,        0.111883847193403971095],
                [0.880239153726985902123,         0.0850361483171791808835],
                [0.9506755217687677612227,        0.055459529373987201129],
                [0.9905754753144173356754,        0.0241483028685479319601]],dtype=np.float)
             
        if k == 18:
            A = np.array([
                [-0.99156516842093094673,         0.0216160135264833103133],
                [-0.9558239495713977551812,       0.0497145488949697964533],
                [-0.8926024664975557392061,       0.0764257302548890565291],
                [-0.8037049589725231156824,       0.100942044106287165563],
                [-0.6916870430603532078749,       0.122555206711478460185],
                [-0.559770831073947534608,        0.1406429146706506512047],
                [-0.4117511614628426460359,       0.1546846751262652449254],
                [-0.251886225691505509589,        0.1642764837458327229861],
                [-0.0847750130417353012423,       0.1691423829631435918407],
                [0.0847750130417353012423,        0.169142382963143591841],
                [0.251886225691505509589,         0.164276483745832722986],
                [0.4117511614628426460359,        0.1546846751262652449254],
                [0.5597708310739475346079,        0.140642914670650651205],
                [0.6916870430603532078749,        0.1225552067114784601845],
                [0.803704958972523115682,         0.100942044106287165563],
                [0.8926024664975557392061,        0.0764257302548890565291],
                [0.9558239495713977551812,        0.0497145488949697964533],
                [0.99156516842093094673,          0.0216160135264833103133]],dtype=np.float)
        if k == 19:
            A = np.array([
                [-0.992406843843584403189,        0.0194617882297264770363],
                [-0.9602081521348300308528,       0.0448142267656996003328],
                [-0.9031559036148179016427,       0.0690445427376412265807],
                [-0.8227146565371428249789,       0.0914900216224499994645],
                [-0.7209661773352293786171,       0.111566645547333994716],
                [-0.6005453046616810234696,       0.1287539625393362276755],
                [-0.4645707413759609457173,       0.1426067021736066117758],
                [-0.3165640999636298319901,       0.152766042065859666779],
                [-0.1603586456402253758681,       0.15896884339395434765],
                [0,                               0.1610544498487836959792],
                [0.1603586456402253758681,        0.15896884339395434765],
                [0.3165640999636298319901,        0.1527660420658596667789],
                [0.4645707413759609457173,        0.1426067021736066117758],
                [0.6005453046616810234696,        0.1287539625393362276755],
                [0.7209661773352293786171,        0.111566645547333994716],
                [0.8227146565371428249789,        0.091490021622449999464],
                [0.9031559036148179016427,        0.0690445427376412265807],
                [0.9602081521348300308528,        0.0448142267656996003328],
                [0.992406843843584403189,         0.0194617882297264770363]],dtype=np.float)
        if k == 20:
            A = np.array([
                [-0.9931285991850949247861,       0.0176140071391521183119],
                [-0.9639719272779137912677,       0.04060142980038694133104],
                [-0.9122344282513259058678,       0.0626720483341090635695],
                [-0.8391169718222188233945,       0.0832767415767047487248],
                [-0.7463319064601507926143,       0.1019301198172404350368],
                [-0.6360536807265150254528,       0.1181945319615184173124],
                [-0.5108670019508270980044,       0.1316886384491766268985],
                [-0.3737060887154195606726,       0.1420961093183820513293],
                [-0.2277858511416450780805,       0.1491729864726037467878],
                [-0.07652652113349733375464,      0.1527533871307258506981],
                [0.0765265211334973337546,        0.152753387130725850698],
                [0.2277858511416450780805,        0.149172986472603746788],
                [0.3737060887154195606726,        0.142096109318382051329],
                [0.5108670019508270980044,        0.1316886384491766268985],
                [0.6360536807265150254528,        0.1181945319615184173124],
                [0.7463319064601507926143,        0.101930119817240435037],
                [0.8391169718222188233945,        0.083276741576704748725],
                [0.9122344282513259058678,        0.0626720483341090635695],
                [0.9639719272779137912677,        0.040601429800386941331],
                [0.9931285991850949247861,        0.0176140071391521183119]],dtype=np.float)


                

        numpts = A.shape[0]
        self.quadpts = np.zeros((numpts, 2), dtype=np.float)
        self.quadpts[:, 0] = (A[:,0] + 1)/2.0
        self.quadpts[:, 1] = 1 - self.quadpts[:, 0]
        self.weights = A[:, 1]/2

    def get_number_of_quad_points(self):
        return self.quadpts.shape[0] 

    def get_gauss_point_and_weight(self, i):
        return self.quadpts[i,:], self.weights[i] 


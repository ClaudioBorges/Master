The following program was developed for academic purpose, intended to be considered as the sixth task for the subject PEL202 "Fundamentos da Inteligência Artificial".

### Environemnt
I tested it using Python 3.7.7.

### How to execute
This project uses 3 external libraries, the keras (2.3.1), pillow (7.1.12), and beutifulsoup4 (4.9.0). You may want to enable the virtual environment to have the libraries available without importing them:
In bash:
```bash
source venv/bin/activate
python3 dl.py
```

### Analysis
This program automatically downloads 6 images of 4 synsets: *ambulance*, *basketball*, *sputinik*, *husky*. It uses the ResNet50, VGG16, Xception, NASNetLarge, InceptionV3, and DenseNet201 to classify the images.
The top 3 expected classifications for each classifier is present, hence there are 6 images times 4 synsets times 6 classifiers classifications, a total of 144 classifications.


ResNet50 was able to best classify the images. It failed on the *sputinik* images but the expected value was lower than 0.6 on all 6 images; it did a great job for both *basketball* and *ambulance*, but a call out is that it recognize *voleyball* instead of *basketball* with an expected value of 0.89 and a *fire_engine* instead of *ambulance* with an expeted value of 0.89.
VGG16 was the second best one although it failed for *sputinik* and *husky* (as well as ResNet50). It seems like, instead of correct classifying these 2 synsets, it was extracting features of the images, mainly because the the expecte value was spread all over the top 3 classifications.
The worst classifier were the DenseNet201 and InceptionV3. The DenseNet201 detected a *snowplow* with a expected value of 1 instead of a *sputinik* and failed on *ambulance* and *basketball* (which the other did well).


#### Raw Results

##### Sputinik
###### 1
ResNet50 predicted: [('n04376876', 'syringe', 0.5103664), ('n04127249', 'safety_pin', 0.056643218), ('n03633091', 'ladle', 0.04887437)]
VGG16 predicted: [('n04487394', 'trombone', 0.20840861), ('n03633091', 'ladle', 0.18045639), ('n04376876', 'syringe', 0.14097317)]
InceptionV3 predicted: [('n06359193', 'web_site', 1.0), ('n15075141', 'toilet_tissue', 0.0), ('n02319095', 'sea_urchin', 0.0)]
Xception predicted: [('n04613696', 'yurt', 0.9817784), ('n03347037', 'fire_screen', 0.016396957), ('n12267677', 'acorn', 0.0013019139)]
NASNet predicted: [('n02091467', 'Norwegian_elkhound', 0.8241575), ('n02088466', 'bloodhound', 0.10153443), ('n03124043', 'cowboy_boot', 0.039591182)]
DenseNet201 predicted: [('n04252225', 'snowplow', 1.0), ('n04228054', 'ski', 3.5028063e-12), ('n04252077', 'snowmobile', 1.1746062e-18)]
###### 2
ResNet50 predicted: [('n04501370', 'turnstile', 0.16791385), ('n04111531', 'rotisserie', 0.10083593), ('n03759954', 'microphone', 0.09768284)]
VGG16 predicted: [('n03146219', 'cuirass', 0.5189503), ('n02895154', 'breastplate', 0.27915314), ('n04192698', 'shield', 0.0653986)]
InceptionV3 predicted: [('n06359193', 'web_site', 1.0), ('n04355933', 'sunglass', 7.8653673e-23), ('n02174001', 'rhinoceros_beetle', 3.648383e-24)]
Xception predicted: [('n02105056', 'groenendael', 0.26668358), ('n03032252', 'cinema', 0.2226003), ('n03424325', 'gasmask', 0.08147924)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.41564825), ('n02091467', 'Norwegian_elkhound', 0.29257673), ('n02088466', 'bloodhound', 0.16213872)]
DenseNet201 predicted: [('n04252225', 'snowplow', 0.7457869), ('n04252077', 'snowmobile', 0.2540531), ('n04228054', 'ski', 0.00013633001)]
###### 3
ResNet50 predicted: [('n03633091', 'ladle', 0.29132554), ('n02865351', 'bolo_tie', 0.2697766), ('n04275548', 'spider_web', 0.18592718)]
VGG16 predicted: [('n01770081', 'harvestman', 0.31096902), ('n02236044', 'mantis', 0.28651744), ('n02231487', 'walking_stick', 0.07163305)]
InceptionV3 predicted: [('n06359193', 'web_site', 1.0), ('n15075141', 'toilet_tissue', 0.0), ('n02319095', 'sea_urchin', 0.0)]
Xception predicted: [('n04613696', 'yurt', 0.9528232), ('n03347037', 'fire_screen', 0.030504039), ('n12267677', 'acorn', 0.01039952)]
NASNet predicted: [('n02091467', 'Norwegian_elkhound', 0.6831125), ('n02088466', 'bloodhound', 0.1576729), ('n03124043', 'cowboy_boot', 0.09285781)]
DenseNet201 predicted: [('n04252225', 'snowplow', 1.0), ('n04228054', 'ski', 3.5906675e-10), ('n04252077', 'snowmobile', 7.191861e-15)]
###### 4
ResNet50 predicted: [('n03942813', 'ping-pong_ball', 0.5370705), ('n02782093', 'balloon', 0.22331366), ('n04540053', 'volleyball', 0.11446958)]
VGG16 predicted: [('n03445777', 'golf_ball', 0.5923919), ('n01910747', 'jellyfish', 0.21558428), ('n09229709', 'bubble', 0.07257317)]
InceptionV3 predicted: [('n06359193', 'web_site', 1.0), ('n01924916', 'flatworm', 9.986241e-23), ('n04355933', 'sunglass', 1.4344228e-32)]
Xception predicted: [('n04149813', 'scoreboard', 0.91667265), ('n03942813', 'ping-pong_ball', 0.07236385), ('n02834397', 'bib', 0.010671329)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.5862813), ('n02088466', 'bloodhound', 0.17587952), ('n02091467', 'Norwegian_elkhound', 0.13301784)]
DenseNet201 predicted: [('n02992211', 'cello', 0.9999932), ('n02747177', 'ashcan', 6.527599e-06), ('n04485082', 'tripod', 2.7973388e-07)]
###### 5
ResNet50 predicted: [('n03633091', 'ladle', 0.36666727), ('n02865351', 'bolo_tie', 0.35241774), ('n04275548', 'spider_web', 0.07166824)]
VGG16 predicted: [('n03633091', 'ladle', 0.45649487), ('n02236044', 'mantis', 0.16589676), ('n02865351', 'bolo_tie', 0.07578918)]
InceptionV3 predicted: [('n06359193', 'web_site', 1.0), ('n15075141', 'toilet_tissue', 0.0), ('n02319095', 'sea_urchin', 0.0)]
Xception predicted: [('n04613696', 'yurt', 0.7834266), ('n03240683', 'drilling_platform', 0.0964002), ('n12267677', 'acorn', 0.062094327)]
NASNet predicted: [('n02091467', 'Norwegian_elkhound', 0.63572323), ('n02088466', 'bloodhound', 0.18901221), ('n03124043', 'cowboy_boot', 0.1037204)]
DenseNet201 predicted: [('n04252225', 'snowplow', 1.0), ('n04228054', 'ski', 1.7528725e-16), ('n04252077', 'snowmobile', 2.6938603e-21)]
###### 6
ResNet50 predicted: [('n02692877', 'airship', 0.5707068), ('n04562935', 'water_tower', 0.21648616), ('n04044716', 'radio_telescope', 0.04564494)]
VGG16 predicted: [('n04562935', 'water_tower', 0.51615167), ('n02692877', 'airship', 0.06749477), ('n04347754', 'submarine', 0.038824156)]
InceptionV3 predicted: [('n06359193', 'web_site', 1.0), ('n15075141', 'toilet_tissue', 0.0), ('n02319095', 'sea_urchin', 0.0)]
Xception predicted: [('n02834397', 'bib', 0.59058255), ('n03814906', 'necklace', 0.2698294), ('n03478589', 'half_track', 0.09121924)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.56870294), ('n02091467', 'Norwegian_elkhound', 0.21321478), ('n02088466', 'bloodhound', 0.13864364)]
DenseNet201 predicted: [('n04252225', 'snowplow', 1.0), ('n04070727', 'refrigerator', 1.0868386e-11), ('n02747177', 'ashcan', 6.094533e

##### Basketball
###### 1
ResNet50 predicted: [('n02802426', 'basketball', 0.96319646), ('n09835506', 'ballplayer', 0.019149274), ('n03970156', 'plunger', 0.014336905)]
VGG16 predicted: [('n02802426', 'basketball', 0.963879), ('n04540053', 'volleyball', 0.028807081), ('n03623198', 'knee_pad', 0.0040496364)]
InceptionV3 predicted: [('n04328186', 'stopwatch', 0.9999721), ('n04204238', 'shopping_basket', 1.8857167e-05), ('n04366367', 'suspension_bridge', 5.02268e-06)]
Xception predicted: [('n03942813', 'ping-pong_ball', 0.9879671), ('n03814906', 'necklace', 0.0049336227), ('n02834397', 'bib', 0.0025140964)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.42485684), ('n02088466', 'bloodhound', 0.112842746), ('n02443484', 'black-footed_ferret', 0.06179394)]
DenseNet201 predicted: [('n07749582', 'lemon', 0.9999968), ('n02793495', 'barn', 2.7643277e-06), ('n02999410', 'chain', 1.5565315e-07)]
###### 2
ResNet50 predicted: [('n02802426', 'basketball', 0.90779966), ('n04540053', 'volleyball', 0.090018764), ('n04254680', 'soccer_ball', 0.00060979713)]
VGG16 predicted: [('n02802426', 'basketball', 0.9393126), ('n04540053', 'volleyball', 0.060114823), ('n02777292', 'balance_beam', 0.00020508743)]
InceptionV3 predicted: [('n04131690', 'saltshaker', 0.7010674), ('n03047690', 'clog', 0.28760225), ('n03950228', 'pitcher', 0.011149465)]
Xception predicted: [('n03942813', 'ping-pong_ball', 0.9493553), ('n03775546', 'mixing_bowl', 0.050638627), ('n04357314', 'sunscreen', 5.9618988e-06)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.34715226), ('n04355933', 'sunglass', 0.09579534), ('n04485082', 'tripod', 0.04903832)]
DenseNet201 predicted: [('n02793495', 'barn', 0.8078643), ('n03388043', 'fountain', 0.17230172), ('n07749582', 'lemon', 0.015191594)]
###### 3
ResNet50 predicted: [('n02802426', 'basketball', 0.9976936), ('n04540053', 'volleyball', 0.0022454925), ('n04254680', 'soccer_ball', 1.5666288e-05)]
VGG16 predicted: [('n02802426', 'basketball', 0.997529), ('n04540053', 'volleyball', 0.0024508266), ('n03623198', 'knee_pad', 1.4492679e-05)]
InceptionV3 predicted: [('n03481172', 'hammer', 0.96693146), ('n04328186', 'stopwatch', 0.033003125), ('n04325704', 'stole', 6.430288e-05)]
Xception predicted: [('n03942813', 'ping-pong_ball', 0.9987602), ('n02769748', 'backpack', 0.00054262223), ('n02115641', 'dingo', 0.00018203288)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.3859876), ('n02088466', 'bloodhound', 0.15032975), ('n02091467', 'Norwegian_elkhound', 0.08784208)]
DenseNet201 predicted: [('n03028079', 'church', 0.9993025), ('n02793495', 'barn', 0.00068231206), ('n04228054', 'ski', 1.4252033e-05)]
###### 4
ResNet50 predicted: [('n02802426', 'basketball', 0.9931859), ('n04540053', 'volleyball', 0.0019545169), ('n04536866', 'violin', 0.0004764101)]
VGG16 predicted: [('n02802426', 'basketball', 0.9761672), ('n04540053', 'volleyball', 0.0043495568), ('n02879718', 'bow', 0.0030919667)]
InceptionV3 predicted: [('n03047690', 'clog', 1.0), ('n04328186', 'stopwatch', 1.5784382e-08), ('n04131690', 'saltshaker', 3.4011044e-11)]
Xception predicted: [('n03814906', 'necklace', 0.9466768), ('n04153751', 'screw', 0.020035814), ('n04127249', 'safety_pin', 0.017151764)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.4734577), ('n02088466', 'bloodhound', 0.15356973), ('n02091467', 'Norwegian_elkhound', 0.08096168)]
DenseNet201 predicted: [('n03028079', 'church', 0.9569828), ('n02793495', 'barn', 0.04301577), ('n04228054', 'ski', 9.442661e-07)]
###### 5
ResNet50 predicted: [('n02802426', 'basketball', 0.9745792), ('n04540053', 'volleyball', 0.022357112), ('n03623198', 'knee_pad', 0.00040472744)]
VGG16 predicted: [('n02802426', 'basketball', 0.9940745), ('n04540053', 'volleyball', 0.005732499), ('n04509417', 'unicycle', 7.97446e-05)]
InceptionV3 predicted: [('n03047690', 'clog', 0.9857115), ('n03950228', 'pitcher', 0.0142774815), ('n04131690', 'saltshaker', 9.02714e-06)]
Xception predicted: [('n03942813', 'ping-pong_ball', 0.9943867), ('n02115641', 'dingo', 0.004939552), ('n03908618', 'pencil_box', 0.00034586503)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.3186262), ('n02088466', 'bloodhound', 0.082444966), ('n04355933', 'sunglass', 0.05579455)]
DenseNet201 predicted: [('n02793495', 'barn', 0.9854887), ('n07749582', 'lemon', 0.014435244), ('n03028079', 'church', 6.973953e-05)]
###### 6
ResNet50 predicted: [('n04540053', 'volleyball', 0.8996359), ('n02802426', 'basketball', 0.04612564), ('n04371774', 'swing', 0.012817903)]
VGG16 predicted: [('n04540053', 'volleyball', 0.6531843), ('n04371774', 'swing', 0.23126662), ('n03535780', 'horizontal_bar', 0.034345746)]
InceptionV3 predicted: [('n03047690', 'clog', 0.9999999), ('n03950228', 'pitcher', 9.813132e-08), ('n01924916', 'flatworm', 4.521091e-10)]
Xception predicted: [('n03942813', 'ping-pong_ball', 0.60112345), ('n03814906', 'necklace', 0.39777786), ('n04252077', 'snowmobile', 0.00032584247)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.029858764), ('n02088466', 'bloodhound', 0.02951363), ('n04485082', 'tripod', 0.022113921)]
DenseNet201 predicted: [('n03000134', 'chainlink_fence', 0.48486677), ('n02708093', 'analog_clock', 0.32410663), ('n03376595', 'folding_chair', 0.19036537)]

##### Ambulance
###### 1
ResNet50 predicted: [('n02701002', 'ambulance', 0.9023919), ('n04461696', 'tow_truck', 0.0294733), ('n03977966', 'police_van', 0.021965053)]
VGG16 predicted: [('n02701002', 'ambulance', 0.4083945), ('n03977966', 'police_van', 0.2949969), ('n04461696', 'tow_truck', 0.053885125)]
InceptionV3 predicted: [('n03047690', 'clog', 1.0), ('n04328186', 'stopwatch', 1.8690795e-08), ('n06359193', 'web_site', 2.784462e-09)]
Xception predicted: [('n03942813', 'ping-pong_ball', 0.9419214), ('n03814906', 'necklace', 0.029491788), ('n03908618', 'pencil_box', 0.017980991)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.46787825), ('n02088466', 'bloodhound', 0.21542), ('n02091467', 'Norwegian_elkhound', 0.143386)]
DenseNet201 predicted: [('n07749582', 'lemon', 0.99999213), ('n02999410', 'chain', 7.4544314e-06), ('n02793495', 'barn', 1.6168075e-07)]
###### 2
ResNet50 predicted: [('n02701002', 'ambulance', 0.46511868), ('n03977966', 'police_van', 0.25769225), ('n03769881', 'minibus', 0.0889469)]
VGG16 predicted: [('n02701002', 'ambulance', 0.3737117), ('n03977966', 'police_van', 0.14939825), ('n03417042', 'garbage_truck', 0.1443568)]
InceptionV3 predicted: [('n03047690', 'clog', 0.99998474), ('n04131690', 'saltshaker', 1.3204322e-05), ('n03950228', 'pitcher', 1.6769044e-06)]
Xception predicted: [('n03942813', 'ping-pong_ball', 0.56114984), ('n02834397', 'bib', 0.109829195), ('n03908618', 'pencil_box', 0.10499943)]
NASNet predicted: [('n02088466', 'bloodhound', 0.2772598), ('n03124043', 'cowboy_boot', 0.12695707), ('n02091467', 'Norwegian_elkhound', 0.12179861)]
DenseNet201 predicted: [('n03461385', 'grocery_store', 0.8231287), ('n07930864', 'cup', 0.12886451), ('n02708093', 'analog_clock', 0.020663535)]
###### 3
ResNet50 predicted: [('n02701002', 'ambulance', 0.6219452), ('n03977966', 'police_van', 0.3215937), ('n03345487', 'fire_engine', 0.030971887)]
VGG16 predicted: [('n02701002', 'ambulance', 0.9238655), ('n03345487', 'fire_engine', 0.04552923), ('n03977966', 'police_van', 0.028357662)]
InceptionV3 predicted: [('n06359193', 'web_site', 0.7931255), ('n03950228', 'pitcher', 0.11051113), ('n04131690', 'saltshaker', 0.023964755)]
Xception predicted: [('n03942813', 'ping-pong_ball', 0.99546635), ('n02115641', 'dingo', 0.0022743475), ('n03763968', 'military_uniform', 0.0019677507)]
NASNet predicted: [('n04485082', 'tripod', 0.039206345), ('n06359193', 'web_site', 0.030299608), ('n04355933', 'sunglass', 0.029724644)]
DenseNet201 predicted: [('n04070727', 'refrigerator', 0.6728562), ('n02793495', 'barn', 0.2966685), ('n03028079', 'church', 0.023523789)]
###### 4
ResNet50 predicted: [('n02701002', 'ambulance', 0.99813557), ('n03796401', 'moving_van', 0.0008506309), ('n03977966', 'police_van', 0.00043357108)]
VGG16 predicted: [('n02701002', 'ambulance', 0.9940684), ('n03977966', 'police_van', 0.0039964733), ('n04461696', 'tow_truck', 0.00072213216)]
InceptionV3 predicted: [('n06359193', 'web_site', 1.0), ('n03047690', 'clog', 3.5896813e-10), ('n04328186', 'stopwatch', 1.5043e-10)]
Xception predicted: [('n02769748', 'backpack', 0.80116206), ('n03763968', 'military_uniform', 0.07493816), ('n03814906', 'necklace', 0.048754726)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.416076), ('n02091467', 'Norwegian_elkhound', 0.26721004), ('n02088466', 'bloodhound', 0.25287554)]
DenseNet201 predicted: [('n04228054', 'ski', 0.47635096), ('n04252225', 'snowplow', 0.19225626), ('n02747177', 'ashcan', 0.1666024)]
###### 5
ResNet50 predicted: [('n02701002', 'ambulance', 0.99981195), ('n03977966', 'police_van', 0.00017906545), ('n03769881', 'minibus', 6.6827656e-06)]
VGG16 predicted: [('n02701002', 'ambulance', 0.99007857), ('n03977966', 'police_van', 0.009206017), ('n03769881', 'minibus', 0.00036291557)]
InceptionV3 predicted: [('n01924916', 'flatworm', 0.90429205), ('n04328186', 'stopwatch', 0.0884966), ('n06359193', 'web_site', 0.007210903)]
Xception predicted: [('n03814906', 'necklace', 0.5231212), ('n03942813', 'ping-pong_ball', 0.3941848), ('n03763968', 'military_uniform', 0.05956933)]
NASNet predicted: [('n02088466', 'bloodhound', 0.50515044), ('n03124043', 'cowboy_boot', 0.2218216), ('n02091467', 'Norwegian_elkhound', 0.14407417)]
DenseNet201 predicted: [('n04070727', 'refrigerator', 0.5758057), ('n04228054', 'ski', 0.2931922), ('n04252225', 'snowplow', 0.050716083)]
###### 6
ResNet50 predicted: [('n03345487', 'fire_engine', 0.85024595), ('n02701002', 'ambulance', 0.14929105), ('n04461696', 'tow_truck', 0.00015809873)]
VGG16 predicted: [('n02701002', 'ambulance', 0.73974013), ('n03345487', 'fire_engine', 0.2514555), ('n04461696', 'tow_truck', 0.0036873615)]
InceptionV3 predicted: [('n01924916', 'flatworm', 0.9999999), ('n06359193', 'web_site', 1.617474e-07), ('n04328186', 'stopwatch', 1.2174682e-15)]
Xception predicted: [('n03942813', 'ping-pong_ball', 0.98986965), ('n03814906', 'necklace', 0.009814051), ('n06359193', 'web_site', 0.00015705064)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.33327568), ('n02088466', 'bloodhound', 0.26737398), ('n02091467', 'Norwegian_elkhound', 0.096084505)]
DenseNet201 predicted: [('n04228054', 'ski', 0.6567715), ('n04252077', 'snowmobile', 0.34170216), ('n04252225', 'snowplow', 0.0015263325)]

##### Husky
###### 1
ResNet50 predicted: [('n02115641', 'dingo', 0.42247918), ('n02110185', 'Siberian_husky', 0.3253942), ('n02110063', 'malamute', 0.08098954)]
VGG16 predicted: [('n02125311', 'cougar', 0.22707765), ('n02114367', 'timber_wolf', 0.17557177), ('n04005630', 'prison', 0.06996081)]
InceptionV3 predicted: [('n03950228', 'pitcher', 0.795881), ('n01740131', 'night_snake', 0.1985909), ('n03908714', 'pencil_sharpener', 0.0043411623)]
Xception predicted: [('n03942813', 'ping-pong_ball', 0.70045185), ('n02769748', 'backpack', 0.12110683), ('n02115641', 'dingo', 0.10072391)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.15897505), ('n04355933', 'sunglass', 0.12641616), ('n02088466', 'bloodhound', 0.057817128)]
DenseNet201 predicted: [('n03461385', 'grocery_store', 0.64547426), ('n02793495', 'barn', 0.21271358), ('n07930864', 'cup', 0.077840604)]
###### 2
ResNet50 predicted: [('n02110185', 'Siberian_husky', 0.84273833), ('n02109961', 'Eskimo_dog', 0.15567638), ('n02110063', 'malamute', 0.00038753316)]
VGG16 predicted: [('n02110185', 'Siberian_husky', 0.8292041), ('n02109961', 'Eskimo_dog', 0.1698575), ('n02091244', 'Ibizan_hound', 0.000580459)]
InceptionV3 predicted: [('n03676483', 'lipstick', 0.99728394), ('n03047690', 'clog', 0.0026477028), ('n01924916', 'flatworm', 6.8408895e-05)]
Xception predicted: [('n02834397', 'bib', 0.77864796), ('n03942813', 'ping-pong_ball', 0.22027968), ('n03445777', 'golf_ball', 0.00087420136)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.311461), ('n02091467', 'Norwegian_elkhound', 0.22175801), ('n02088466', 'bloodhound', 0.2019226)]
DenseNet201 predicted: [('n04485082', 'tripod', 0.9946949), ('n04507155', 'umbrella', 0.0026107298), ('n02793495', 'barn', 0.0022494653)]
###### 3
ResNet50 predicted: [('n02114548', 'white_wolf', 0.541486), ('n02109961', 'Eskimo_dog', 0.27252305), ('n02110185', 'Siberian_husky', 0.1438061)]
VGG16 predicted: [('n02109961', 'Eskimo_dog', 0.53026956), ('n02114548', 'white_wolf', 0.24152276), ('n02110185', 'Siberian_husky', 0.1975985)]
InceptionV3 predicted: [('n06359193', 'web_site', 1.0), ('n15075141', 'toilet_tissue', 0.0), ('n02319095', 'sea_urchin', 0.0)]
Xception predicted: [('n02834397', 'bib', 0.94640183), ('n02105056', 'groenendael', 0.048018403), ('n02027492', 'red-backed_sandpiper', 0.0033640212)]
NASNet predicted: [('n02091467', 'Norwegian_elkhound', 0.46487135), ('n03124043', 'cowboy_boot', 0.28027937), ('n02088466', 'bloodhound', 0.15380205)]
DenseNet201 predicted: [('n07749582', 'lemon', 0.93843937), ('n03028079', 'church', 0.058377348), ('n02793495', 'barn', 0.0026381966)]
###### 4
ResNet50 predicted: [('n02109961', 'Eskimo_dog', 0.7887978), ('n02110185', 'Siberian_husky', 0.16694796), ('n02110063', 'malamute', 0.020697044)]
VGG16 predicted: [('n02109961', 'Eskimo_dog', 0.7428311), ('n02110185', 'Siberian_husky', 0.19549456), ('n02114548', 'white_wolf', 0.028780777)]
InceptionV3 predicted: [('n06359193', 'web_site', 1.0), ('n04328186', 'stopwatch', 1.2404323e-11), ('n02442845', 'mink', 5.353201e-18)]
Xception predicted: [('n03445777', 'golf_ball', 0.5777558), ('n03942813', 'ping-pong_ball', 0.39015147), ('n03775546', 'mixing_bowl', 0.028972903)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.5356465), ('n04355933', 'sunglass', 0.23235968), ('n02088466', 'bloodhound', 0.0438344)]
DenseNet201 predicted: [('n02747177', 'ashcan', 0.9667262), ('n04252225', 'snowplow', 0.009271335), ('n04485082', 'tripod', 0.008806801)]
###### 5
ResNet50 predicted: [('n02109961', 'Eskimo_dog', 0.4565128), ('n02110185', 'Siberian_husky', 0.23219422), ('n03218198', 'dogsled', 0.13822861)]
VGG16 predicted: [('n02111129', 'Leonberg', 0.15757975), ('n03404251', 'fur_coat', 0.12462826), ('n02127052', 'lynx', 0.10873495)]
InceptionV3 predicted: [('n06359193', 'web_site', 0.9999999), ('n03481172', 'hammer', 1.1673939e-07), ('n04325704', 'stole', 1.0225782e-08)]
Xception predicted: [('n03942813', 'ping-pong_ball', 0.6085538), ('n03763968', 'military_uniform', 0.16924897), ('n03814906', 'necklace', 0.15967025)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.40630338), ('n02088466', 'bloodhound', 0.213956), ('n02091467', 'Norwegian_elkhound', 0.08338199)]
DenseNet201 predicted: [('n02793495', 'barn', 0.7639804), ('n03028079', 'church', 0.22887981), ('n04485082', 'tripod', 0.005609066)]
###### 6
ResNet50 predicted: [('n03218198', 'dogsled', 0.96880585), ('n02109961', 'Eskimo_dog', 0.024096528), ('n02110185', 'Siberian_husky', 0.003144277)]
VGG16 predicted: [('n03218198', 'dogsled', 0.597226), ('n02109961', 'Eskimo_dog', 0.19621012), ('n02110185', 'Siberian_husky', 0.116015844)]
InceptionV3 predicted: [('n01924916', 'flatworm', 0.94631594), ('n06359193', 'web_site', 0.053683206), ('n04355933', 'sunglass', 8.8070243e-07)]
Xception predicted: [('n03814906', 'necklace', 0.35517055), ('n02112350', 'keeshond', 0.35449645), ('n03763968', 'military_uniform', 0.14650032)]
NASNet predicted: [('n03124043', 'cowboy_boot', 0.7288257), ('n02088466', 'bloodhound', 0.13657787), ('n02091467', 'Norwegian_elkhound', 0.083469756)]
DenseNet201 predicted: [('n02793495', 'barn', 0.9988311), ('n04485082', 'tripod', 0.0010800828), ('n03873416', 'paddle', 5.1296985e-05)]

### Exercise
- Utilizem 3 redes prontas e treinadas do Keras para classificar imagens da ImageNet e verificar qual a melhor...

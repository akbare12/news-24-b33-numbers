import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png')
SB='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'; SN='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; SNB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(s,b=False,ser=False):
    try: return ImageFont.truetype((SB if ser else SNB) if (b or ser) else SN, s)
    except Exception: return ImageFont.load_default()
def wrap(d,t,f,mw):
    words=t.split(); lines=[]; cur=''
    for w in words:
        x=(cur+' '+w).strip()
        if d.textlength(x,font=f)<=mw: cur=x
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def para(d,x,y,t,f,mw,fill, leading=None):
    lh=(leading or int(f.size*1.18))
    for ln in wrap(d,t,f,mw): d.text((x,y),ln,font=f,fill=fill); y+=lh
    return y
def chip(d,x,y,t,c):
    f=F(8,True); w=int(d.textlength(t,font=f))+10; d.rounded_rectangle([x,y,x+w,y+14],3,fill=c); d.text((x+5,y+2),t,font=f,fill='white'); return x+w+4
def scene(d,b,k):
    x0,y0,x1,y1=b; d.rectangle(b,fill='#dfe9f2'); d.rectangle([x0,y1-18,x1,y1],fill='#2f4a3a')
    if y1-y0<50:
        d.rectangle([x0,y1-8,x1,y1],fill='#2f4a3a')
        if k=='tower': d.rectangle([x0+85,y0+4,x0+105,y1-8],fill='#1c2f4a'); d.ellipse([x0+150,y0+4,x0+170,y0+24],fill='#e4572e')
        elif k=='chart': d.line([(x0+10,y1-10),(x0+80,y1-16),(x0+150,y1-22),(x0+190,y1-28)],fill='#1c7a3a',width=3)
        elif k=='rocket': d.rectangle([x0+90,y0+2,x0+102,y1-8],fill='#e8e0cc'); d.polygon([(x0+90,y0+2),(x0+96,y0-2),(x0+102,y0+2)],fill='#8c2f2f')
        elif k=='ship': d.rectangle([x0+40,y0+10,x0+160,y0+22],fill='#33506e'); d.rectangle([x0+15,y0+22,x1-15,y1-8],fill='#7fb3d5')
        elif k=='trophy': d.ellipse([x0+85,y0+2,x0+110,y0+27],fill='#f2b04d')
        elif k=='drone': d.rectangle([x0+70,y0+12,x0+125,y0+24],fill='#1c2f4a'); d.ellipse([x0+30,y0+6,x0+55,y0+18],fill='#333333'); d.ellipse([x0+140,y0+6,x0+165,y0+18],fill='#333333')
        elif k=='data': d.rectangle([x0+20,y0+4,x0+175,y0+26],fill='#1c2f4a'); d.text((x0+28,y0+8),'CODE RED',font=F(12,True),fill='#ff5a4d')
        elif k=='heli': d.ellipse([x0+70,y0+8,x0+130,y0+26],fill='#5c6b4a'); d.rectangle([x0+40,y0+12,x0+155,y0+16],fill='#333333')
        else: d.rectangle([x0+20,y0+6,x0+90,y1-8],fill='#33506e'); d.text((x0+100,y0+8),'NEWS',font=F(11,True,True),fill='#1c2f4a')
        return
    if k=='tower':
        d.rectangle([x0+20,y0+8,x1-20,y0+30],fill='#f2b04d'); d.rectangle([x0+105,y0+30,x0+125,y1-18],fill='#1c2f4a'); d.rectangle([x0+135,y0+55,x0+165,y1-18],fill='#33506e'); d.rectangle([x0+175,y0+70,x0+205,y1-18],fill='#1c2f4a')
        for yy in range(38,y1-y0-24,10):
            for xx in (112,142,182): d.rectangle([x0+xx,y0+yy,x0+xx+6,y0+yy+6],fill='#ffd97a')
        d.ellipse([x0+230,y0+12,x0+258,y0+40],fill='#e4572e'); d.polygon([(x0+240,y0+55),(x0+255,y0+70),(x0+225,y0+70)],fill='#333333'); d.ellipse([x0+250,y0+75,x0+270,y0+95],fill='#f2b04d'); d.ellipse([x0+255,y0+80,x0+265,y0+90],fill='#e4572e')
    elif k=='court':
        d.rectangle([x0+90,y0+45,x0+230,y1-18],fill='#e8e0cc'); d.polygon([(x0+80,y0+45),(x0+160,y0+15),(x0+240,y0+45)],fill='#8c2f2f'); d.rectangle([x0+105,y0+55,x0+120,y1-18],fill='#fff8e6'); d.rectangle([x0+200,y0+55,x0+215,y1-18],fill='#fff8e6'); d.rectangle([x0+130,y0+62,x0+190,y0+72],fill='#1c2f4a'); d.text((x0+138,y0+52),'HUAWEI',font=F(11,True),fill='white')
    elif k=='party':
        d.rectangle([x0+60,y0+40,x0+260,y1-18],fill='#8c2f2f'); d.rectangle([x0+130,y0+60,x0+190,y1-18],fill='#5c1a1a'); d.polygon([(x0+110,y0+40),(x0+160,y0+18),(x0+210,y0+40)],fill='#f2b04d'); d.rectangle([x0+20,y0+55,x0+110,y0+88],fill='#e8e0cc'); d.text((x0+26,y0+58),'FILE',font=F(10,True),fill='#8c2f2f'); d.text((x0+26,y0+72),'UNDER',font=F(10,True),fill='#333333')
    elif k=='chart':
        d.rectangle([x0+15,y0+55,x0+290,y0+58],fill='#8c2f2f'); d.line([(x0+15,y0+85),(x0+80,y0+80),(x0+150,y0+70),(x0+220,y0+45),(x0+295,y0+25)],fill='#1c7a3a',width=4); d.polygon([(x0+15,y0+85),(x0+80,y0+80),(x0+150,y0+70),(x0+220,y0+45),(x0+295,y0+25),(x0+295,y1-18),(x0+15,y1-18)],fill='#bfe3c6'); d.text((x0+18,y0+12),'50,018',font=F(20,True,True),fill='#1c2f4a')
    elif k=='rocket':
        d.rectangle([x0+140,y0+20,x0+170,y1-40],fill='#e8e0cc'); d.polygon([(x0+140,y0+20),(x0+155,y0+2),(x0+170,y0+20)],fill='#8c2f2f'); d.text((x0+142,y0+45),'CZ-2F',font=F(9,True),fill='#8c2f2f'); d.ellipse([x0+230,y0+15,x0+285,y0+70],fill='#f2b04d'); d.polygon([(x0+150,y1-40),(x0+140,y1-18),(x0+160,y1-18)],fill='#f2b04d'); d.polygon([(x0+160,y1-40),(x0+170,y1-18),(x0+150,y1-18)],fill='#e4572e')
    elif k=='ship':
        d.rectangle([x0+40,y0+60,x0+280,y0+95],fill='#33506e'); d.rectangle([x0+70,y0+35,x0+250,y0+60],fill='#e4572e'); d.rectangle([x0+90,y0+45,x0+110,y0+60],fill='#fff8e6'); d.rectangle([x0+130,y0+45,x0+150,y0+60],fill='#fff8e6'); d.rectangle([x0+170,y0+45,x0+190,y0+60],fill='#fff8e6'); d.rectangle([x0+15,y0+95,x1-15,y1-18],fill='#7fb3d5')
    elif k=='trophy':
        d.ellipse([x0+120,y0+15,x0+190,y0+75],fill='#f2b04d'); d.rectangle([x0+145,y0+75,x0+165,y0+95],fill='#c98a1b'); d.rectangle([x0+120,y0+95,x0+190,y1-18],fill='#8c6a1b'); d.ellipse([x0+105,y0+25,x0+125,y0+55],outline='#c98a1b',width=4); d.ellipse([x0+185,y0+25,x0+205,y0+55],outline='#c98a1b',width=4)
    elif k=='drone':
        d.ellipse([x0+20,y0+10,x0+60,y0+35],fill='#333333'); d.ellipse([x0+250,y0+10,x0+290,y0+35],fill='#333333'); d.rectangle([x0+110,y0+55,x0+200,y0+85],fill='#1c2f4a'); d.rectangle([x0+40,y0+70,x0+110,y0+75],fill='#333333'); d.rectangle([x0+200,y0+70,x0+270,y0+75],fill='#333333'); d.text((x0+130,y0+60),'96',font=F(14,True),fill='white')
    elif k=='data':
        d.rectangle([x0+30,y0+30,x0+280,y0+90],fill='#1c2f4a'); d.text((x0+40,y0+40),'CODE RED',font=F(18,True),fill='#ff5a4d'); d.text((x0+40,y0+65),'24-HOUR OUTAGE',font=F(11,True),fill='white'); d.rectangle([x0+30,y0+95,x0+120,y1-18],fill='#33506e'); d.rectangle([x0+130,y0+95,x0+220,y1-18],fill='#e4572e')
    elif k=='heli':
        d.ellipse([x0+90,y0+45,x0+220,y0+85],fill='#5c6b4a'); d.rectangle([x0+40,y0+55,x0+95,y0+65],fill='#5c6b4a'); d.rectangle([x0+60,y0+38,x0+260,y0+44],fill='#333333'); d.polygon([(x0+220,y0+60),(x0+280,y0+50),(x0+280,y0+75),(x0+220,y0+70)],fill='#5c6b4a')
    else:
        d.rectangle([x0+25,y0+25,x0+125,y1-18],fill='#33506e'); d.rectangle([x0+140,y0+40,x0+285,y1-18],fill='#e8e0cc'); d.text((x0+150,y0+50),'NEWS',font=F(16,True,True),fill='#1c2f4a'); d.text((x0+150,y0+72),'24 NOV',font=F(11,True),fill='#8c2f2f')
NA=[(-168,66),(-155,71),(-140,70),(-128,70),(-120,71),(-110,68),(-95,69),(-85,66),(-82,60),(-76,62),(-70,58),(-65,60),(-60,52),(-55,47),(-60,45),(-65,44),(-70,42),(-74,40),(-76,35),(-80,32),(-81,26),(-84,30),(-89,30),(-91,29),(-94,29),(-97,26),(-97,16),(-94,16),(-92,15),(-86,13),(-83,9),(-80,8),(-77,4),(-80,7),(-85,11),(-90,14),(-95,16),(-105,20),(-110,23),(-114,28),(-117,33),(-122,37),(-124,42),(-124,48),(-130,55),(-140,60),(-150,61),(-158,58),(-165,60),(-168,66)]
SA=[(-80,8),(-77,4),(-75,-5),(-80,-6),(-81,-12),(-77,-15),(-72,-18),(-70,-23),(-70,-30),(-71,-35),(-73,-40),(-73,-50),(-68,-55),(-65,-55),(-68,-50),(-65,-45),(-62,-41),(-58,-38),(-52,-33),(-48,-28),(-41,-23),(-39,-17),(-35,-9),(-35,-6),(-40,-3),(-44,-2),(-50,0),(-53,4),(-58,6),(-62,9),(-68,11),(-72,12),(-76,10),(-80,8)]
AF=[(-6,35),(-10,31),(-15,27),(-17,21),(-17,15),(-15,11),(-12,8),(-8,5),(-4,5),(0,6),(6,4),(9,4),(9,0),(12,-5),(13,-10),(12,-17),(14,-22),(16,-28),(19,-34),(26,-34),(32,-29),(35,-24),(36,-18),(40,-15),(40,-10),(42,-4),(44,0),(48,2),(51,11),(48,11),(44,12),(40,15),(38,18),(37,22),(35,28),(34,28),(32,31),(30,32),(25,32),(20,32),(15,32),(11,34),(10,37),(5,37),(0,36),(-6,35)]
EU=[(-10,36),(-9,43),(-2,48),(0,50),(-4,52),(2,51),(5,53),(8,57),(10,59),(18,56),(21,55),(24,59),(28,60),(30,62),(35,65),(45,68),(55,69),(65,72),(75,73),(85,75),(95,76),(105,78),(115,76),(125,73),(135,72),(145,72),(155,70),(162,66),(170,66),(178,65),(178,62),(170,60),(162,60),(158,53),(150,59),(142,55),(140,50),(138,46),(135,43),(132,43),(128,38),(127,35),(122,38),(120,32),(122,28),(118,25),(110,20),(108,18),(105,10),(103,8),(100,6),(98,10),(94,16),(92,21),(90,22),(86,20),(80,13),(77,8),(74,20),(70,23),(66,25),(62,25),(58,26),(56,27),(52,28),(50,30),(48,30),(44,29),(42,18),(40,15),(38,20),(35,28),(34,31),(36,36),(30,36),(27,37),(23,36),(19,40),(15,44),(12,44),(8,44),(3,43),(0,40),(-2,37),(-6,36),(-9,37),(-10,36)]
AU=[(113,-22),(114,-30),(115,-35),(122,-34),(129,-32),(134,-33),(137,-35),(140,-38),(147,-39),(150,-37),(153,-27),(146,-19),(142,-11),(136,-12),(132,-12),(126,-14),(122,-17),(118,-20),(113,-22)]
JP=[(130,31),(132,33),(135,34),(138,35),(140,38),(141,42),(143,44),(141,45),(140,40),(139,37),(136,36),(133,35),(130,33)]
UK=[(-5,50),(-3,53),(-5,56),(-3,58),(-1,57),(0,53),(1,51),(-3,50)]
HEROES=[('1 RIYADH · MIDDLE EAST','Houthi drone hits Riyadh\'s tallest tower again, 11 hurt','A Houthi drone struck the PIF tower, Riyadh\'s tallest, for the second time in a week, injuring 11 people.','CONFIRMED','#1c7a3a','tower','Saudi officials · AP'),('2 SHANGHAI · ASIA','China probes Shanghai party chief Chen Jining','Chen Jining, 62, is probed for serious violations, the fourth Politburo member to fall this year.','OFFICIAL','#1c4f8c','party','CCDI · Reuters'),('3 NEW YORK · US/TECH','Huawei guilty on 10 of 12 counts','A US jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud.','CONFIRMED','#1c7a3a','court','US court · AP')]
CARDS=[('4 ZAPORIZHZHIA · EUROPE/WAR','Russian attacks kill 9 across Ukraine in a day','Russia killed 9 in Ukraine in a day and launched 96 drones; 73 were shot down.','REPORTED','#5a6b7d','drone','Kyiv officials'),('5 CAS · AFRICA/SPORT','CAS hands Senegal back the AFCON title','CAS restored Senegal as champions; Morocco forfeited 3-0, so Senegal won 1-0.','OFFICIAL','#1c4f8c','trophy','CAS'),('6 HORMUZ · MIDDLE EAST','IRGC attacks container ship in Hormuz','The IRGC attacked a container ship in Hormuz and cut its navigation.','REPORTED','#5a6b7d','ship','UKMTO · wires'),('7 NEW YORK · WORLD/MARKETS','Dow closes above 50,000 for the first time','The Dow closed at 50,018, its first close above 50,000, while the Taiex set a record.','CONFIRMED','#1c7a3a','chart','Market close'),('8 REDMOND · WORLD/TECH','Microsoft declares \'Code Red\' after historic outage','Microsoft declared Code Red after a 24-hour outage, the worst in Exchange history.','REPORTED','#5a6b7d','data','Reuters'),('9 ESKISEHIR · EUROPE','Turkish military helicopter crash kills 5','A Turkish military AS-532 helicopter crashed in Eskisehir, killing all 5 on board.','REPORTED','#5a6b7d','heli','Turkish officials'),('10 CARTAGENA · AMERICAS','Supermarket hostages: 25 held in Cartagena','Gunmen held 25 hostages in a Cartagena supermarket; 5 elderly women were freed.','REPORTED','#5a6b7d','news','Colombian officials'),('11 ADEN · MIDDLE EAST','Houthis advance within 60 km of Aden','Houthi forces advanced to within 60 km of Aden, Yemen, in their latest push south.','REPORTED','#5a6b7d','news','Wires'),('12 LAHJ · MIDDLE EAST','Saudi strikes kill 25, wound 6 in Yemen','Saudi strikes on a bus and truck in Wadi Maabaq, Lahj, killed or left missing 25 people.','REPORTED','#5a6b7d','news','Yemeni officials'),('13 JIUQUAN · WORLD/SPACE','China names first foreign astronaut for Tiangong','China named Tang Hongbo, Wu Yi and Zeeshan Ali for Shenzhou-24.','OFFICIAL','#1c4f8c','rocket','CMSA')]
ALSO=['14 Ankara: Haftar visits Turkey for the first time.','15 London: UK sanctions Houthis and 4 officials.','16 Villavicencio: Car bomb injures 23 people.','17 Gaza: Israel kills Hamas internal security chief.','18 Baghdad: Iraq orders federal control of Kurdish oilfields.','19 Gaza: Meningitis epidemic alert, 272 cases in October.','20 DR Congo: Missing Cessna 208, rebels claim shootdown.','21 Hanoi: Hot-pot explosion kills at least 6 people.','22 Gulf of Finland: Ukraine hits Russian ship Sparta II.','23 Kuala Lumpur: Malaysia to return migrants to Myanmar.','24 Ulleungdo: S. Korea shelter order as Russian jets enter ADIZ.','25 Dhaka: Hasina plans return on 16 December.','26 The Hague: 14 nations endorse ICJ Myanmar ruling.','27 Jakarta: Indonesia nominates 2 VP candidates.','28 Beijing: China sentences official Ma to death for spying.','29 Brussels: NATO vows defence against space threat.','30 Mexico City: US drone aided El Chapo capture; Mexico to try him.','31 San Salvador: Bukele names 3 soldiers killed in Haiti.','32 Ottawa: Pentagon rebukes Canada; only 41.9% of air fleet ready.','33 Washington: US adds Megaspeed to trade blacklist.','34 Kyiv: Zelensky urges Ukraine/Russia/US/Europe talks soon.','35 Ras Al Khaimah: UAE bus-truck crash kills 13 people.','36 London: England record 5,258 heat deaths, summer 2026.','37 Kourou: Ariane 6 lofts 36 Amazon satellites.','38 Cikande: Factory-fire toll rises to 26 people.']
NUMBERS=[('11','hurt in Riyadh'),('9','killed in Ukraine'),('50,018','Dow close'),('+8.99%','Taiex record'),('25','killed/missing, Yemen'),('26','Cikande toll'),('10/12','Huawei guilty'),('96','drones at Ukraine')]
UTC=[('02:15','NATO vows space defence'),('08:16','Hanoi blast'),('10:42','Saudi strikes Yemen'),('14:27','Riyadh tower hit'),('16:51','Houthis 60 km from Aden'),('18:58','Hormuz ship attack'),('20:41','Huawei guilty')]
PINS=[(1,24.71,46.68),(2,31.23,121.47),(3,40.71,-74.01),(4,47.84,35.14),(5,14.72,-17.47),(6,26.50,56.30),(7,40.71,-74.01),(8,47.67,-122.12),(9,39.78,30.52),(10,10.39,-75.51),(11,12.80,45.03),(12,13.05,44.88),(13,39.77,98.50)]
OFF={3:(0,-16),7:(0,16),11:(-18,10),12:(18,-10),6:(0,-14),2:(0,-14)}
img=Image.new('RGB',(W,H),'#f7f2e7'); d=ImageDraw.Draw(img)
d.text((14,10),'THE WORLD ON ONE DAY',font=F(11,True),fill='#8c2f2f'); d.text((1024-14-d.textlength('38 STORIES · 6 REGIONS · 13 FIELDS',font=F(11,True)),10),'38 STORIES · 6 REGIONS · 13 FIELDS',font=F(11,True),fill='#1c2f4a'); d.line([14,28,1010,28],fill='#8c2f2f',width=2)
d.text((14,34),'Tuesday 24 November 2026',font=F(34,True,True),fill='#111111'); d.text((14,72),'Riyadh tower hit again · Shanghai party chief probed · Huawei guilty on 10 of 12 counts',font=F(12,False,True),fill='#8c2f2f')
REG=[('Europe',9,'#1c4f8c'),('Middle East',8,'#8c2f2f'),('Asia',8,'#c98a1b'),('Africa',2,'#1c7a3a'),('Americas',7,'#5a3a7d'),('World/Space',4,'#333333')]; x=14; d.rectangle([14,94,1010,112],fill='#e8e0cc')
for nm,n,c in REG:
    t=f'{nm} {n}'; w=int(d.textlength(t,font=F(10,True)))+16; d.rectangle([x,94,x+w,112],fill=c); d.text((x+8,97),t,font=F(10,True),fill='white'); x+=w+4
d.text((14,118),'THE DAY IN NUMBERS',font=F(10,True),fill='#8c2f2f')
for i,(v,lb) in enumerate(NUMBERS):
    xx=14+i*125; d.rectangle([xx,132,xx+118,168],outline='#1c2f4a',width=1); d.text((xx+6,136),v,font=F(17,True,True),fill='#1c2f4a'); d.text((xx+6,156),lb,font=F(8),fill='#333333')
d.text((14,174),'THE DAY IN UTC',font=F(10,True),fill='#8c2f2f'); xx=14
for tm,ev in UTC:
    t=f'{tm} {ev}'; w=int(d.textlength(t,font=F(9,True)))+8; d.text((xx,186),t,font=F(9,True),fill='#1c2f4a'); xx+=w+6
d.line([14,202,1010,202],fill='#1c2f4a',width=1)
for i,(kick,head,deck,ch,col,kind,src) in enumerate(HEROES):
    x0=14+i*332; x1=x0+324; scene(d,(x0,206,x1,296),kind); d.text((x0,300),kick,font=F(9,True),fill='#8c2f2f'); cx=chip(d,x0,314,ch,col); d.text((cx,315),src,font=F(8),fill='#555555'); y=para(d,x0,330,head,F(13,True,True),318,'#111111',16); para(d,x0,y+2,deck,F(10),318,'#333333',13)
d.line([14,404,1010,404],fill='#1c2f4a',width=1)
for i,(kick,head,deck,ch,col,kind,src) in enumerate(CARDS):
    r,c=i//5,i%5; x0=14+c*200; y0=410+r*112; x1=x0+192; scene(d,(x0,y0,x1,y0+34),kind); d.text((x0,y0+37),kick,font=F(7,True),fill='#8c2f2f'); cx=chip(d,x0,y0+49,ch,col); d.text((cx,y0+50),src,font=F(7),fill='#555555'); y=para(d,x0,y0+64,head,F(9,True),192,'#111111',11); para(d,x0,y+1,deck,F(8),192,'#333333',10)
d.line([14,636,1010,636],fill='#1c2f4a',width=1); d.text((14,642),'THE WORLD · 13 PLACES PINNED',font=F(10,True),fill='#8c2f2f')
MX,MY,MW,MH=14,660,620,200
def proj(lat,lon): return (MX+(lon+180)/360*MW, MY+(85-lat)/140*MH)
d.rectangle([MX,MY,MX+MW,MY+MH],fill='#cfe0ee',outline='#1c2f4a')
for poly in (NA,SA,AF,EU,AU,JP,UK):
    pts=[proj(la,lo) for lo,la in poly]; d.polygon(pts,fill='#8aa86b',outline='#33502a')
d.text((MX+8,MY+6),'ATLANTIC',font=F(8),fill='#33506e'); d.text((MX+430,MY+6),'PACIFIC',font=F(8),fill='#33506e'); d.text((MX+250,MY+150),'INDIAN OCEAN',font=F(8),fill='#33506e')
for n,la,lo in PINS:
    px,py=proj(la,lo); dx,dy=OFF.get(n,(0,-14)); lx,ly=px+dx,py+dy
    if (dx,dy)!=(0,-14) and (dx,dy)!=(0,0): d.line([px,py,lx,ly],fill='#8c2f2f',width=1)
    d.ellipse([lx-9,ly-9,lx+9,ly+9],fill='#8c2f2f',outline='white',width=1); d.text((lx-3 if n<10 else lx-6,ly-6),str(n),font=F(8,True),fill='white')
LX=650; d.text((LX,660),'LEGEND · 1-13',font=F(10,True),fill='#1c2f4a')
LEG=[('1 Riyadh — PIF tower hit','#8c2f2f'),('2 Shanghai — Chen Jining probed','#c98a1b'),('3 New York — Huawei 10/12','#1c4f8c'),('4 Zaporizhzhia — 9 killed','#1c4f8c'),('5 Dakar — Senegal AFCON title','#1c7a3a'),('6 Hormuz — ship attacked','#8c2f2f'),('7 New York — Dow 50,018','#1c4f8c'),('8 Redmond — Microsoft Code Red','#5a3a7d'),('9 Eskisehir — helicopter, 5 killed','#1c4f8c'),('10 Cartagena — 25 hostages','#5a3a7d'),('11 Aden — Houthis 60 km away','#8c2f2f'),('12 Lahj — 25 killed','#8c2f2f'),('13 Jiuquan — Shenzhou-24 crew','#333333')]
for i,(t,c) in enumerate(LEG): d.rectangle([LX,678+i*14,LX+10,688+i*14],fill=c); d.text((LX+14,677+i*14),t,font=F(9),fill='#111111')
d.text((14,866),'ALSO ON TUESDAY 24 NOVEMBER — 25 MORE STORIES',font=F(10,True),fill='#8c2f2f')
COLS=[ALSO[0:9],ALSO[9:17],ALSO[17:25]]
for ci,col in enumerate(COLS):
    y=880; xx=14+ci*332
    for t in col: y=para(d,xx,y,t,F(8),324,'#111111',9)
d.rectangle([14,962,1010,1010],outline='#8c2f2f',width=2); d.text((20,966),'DATE CHECK',font=F(10,True),fill='#8c2f2f')
yy=para(d,20,978,'Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.',F(8),984,'#111111',10)
yy=para(d,20,yy,'LEFT OUT (not 24 Nov): Hormuz mine claims (23 Nov) · Huang returns as Nvidia CEO (23 Nov) · EU sanctions 22 (23 Nov) · COP31 no deal (22 Nov) · Merkury sunk (22 Nov) · El Chapo arrested (Fri 20 Nov) · Cikande fire started (Sat 21 Nov).',F(8),984,'#111111',10)
para(d,20,yy,'NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) · MPR session to pick VP (11 Dec) · Huawei sentencing (Sep 2027) · Hasina returns to Bangladesh (16 Dec).',F(8),984,'#111111',10)
d.text((14,1014),'Sources: wires · AP · Reuters · UKMTO · CAS · CMSA · CCDI · US court. CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side. Scenes are drawn illustrations, not photographs.',font=F(7),fill='#555555')
os.makedirs(os.path.dirname(OUT) or '.',exist_ok=True); img.save(OUT,format='PNG',optimize=True); print(OUT,img.size,os.path.getsize(OUT))

from guizero import *
import serial
import sys
import glob

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(32)] # Hız için 256'dan 32'e düşürüldü.
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    #print(ports)
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

sayac = 0
sure = 0
ser = None  #Global tanımlanmalı
role_acik = False 
#* Olaylar
def port_tarama():
    com_combo.clear()
    options = serial_ports()
    for x in options:
        com_combo.append(x)
    if(options==[]):
        app.error("Hata!", "Port Bulunamadı. Bağlantıyı Gözden Geçirin.")

def baglan():
    com_deger = com_combo.value
    baud_deger =baud_combo.value
    global ser
    ser = serial.Serial(com_deger, baud_deger, timeout=0, parity=serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS, rtscts=0)
    empty_label2.value="Bağlandı..."
def role1ac():
    ser.write('1'.encode('Ascii'))
    role1_kapa.enabled = True 
    role1_ac.enabled = False 
def role1kapa():
    ser.write('2'.encode('Ascii'))
    role1_kapa.enabled = False 
    role1_ac.enabled = True 
def role2ac():
    ser.write('3'.encode('Ascii'))
    role2_kapa.enabled = True 
    role2_ac.enabled = False 
def role2kapa():
    ser.write('4'.encode('Ascii'))
    role2_kapa.enabled = False 
    role2_ac.enabled = True 
def role3ac():
    ser.write('5'.encode('Ascii'))
    role3_kapa.enabled = True  
    role3_ac.enabled = False
def role3kapa():
    ser.write('6'.encode('Ascii'))
    role3_kapa.enabled = False  
    role3_ac.enabled = True 
def role4ac():
    ser.write('7'.encode('Ascii'))
    role4_kapa.enabled = True  
    role4_ac.enabled = False  
def role4kapa(): 
    ser.write('8'.encode('Ascii'))
    role4_kapa.enabled = False
    role4_ac.enabled = True 
def ayarlar():
    pencere_2.show()
def ayarlari_kaydet():
    role1_ac.text = role_1_textbox.value + " AÇ"
    role1_kapa.text = role_1_textbox.value + " KAPA"  
    role2_ac.text = role_2_textbox.value + " AÇ"  
    role2_kapa.text = role_2_textbox.value + " KAPA"
    role3_ac.text = role_3_textbox.value + " AÇ"
    role3_kapa.text = role_3_textbox.value + " KAPA"
    role4_ac.text = role_4_textbox.value + " AÇ"
    role4_kapa.text = role_4_textbox.value + " KAPA"
    pencere_2.hide()

def zamanlama():
    pencere_3.show()
    cihaz_combo.clear()
    cihaz_combo.append(role_1_textbox.value)
    cihaz_combo.append(role_2_textbox.value)
    cihaz_combo.append(role_3_textbox.value)
    cihaz_combo.append(role_4_textbox.value)

def zamanlama_baslat():
    global sure
    global sayac
    global role_acik
    cihaz = cihaz_combo.value
    if (cihaz == role_1_textbox.value):
        role1ac()
    elif(cihaz == role_2_textbox.value):
        role2ac()
    elif(cihaz == role_3_textbox.value):
        role3ac()
    elif(cihaz == role_3_textbox.value):
        role4ac()
    #sure = sayac + (int(float(zaman_dakika.value)) * 60) + int(float(zaman_saniye.value))
    dakika = int(zaman_dakika.value)
    saniye = int(zaman_saniye.value)
    sure = (((dakika * 60) + saniye) * 1000) + sayac
    role_acik = True 
def say():
    global sayac
    global sure 
    global role_acik
    sayac += 1
    if(sayac > sure and role_acik == True):
        role_acik == False
        cihaz = cihaz_combo.value
        if (cihaz == role_1_textbox.value):
            role1kapa()
        elif(cihaz == role_2_textbox.value):
            role2kapa()
        elif(cihaz == role_3_textbox.value):
            role3kapa()
        elif(cihaz == role_3_textbox.value):
            role4kapa()
#** Olaylar


app = App(title="Python Röle Kontrol", layout="grid", width="420", height="400")
#*Yeni Ayar Penceresi 
pencere_2 = Window(app, title="Ayarlar", width="250", height="400", layout="grid")
pencere_2.hide()
pencere_2_yazi = Text(pencere_2, text="Ayarlar", grid=[0,0], align="left")
pencere_2_yazi_bos = Text(pencere_2, text=" ", grid=[1,1])
role_1_ad_label = Text(pencere_2, text="Röle 1 Ad:", grid=[0,2])
role_1_textbox = TextBox(pencere_2, text="RÖLE 1", width=30, grid=[1,2], align="left")
role_2_ad_label = Text(pencere_2, text="Röle 2 Ad:", grid=[0,3])
role_2_textbox = TextBox(pencere_2, text="RÖLE 2", width=30, grid=[1,3])
role_3_ad_label = Text(pencere_2, text="Röle 3 Ad", grid=[0,4])
role_3_textbox = TextBox(pencere_2, text="RÖLE 3", width=30, grid=[1,4])
role_4_ad_label = Text(pencere_2, text="Röle 4 Ad", grid=[0,5])
role_4_textbox = TextBox(pencere_2, text="RÖLE 4", width=30, grid=[1,5])
kayit_button = PushButton(pencere_2, command=ayarlari_kaydet, text="Kaydet", grid=[0,6])
#* Zamanlama Penceresi 
pencere_3 = Window(app, title="Zamanlama", width="380", height="300",layout="grid")
pencere3_text = Text(pencere_3, text="Zamanlama Süresini ve Cihazı Seçiniz...", grid=[1,0])
cihaz_label = Text(pencere_3, text="Cihaz:", grid=[0,1], align="left")
cihaz_combo = Combo(pencere_3, align="left", options = [role_1_textbox.value, role_2_textbox.value, role_3_textbox.value, role_4_textbox.value], grid=[1,1])
dakika_label = Text(pencere_3, "Dakika:", grid=[0,3])
zaman_dakika = TextBox(pencere_3, text="0", width=10, grid=[1,3])
saniye_label = Text(pencere_3, text="Saniye:", grid=[0,4])
zaman_saniye = TextBox(pencere_3,text="0", width=10, grid=[1,4])
zamanlama_baslat_dugme = PushButton(pencere_3, command=zamanlama_baslat, text="Başlat", grid=[0,5])

pencere_3.hide()
#* Tasarım 
giris_yazisi = Text(app, text="Python Röle Kontrol v.2", grid=[1, 0], align="left")
giris_yazisi.repeat(1, say)
empty_label = Text(app, text=" ", grid=[0,1])
com_label = Text(app, text="Port:", grid=[0,2])
com_combo = Combo(app, options = ["PORT SEÇİNİZ"], grid =[1,2])
com_combo.when_clicked = port_tarama 
baud_label = Text(app, text="Baud Seçiniz:", grid=[0,3])
baud_combo = Combo(app, options = ["110","300","600","1200", "2400", "4800", "9600", "14400", "19200", "38400", "57600", "115200", "128000", "256000"], grid=[1,3])
baud_combo.value = "9600"  # Varsayılan 9600 bps olarak ayarlandı
empty_label2 = Text(app, text=" ", grid=[0,4])
ayarlar_button = PushButton(app, command=ayarlar, text="Ayarlar", grid=[0,5])
zamanlama_button = PushButton(app, command=zamanlama, text="Zamanlama", grid=[1,5])
baglan_button = PushButton(app, command=baglan, text="Bağlan", grid=[2,5])
## Bağlantı Tasarımı Bitti.
bilgi_etiketi = Text(app, text=" ", grid=[0,6])
role1_ac = PushButton(app, command=role1ac, width=20 , text="Röle 1 AÇ", grid=[0,7])
role1_kapa = PushButton(app, command=role1kapa, width=20,text="Röle 1 KAPA", grid=[1,7], enabled=False)
role2_ac = PushButton(app, command=role2ac, width=20, text="Röle 2 AÇ", grid=[0,8])
role2_kapa = PushButton(app, command=role2kapa, width=20, text="Röle 2 KAPA", grid=[1,8], enabled=False )
role3_ac = PushButton(app, command=role3ac, width=20, text="Röle 3 AÇ", grid=[0,9])
role3_kapa = PushButton(app, command=role3kapa, width=20, text="Röle 3 KAPA", grid=[1,9], enabled=False)
role4_ac = PushButton(app, command=role4ac, width=20, text="Röle 4 AÇ", grid=[0,10])
role4_kapa = PushButton(app, command=role4kapa, width=20, text="Röle 4 KAPA", grid=[1,10], enabled=False)
#** Tasarım
app.display()
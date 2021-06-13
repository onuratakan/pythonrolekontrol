# pythonrolekontrol
AVR mikrodenetleyici kartı üzerinden guizero kullanılarak yapılmış olan röle kontrol yazılımı

Yazılım portları otomatik taramakta, port bulunmazsa hata mesajı vermektedir. Dört ayrı röle bağımsız olarak açılıp kapatılabilir. Rölenin açık olup olmadığı kullanıcıya düğmelerin etkin/devredışı olmasıyla bildirilmekte ve aynı zamanda kazara basmanın önüne geçmektedir. 

Ayarlar penceresinden her röle isimlendirilmekte bu isimler düğmelere ve zamanlayıcıya yansımaktadır. 

Zamanlayıcıda bir röle istenilen dakika ve saniye değeri girilerek belirtilen süre boyunca açık konumda olur. Geçen süre her milisaniyede güncellenmektedir. 

Röleler Arduino kartının D4, D5, D6, D7 ayaklarına bağlanmalıdır. Mikrodenetleyici yazılımı Atmel Studio'da AVR-GCC üzerinde yazılmıştır. 

# 3.2 Analyse

[Home](../README.md)

## Aufgabe 1
### Begründen Sie die öffentliche Erreichbarkeit/Nichterreichbarkeit der Systeme
<br></br>
***Firewall-System*** öffentlich erreichbar: **Nein**, weil ein externer Zugriff auf die Firewall zu einer Sicherheitslücke führt, durch die Einstellungen an der Firewall vorgenommen werden können. Somit würden Externe Zugriff auf das Netzwerk erhalten.

***DNS*** öffentlich erreichbar: **Nein**, da interne DNS-Server erfordern keine Authentifizierung. Somit kann meist jeder, der sich im Netzwerk befindet, interne DNS-Anfragen tätigen. Diese DNS-Server speichern alle Servernamen und IP-Adressen für private Domains, welche durch Angreifer ausgespäht und verfälscht werden könnten. 

***DHCP*** öffentlich erreichbar: **Nein**, da durch externe Angriffe sonst keine Clients mehr in das Netzwerk eingebunden werden können. Ebenso könnten IP-Adressen ausgespäht und letztendlich geändert werden.

***Web-Server*** öffentlich erreichbar: **Ja**, da dieser aus dem Internet mithilfe von HTTPS über Port 443 aufrufbar sein sollte, damit Mandaten darauf zugreifen und Tickets erstellen können.

***Datenbank-Server*** öffentlich erreichbar: **Nein**, da dieser sensible Daten wie Anmeldedaten der Website-Nutzer enthält, welche geschützt werden müssen.

***[Pi-Hole]*** öffentlich erreichbar: **Nein**, da Angreifer somit Einstellungen tätigen können. Hierbei kann es sich um Änderungen von gefilterten Webseiten handeln, um die internen Nutzer auf diese weiterzuleiten. Darüber hinaus werden DNS-Anfragen von der Software Pi-Hole gespeichert und dient somit als eigener DNS-Server, welcher ohne starke Absicherung nicht öffentlich erreichbar gemacht werden sollte.

***[Mailproxy für eingehende Mails]*** öffentlich erreichbar: **Ja**, da sonst keine Mails in das interne Netzwerk weitergeleitet werden können.

***[Existierender Mailserver]*** öffentlich erreichbar: Nein, da eingehende Mails vom Mailproxy an diesen weitergeleitet und anschließend verteilt werden. Wenn der Mailserver von extern erreichbar wäre, könnte dieser mit Schadmail belagert und darüber hinaus auch die Datenpakete ausspioniert werden.
<br></br>
## Aufgabe 2

### Beschreiben Sie die Akteure und den jeweiligen Kommunikationsweg über die Zwischensysteme zu den IT-Endsystemen für folgenden Anwendungsfälle:
<br></br>
***a)	Ticket erstellen und in DB speichern***
Der Kunde greift vom Host-Rechner mit Hilfe eines Browsers auf den Web-Server zu, welcher aus dem Internet abrufbar ist und erstellt ein Ticket. Dabei läuft die Kommunikation über die IP-Adresse des Gateways des VMNet8, passiert die Firewall des IP-Fires, wird über das Gateway in das VMnet2. Die Daten des Tickets werden auf den Datenbank-Server übertragen und eingepflegt. Hierzu muss aus dem VMNet2 auf das VMNet1 über die Firewall des IPFires zugegriffen werden. 
Der Kunde kann jedoch auch telefonisch Kontakt mit dem Kundenservice herstellen. Der Mitarbeiter erzeugt anschließend über das interne VMNet1 auf den Webserver im VMNet2 ein Ticket, welches wieder in die Datenbank, welche im VMNet1 liegt, eingepflegt wird.

***b)	Administration von FW, DNS- und DHCP-Server***
Die Administration der Dienste erfolgt aus dem internen VMNet1-Netz durch einen Mitarbeiter mit administrativen Rechten. Ausgehend vom Administrator-Rechner kann eine ssh-Verbindung mit dem DNS- und DHCP-Server im Netz hergestellt werden, sofern der Port 22 auf dem Server geöffnet ist. Die Firewall kann über die Weboberfläche des IPFire vom Administrator-Rechner aus konfiguriert werden. Hierzu werden die IP-Adresse und der Port :444 im Browser eingegeben.

***c)	Administration des Web-Servers***
Für die Konfiguration des Web-Servers wird aus dem VMNet1 auf den Web-Server im VMNet2 über die Firewall des IPFires und des Web-Servers zugegriffen. Hierzu wird durch einen Administrator eine ssh-Verbindung hergestellt. Zu beachten ist, dass die Installationen eine Internetverbindung benötigen, welche über den Kinder- und Jugendschutzproxy läuft.

***d)	Datenbankabfragen zur Supportsteuerung (z.B. Anzahl offener Tickets)***
Die Datenbankabfragen können vom Administrator über eine ssh-Verbindung auf dem Datenbankserver getätigt werden, sofern der Port 22 des Datenbankservers geöffnet ist. 

***e)	[PI-Hole]*** 
Das PI-Hole wird als Werbeblocker eingesetzt. Somit wird aus dem internen VMNet1 eine Anfrage über die Firewall des IPFire und das VMNet8 ins Internet getätigt und somit eine Webseite aufgerufen. Der Kommunikationsweg läuft wie bei einer gewöhnlichen DNS-Anfrage.

***f)	[Mailkommunikation]*** 
Die Mailkommunikation erfolgt via Client-Server-Prinzip. Der Client schickt seine Mail an den SMTP-Server (entweder im eigenen Subnetz, oder über ein Gateway an ein anderes Subnetz). Der Server kommuniziert mit dem DNS-Server, um den Empfänger der Mail zu ermitteln. Anschließend leitet der DNS-Server die Informationen an den SMTP-Server zurück, welcher letztendlich die Nachricht an den Empfänger übermittelt. 

# Dokumentation Heimnetz

## Aufgaben

+ [ ] Netze rot, grün, orange entsprechen eigenen Vorgaben
  + [ ] IP
  + [ ] Verbindung Host
  + [ ] Verfügbarkeit der Dienste
+ [ ] IPFire, Server und Adminrechner folgen eigenen Vorgaben
+ [ ] IPFire aufgesetzt, Ping möglich
+ [ ] DNS von IPFire funktioniert entsprechend Vorgabe
+ [ ] DNS Server im Intranet aufgesetzt und konfiguriert
+ [ ] DNS löst ei Test auf Adminrechner lokale und globale Namen auf
+ [ ] Interner DHCP Server im Intranet aufgesetzt und konfiguriert
+ [ ] Web-Server aufgesetzt und konfiguriert
+ [ ] Webserver mit Firefox des Hosts aufrufbar mittels IP (http)
---
**Zusatz**
+ [ ] Zugriff auf Webserver über Hostname statt IP ist möglich
+ [ ] Proxyeinstellung auf IPFire erlauben https Zugriffe von IPFire ins Internet

## Virtualisierungsumgebung
+ Hyper-V
+ Erstellung von 3 Switches
  + extern = VMnet8 (mit Zugang zum WLAN-Adapter)
  + intern1 = VMnet1
  + intern2 = VMnet2

## Installationen

### IP-Fire
+ Hostname: srv01ipfire
+ Hinzufügen der drei Switche
+ "sicherer Start" deaktivieren
+ Installation wie gewohnt
  + Hinzufügen der MAC-Adressen der Switche 
    + VMnet8 - 00:15:5D:B2:14:07
    + VMnet1 - 00:15:5D:B2:14:09
    + VMnet2 - 00:15:5D:B2:14:08
  + Vergabe IP-Adressen
    + VMnet8 = 192.168.178.3
    + VMnet1 = 192.168.13.3
    + VMnet2 = 192.168.113.3

### DNS + DHCP
+ Hostname: srv02dc
+ Hinzufügen Switch intern 1 für VMnet1
+ "sicherer Start" deaktivieren
+ Betriebssystem: CentOS 9
+ Konfiguration static IP-Adresse:

```
nmcli device
nmcli connection modify eth0 ipv4.addresses 192.168.13.20/24
nmcli connection modify eth0 ipv4.gateway 192.168.13.3
nmcli connection modify eth0 ipv4.method manual
```

+ Installation `dnsmasq`

```
yum -y install dnsmasq
systemctl start dnsmasq
systemctl enable dnsmasq
systemctl status dnsmasq
```
![dnsmasq_run](images/dnsmasq_run.png)

### Bearbeitung der /etc/dnsmasq.conf
```
        cp /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
        nano /etc/dnsmasq.conf

listen-address=127.0.0.1,192.168.13.20
interface=eth0
expand-hosts (soll Clients in die /etc/hosts aufnehmen)
domain=Doubtful-Joy13.de
server=8.8.8.8
server=8.8.4.4
address=/Doubtful-Joy13.de/127.0.0.1
address=/Doubtful-Joy13.de/192.168.13.20

        dnsmasq -test
        nano /etc/resolv.con

nameserver 127.0.0.1
```
+ die `resolv.conf` wird vom lokalen deamon verwaltet (u. a. NetworkManager), welcher Änderungen überschreibt
+ daher wird sie schreibgeschützt

```
chattr + i /etc/resolv.conf
lsattr /etc/resolv.conf
```
+ die `/etc/hosts` bearbeiten, um dnsmasq-controller und gateway einzutragen

```
nano /etc/hosts
        127.0.0.1		dnsmasq
        192.168.13.20	dnsmasq
        192.168.13.3	gateway
```
+ Testen der lokalen Domäne `Doubtful-Joy13.de`

![domaintest](images/domaintest.png)

![domaintestreverse](images/domaintestreverse.png)

``Bemerkung: ipfire wurde umbenannt von "gateway" in "ipfire"``

### Einrichtung DHCP
+ Bearbeitung der `/etc/dnsmasq.conf`

```
dhcp-range=192.168.13.50,192.168.13.150,12h
dhcp-leasefile=/var/lib/dnsmasq/dnsmasq.leases
dhcp-option=3,192.168.13.3
dhcp-option=option:dns-server,192.168.13.20
dhcp-option=option:netmask,255.255.255.0
#dhcp-authoritative
```

## Installation Administrator-Rechner
+ Hostname: cl01admin
+ Hinzufügen Switch intern 1 für VMnet1
+ "sicherer Start" deaktivieren
+ Betriebssystem: CentOS 9 -> diesmal als Client-Rechner
+ gewohnte Installation
+ LAN-Einstellungen > IPv4-Methode > Automatisch DHCP
  + Rechner erhält nun über aufgesetzten DHCP-Server seine IP-Adresse, die Subnetzmaske und das Gateway

![cl01admin_ifconfig1](images/cl01admin_ifconfig1.png)

## Installation Datenbank-Server
+ Hostname: srv03db
+ Hinzufügen Switch intern 1 für VMnet1
+ "sicherer Start" deaktivieren
+ Betriebssystem: CentOS 9 -> Server
+ gewohnte Installation
+ da der Server die Daten vom Webserver erhalten soll, benötigt er eine statische IP vom DHCP

```
srv02dc$ nano /etc/dnsmasq.conf
dhcp-host=00:15:5d:b2:14:0e,srv03db,192.168.13.22
```

![srv03db_ifconfig1](images/srv03db_ifconfig1.png)

+ Auflösung von DNS-Anfragen funktionieren -> geprüft mit `ping google.de`

![srv03db_ping1](images/srv03db_ping1.png)

### Installation MariaDB

```
yum install mariadb-server
systemctl enable mariadb
systemctl start mariadb
mysql_secure_installation
  Enter
  Yes
  No
  Yes
  Yes
  Yes
  Yes
mysql -u root -p
  CREATE DATABASE tickets;
  CREATE user dbadmin;
  GRANT ALL ON tickets.* TO dbadmin@localhost IDENTIFIED BY '12345';
  exit;
```

## Installation Webserver
+ Hostname: srv04web
+ Hinzufügen Switch intern2 für VMnet2
+ "sicherer Start" deaktivieren

### Installation http (apache)

``` 
yum install httpd
systemctl start httpd
systemctl enable httpd
```

### Überprüfung der Verbindungen // Firewall-Regeln
+ ping an srv01ipfire von allen Maschinen möglich
+ ping zwischen den Maschinen im Grünen Netz möglich
+ ping von srv04web ins Grüne Netz nicht möglich -> muss auch nicht möglich sein
+ ping aus dem Grünen Netz zu srv04web -> funktioniert
+ Zugriff auf srv04web über ssh vom cl01admin-Rechner aus -> funktioniert

![srv04web_ssh](images/srv04web_ssh.png)

## Anmerkungen
+ Switch extern muss von WLAN-Adapter auf Ethernet umgestellt werden
+ Schulproxy muss eingetragen werden, sofern IPFire nicht als UpstreamProxy konfiguriert
+ IP-Adresse des VMnet8 auf dem IPFire ändern
+ dnsmasq.service failed, wenn der Server heruntergefahren wurde; muss beim Starten der VMs neu gestartet werden `systemctl restart dnsmasq.service`

### Netzwerkplan
+ Domain-Name überarbeiten in Doubtful-Joy13.de
+ Benutzername und Passwort
+ Software Webserver: Apache2, php 7
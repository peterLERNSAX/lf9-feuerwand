# Soll-Ist-Vergleich 

[Home](../README.md)

| Soll | Ist |
|------------------------------------------------------------------------------|-----------------------------------------------|
|Doubtful-Joy fordert eine Segmentierung der Netzinfrastruktur mit einer sicheren Trennung von öffentlich erreichbaren Diensten und dem Intranet.<br> | Es erfolgte eine Trennung in DMZ und Intranet. Die DMZ enthält den online zur Verfügung gestellten Webserver. Im Intranet sind alle unternehmensinternen Server und Client-Geräte |
Die netzwerkrelevanten internen Dienste DNS und DHCP sind auf einem separaten System bereitzustellen um Abhängigkeiten von der Firewall auszuschließen. <br> | DNS und DHCP wurden auf einem Server im Intranet aufgesetzt und verteilen Konfigurationen an Geräte im Intranet, sowie bieten die Möglichkeit zur Namensauflösung |
Doubtful-Joy setzt im Bereich der Server ausschließlich RedHat und binärkompatible Systeme ein. Alle OS-Installationen der Server folgen dieser System-Strategie. <br> | Alle Geräte wurden mit CentOS 9 installiert.  | 
Auf Grundlage des dynamischen Wachstums erwartet Doubtful-Joy eine begründete Empfehlung <br>
a) zur technischen Bereitstellung der IT-Infrastruktur | Upgrades sind jederzeit möglich (Hardware/Software), Upgrades sind schneller realisierbar (sofort) 
b) zum zukunftssicheren Systembetrieb der Lösung im Kontext von „make or buy“. | Die Wartung der Server ist einfacher und günstiger, da Fachkräfte vor Ort zur Verfügung stehen;  |


# Ergebnis und Zeitaufwand

+ alle Anforderungen wurden erfüllt
+ Zeitaufwand war per se nicht sehr hoch (3-4h für die Installation und Konfiguration aller VMs (Teil1) noch einmal 2h für den zweiten Teil) 
+ als endgültige Lösung für ein Unternehmen, würden jedoch noch einige Installationen und Konfigurationen fehlen 

# Optimierungen
+ Domain Controller (entweder Windows AD-Server, oder freeipa (linuxbasiert)) für die zentrale Authentifizierung und Autorisierung, sowie Freigabe von Ordnern für berechtigte Personen (Berechtigungskonzept)
+ auf dem IPFire sollte nicht nur Destination Natting, sondern auch Source Natting betrieben werden 
    + Source Natting damit die eigentliche Server-Adresse des Webservers den Nutzern nicht bekannt gemacht wird -> Es wird dann so angezeigt, dass die Firewall selbst den Dienst zur Verfügung stellt
+ regelmäßiges Datenbankbackup für den Datenbankserver, welches jedoch auf einem zusätzlichen Server gelagert wird
+ einen Mailserver, welcher zusätzlich abgesichert werden kann
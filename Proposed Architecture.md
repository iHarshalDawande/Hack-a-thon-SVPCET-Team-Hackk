# II. PROPOSED ARCHITECTURE

A. NFC Tags Utilization for Secure Medical Object Identification It is important to reduce errors in the
hospital workflow using Reliable medical object identifiers, such as giving correct medicine to a
patient. We propose architecture of an application for issuing secure identifiers to reduce the error
Fig.1: Architecture of NFC based mobile healthcare system and also to prevent security attacks like
modification, repudiation and masquerading. The secure NFC passive tags have been used for
identifiers, specifically MIFARE Classic. Bluetooth Low Energy (BTLE) stickers have lately been used to
identify objects. But since they require a dedicated battery to operate, NFC passive tags are cheaper
for identifiers to be used in healthcare. Hence basic NFC-A interface can be used to access
smartcards from a mobile device. A valid mobile reader must have security key KR for read access
and a valid writer must have security key KW for update access. The tag is issued by a healthcare
We have proposed an architecture for NFC based secure health care as illustrated in Fig. 1 for i)
secure medical identifiers as in flow steps 1.1 to 1.5 and ii) Health card retaining EHR using Android
mobile devices as in flow steps 2.1 to 2.5.
We have proposed a secure healthcare service like Health Secure on a hybrid cloud to which all
hospitals can subscribe. The Health Secure hybrid cloud provides service for maintaining
Cryptographic servers for secure framework and Storage server to provide backup as well as space
for extended EHR. MobileADMIN is a mobile device of an authorized medical admin. “Mobile-P” is the
patient's mobile device with the Health card and “Mobile-D” is the doctor's mobile device. Since a
larger screen would be better suited to view and update the health records, MobileDoc could either
be an NFC enabled tablet, for portability, or a laptop with external smartcard reader. KA and KB are
the read and write access keys respectively for a secure tag based on MIFARE Classic. For NFC P2P
based and card emulation based Health cards, we use patient's and doctor's set of public and
private keys, which are KpUBPAT, KpRlPAT and KpUBDOC, KpRJDOC respectively. A symmetrical
shared key KSH is used for encrypting data. Hospital administration has an application for securely
reading/writing with a mobile device, MobileADMIN, to manage smartcard based tags and patient
Health Cards. MobileADMIN can register with the proposed HealthSecure cloud service on a hybrid
cloud, which can issue security keys for our architecture. The mobiles use SE and simple interfaces of
NFC and Bluetooth for credential storage and communication. We discuss the architecture of the
applications briefly and the details of the implementation in ‘section iv’ admin mobile device, MobileADMIN, which has registered to a HealthSecure service.
It retains security keys in its SE for issuing tags. To enhance security, the access keys of the tag could be
updated on a periodic basis for retaining secure IDs on the medical objects showing the workflow of
secure tag identifiers in bold. Along with medical identification records, information related to
timestamp can also be updated.

B. NFC Tags in e-Health Cards The secure tags used for application in III-A, are used for a different
application for storing EHR on the Health Card of a patient. This is similar to a smartcard based
Health Card. But here we suggest smartcards that can be securely and easily accessed using mobile
devices. The tag could retain patient identification information along with emergency information,
insurance information and health records. The tag could be organized into different sections, each
administered separately by different set of security access keys. Similar to the secure tag application,
this card can be issued and updated by an authorized health admin mobile device MobileADMIN. A
patient can register at the MobileADMIN and then later show to an authorized doctor with
MobileDOC in an OPD which would have the required access keys KR and KW for reading and
updating the health records respectively. All NFC information can be retained with a timestamp.
Detailed health records can be retained on a storage server of the HealthSecure service on hybrid
cloud. At the end of the visit the patient can present the tag back to the administrator to tap and
store his visit detail on the hybrid cloud. At any point of time if patients‘ past records are required,
they can be retrieved over a secure wireless interface (like HTTPS) from the hybrid cloud, using the
patient ID on the tag. This application will help the patient to retain the recent health records on a
cheap yet secure tag equivalent to a smartcard.

C. e-Health Card based on P2P NFC mode This application architecture is based on retaining a Health
Card on a mobile device using NFC P2P mode. The EHR is retained on the mobile device in a secure
region instead of the NFC tag as in III-B. The patient can tap his mobile device onto the doctor's
mobile device to exchange his records using NFC NDEF format. The doctor can read and update the
records and tap them back onto the patient's mobile device. Both patient and doctor register for the
OPD session with the health admin, MobileADMIN, to get secure keys. The patient's public and
private keys are KpUBPAT, KpRJPAT and doctor's public and private keys KpUBDOC, KpRIDoc get
stored on the SE of their respective mobile devices for the OPD session, This Health Card offers
more storage space as compared to what a smartcard based tag can provide as in application. It also
ensures that only the permitted records of the patient are accessed by an authorized doctor, thus
retaining security and privacy of the patient. NFC P2P mode can be utilized for information
exchange, But very large health records exchanged over NFC can be slow due to the low data rate of
NFC. Bluetooth can be used along with NFC for exchange of larger information.

D. e-Health Card based on NFC card emulation In this application architecture, Healthcard is retained on a mobile
device using card emulation and Java card applets installed on the SE. We propose usage of a SE in
the form of an SWP enabled microSD card which can be issued to the patient by HealthSecure
service. Java Card applet can be used to authenticate and authorize the reader to access and update
the health records using NFC SWP protocol. Since the SE has limited space, it can only retain part of
the health records. The remaining health records can be retained outside the SE region on the SD
card in a secure manner. The Card on the MobilePAT can be accessed externally by a PC/SC reader
that is attached to MobileDOC. Since the SE has limited space, an extended card consisting of past
records and other health information, like images and documents.

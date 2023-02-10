# III. Implementation

Applications can be developed for both Android devices using Android APIs, and administrative
servers, using PHP and MySQL, for secure, reliable and robust healthcare systems. Implementation
of the Security framework and hybrid cloud service is in progress and will be tested and deployed in
the field in our future work. The healthcare data can be large in size as in a Health card with the
entire EHR in section. Also the health card could be accessed by various persons: patient, medical
professional, emergency person and insurance. The patient should be able to securely manage the
access control of the EHR. There is a requirement of confidentiality, integrity, mutual authentication,
access control of EHR, privacy threats leading to identity thefts and insurance security breach. The
security framework involves various entities. A cryptographic server can be used to generate, verify
and store security keys. An administrator bot will be present to issue and authenticate Health Cards
/ tags and register patients/doctors. Mobile devices used by doctors are equipped with a Doctor App
and a secure element. A Health Card used by patients can be called a Patient card which in this case
is using a NFC P2P or card emulation mode. Since the health card could be accessed by various
persons: patient, medical professional and emergency person. There could be a separate Doctor PIN
for the doctor and a super key for the emergency team when the patient is unconscious.
The security flow consists of
1. Health Card personalization.
2. Mutual Authentication between the patient and the medical doctor to assure the correct patient is
appearing before an authorized doctor and there is no relay attack.
3. Access control for data viewable by the doctor.
4. Secure health card retrieval and updation.
There is an initial phase of personalization in which the Patient Card and the Doctor get a unique
identification ID (UIDpat and UIDdoc) and a set of public and private keys (KpUBPAT, KpRlPAT and
KpUBOOC, KpRIDoc) which are stored locally in the security server based on the respective card ID
and/or secure element ID. An encrypted and signed data communications ensures confidentiality
and integrity.

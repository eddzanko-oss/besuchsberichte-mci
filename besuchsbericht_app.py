import streamlit as st
import json
import os
from datetime import date, datetime, timedelta
import uuid

DATA_FILE = "besuchsberichte.json"
UPLOADS_DIR = "uploads"
os.makedirs(UPLOADS_DIR, exist_ok=True)

KUNDEN_DB = {
  "Karl Schmidt GmbH": {
    "strasse": "Großharbach 3+5",
    "plz": "91587",
    "ort": "Adelshofen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Haustechnik",
    "region": "Bayern",
    "prioritaet": "A"
  },
  "ESD Einrichtungs-Systeme GmbH": {
    "strasse": "Werkstraße 5",
    "plz": "90518",
    "ort": "Altdorf",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Architekt",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Firma  Incotec GmbH + Co. KG z.Hd. Herrn Blaufelder": {
    "strasse": "Wacholderweg 3",
    "plz": "90518",
    "ort": "Altdorf",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Bayern",
    "prioritaet": "C"
  },
  "TM Ausbau GmbH Regionalbüro Franken": {
    "strasse": "Feuerweg 22",
    "plz": "90518",
    "ort": "Altdorf",
    "email": "info@tm-ausbau.eu",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "GU",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Lex GmbH": {
    "strasse": "Bahnhofstraße 29",
    "plz": "94424",
    "ort": "Arnstorf",
    "email": "",
    "telefon": "+49 8723 20 36 76",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "INTEK Funktionsraum Gmbh": {
    "strasse": "Untere Hofmark 27",
    "plz": "94424",
    "ort": "Arnstorf/Mariakirchen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Von Guttenberg GmbH": {
    "strasse": "Uhlandstr. 13 - 15",
    "plz": "85609",
    "ort": "Aschheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Lurz GmbH": {
    "strasse": "Max-Eyth-Str. 20",
    "plz": "97980",
    "ort": "Bad Mergentheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Haustechnik",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Max Wild GmbH": {
    "strasse": "Leutkircher Straße 22",
    "plz": "88450",
    "ort": "Berkheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Techno Color": {
    "strasse": "Brunfeldstrasse 7",
    "plz": "94327",
    "ort": "Bogen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Elektro Kreutzpointner GmbH": {
    "strasse": "Burgkirchener Straße 3",
    "plz": "84489",
    "ort": "Burghausen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Caverion Deutschland GmbH": {
    "strasse": "Gstocketwiesenstraße 9",
    "plz": "94469",
    "ort": "Deggendorf",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "ENGIE Deutschland GmbH Geschäftsbereich Building Services Standort Deggendorf": {
    "strasse": "Hafenstr. 28",
    "plz": "94469",
    "ort": "Deggendorf",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Fa. Syscotec; Frau Hageneder": {
    "strasse": "Gewerbegebiet Mitterhof 26",
    "plz": "84307",
    "ort": "Eggenfelden",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Syscotec GmbH  z.Hd. Frau  Hageneder": {
    "strasse": "Gewerbegebiet Mitterhof 26",
    "plz": "84307",
    "ort": "Eggenfelden",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "MPM Micro Präzision Marx GmbH & Co. KG": {
    "strasse": "Neuenweiherstraße 19",
    "plz": "91056",
    "ort": "Erlangen",
    "email": "info@mpmgmbh.de",
    "telefon": "+49-9131/9056-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "FEISTL Lüftungs- und Klimatechnik GmbH & Co. KG": {
    "strasse": "Liebigstraße 1",
    "plz": "84051",
    "ort": "Essenbach",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Zeppelin GmbH zu Hdn. Frau Anett Tempel": {
    "strasse": "Graf-Zeppelin-Platz 1",
    "plz": "85748",
    "ort": "Garching bei München",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Stelzig GmbH": {
    "strasse": "Von-Linde-Str. 2",
    "plz": "82205",
    "ort": "Gilching",
    "email": "info@stelzig.de",
    "telefon": "+ 49 (8105) 77 36 00",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "B&S Belch mit System GmbH & Co KG": {
    "strasse": "Josef-Buchinger-Straße 12",
    "plz": "94481",
    "ort": "Grafenau",
    "email": "info@blechmitsystem.de",
    "telefon": "+49 8552 97433-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Pfau GmbH Meisterbetrieb": {
    "strasse": "Kapfweg 1",
    "plz": "88178",
    "ort": "Heimenkirch",
    "email": "info@pfau-meisterbetrieb.de",
    "telefon": "+49 83 87 92 36 29",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Fa. Probat; Herr Jan Zylstra": {
    "strasse": "Eriagstrasse 60",
    "plz": "85053",
    "ort": "Ingolstadt",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "IM-Bau Montagen": {
    "strasse": "Laboratoriumstrasse 1",
    "plz": "85055",
    "ort": "Ingolstadt",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Kaufmann GmbH & Co.": {
    "strasse": "Siemensstrasse 9",
    "plz": "88353",
    "ort": "Kisslegg",
    "email": "info@stuckateur-kaufmann.de",
    "telefon": "+49 7563 913075-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Lichtwerk GmbH": {
    "strasse": "Hellinger Straße 3",
    "plz": "97486",
    "ort": "Königsberg",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Konrad Knoblauch": {
    "strasse": "Zeppelinstraße 8-12",
    "plz": "88677",
    "ort": "Markdorf",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Konrad Knoblauch GmbH; Hr. Bochenek +49-7544-9530-0": {
    "strasse": "Zeppelinstraße 8 - 12",
    "plz": "88677",
    "ort": "Markdorf",
    "email": "info@knoblauch.eu",
    "telefon": "+49 7544 953 0125",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Lierzer Montage Service": {
    "strasse": "Im Brand 8",
    "plz": "88074",
    "ort": "Meckenbeuren",
    "email": "",
    "telefon": "+49 (0) 7542 911 30",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Peuckert GmbH": {
    "strasse": "Stetthaimerstraße 2",
    "plz": "84561",
    "ort": "Mehring",
    "email": "info@peuckert.de",
    "telefon": "+49 (867) 7983-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Siegel GmbH": {
    "strasse": "Gartenstraße 21",
    "plz": "95213",
    "ort": "Münchberg",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Jaeger Ausbau GmbH + Co.KG": {
    "strasse": "Joseph-Dollinger Bogen 24",
    "plz": "80807",
    "ort": "München",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "KOVAC GmbH": {
    "strasse": "Neumarkter Straße 81",
    "plz": "81673",
    "ort": "München",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "REHE Versorgungstechnik GmbH": {
    "strasse": "Theo-Prosel-Weg 7",
    "plz": "80797",
    "ort": "München",
    "email": "",
    "telefon": "+49 (89) 126901-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Teuber+Viel Ingenieurgesellschaft für Energie- und Gebäudetechnik mbH, zu Hdn. Herr Axel Stier": {
    "strasse": "Eversbuschstraße 194",
    "plz": "80999",
    "ort": "München",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Coole - Decken Designkühldecken e.K.": {
    "strasse": "Stubenberg 5",
    "plz": "94089",
    "ort": "Neureichenau",
    "email": "info@coole-decken.com",
    "telefon": "+49 8583 9794885",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Ligamont d.o.o. Lukavac Niederlassung Deutschland": {
    "strasse": "Edisonstr. 40",
    "plz": "90431",
    "ort": "Nürnberg",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Schreinerei Frank Burges": {
    "strasse": "Platenstraße 66",
    "plz": "90441",
    "ort": "Nürnberg",
    "email": "info@frank-burges.de",
    "telefon": "+49 911 54830955",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Prüfling HKS-Energietechnik GmbH": {
    "strasse": "Maria-Merian-Straße 12",
    "plz": "85521",
    "ort": "Ottobrunn",
    "email": "kontakt@pruefling-hks.de",
    "telefon": "+49 (89)  60 86 46 0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Höber GmbH": {
    "strasse": "Eck 6",
    "plz": "94034",
    "ort": "Passau",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Zimmermann Anton  Schreinerei - Innenausbau": {
    "strasse": "Wernberger Str. 36",
    "plz": "92536",
    "ort": "Pfreimd",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Müller-BBM GmbH zu Hdn. Herrn M. Eng. Philipp Meistring": {
    "strasse": "Robert-Koch-Str. 11",
    "plz": "82152",
    "ort": "Planegg",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Kramhöller GmbH Innenausbau": {
    "strasse": "Werner-von-Siemens-Straße 20",
    "plz": "94447",
    "ort": "Plattling",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Fa. Hefter Systemform GmbH Hr. Stephan Wilomitzer": {
    "strasse": "Am Mühlbach 6",
    "plz": "83209",
    "ort": "Priem am Chiemsee",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "TM Ausbau GmbH z.Hd. Herrn Hoch": {
    "strasse": "Aubinger Weg 57",
    "plz": "82178",
    "ort": "Puchheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Hada Mihail GmbH & Co KG": {
    "strasse": "Schrobenhausenerstr. 9",
    "plz": "86554",
    "ort": "Pöttmes",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "L & K Trockenbau GmbH": {
    "strasse": "St.Jakob-Str. 6",
    "plz": "86641",
    "ort": "Rain",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "ANDRITZ Fiedler Gmbh": {
    "strasse": "Weidener Straße 9",
    "plz": "93057",
    "ort": "Regensburg",
    "email": "",
    "telefon": "+49 (941) 6401 602",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "B+M Baustoff + Metall Handels-GmbH": {
    "strasse": "Hofer Straße 39",
    "plz": "93057",
    "ort": "Regensburg",
    "email": "invoice-in.rgb@documents.baustoff-metall.com",
    "telefon": "+49 941 69 66 60",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "DTB-Innenausbau GmbH;  Hr. Wolfgang Hill 0049-8434-9401-0 od. Hr. Schlamp 0049-151-19559820": {
    "strasse": "Industriestraße 14",
    "plz": "86643",
    "ort": "Rennertshofen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Schreinerei Vogl GmbH": {
    "strasse": "Dorfstrasse 16",
    "plz": "94439",
    "ort": "Rossbach/Thanndorf",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "BTB Burkhartsmaier Trockenbau GmbH": {
    "strasse": "Ostring 5",
    "plz": "91154",
    "ort": "Roth",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Demling GmbH & Co KG": {
    "strasse": "Talstraße 6",
    "plz": "97616",
    "ort": "Salz - Bad Neustadt a.d. Saale",
    "email": "",
    "telefon": "+49 (0) 9771 62 40 0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Fa. Haydn & Oberneder  Akustikbau GmbH & Co KG": {
    "strasse": "Waldstraße 22",
    "plz": "94121",
    "ort": "Salzweg",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Hans Huber Trockenbau GmbH": {
    "strasse": "EurimPark 11",
    "plz": "83416",
    "ort": "Surheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Gebäudetechnik Schindler GmbH&Co KG": {
    "strasse": "Ödmiesbacher Straße 29",
    "plz": "92552",
    "ort": "Teunz",
    "email": "info@technik-schindler.de",
    "telefon": "0049 (0) 9671 - 642",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Planotec Innenausbau GmbH": {
    "strasse": "Sägmeister 3",
    "plz": "84577",
    "ort": "Tüßling",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Alois Müller GmbH": {
    "strasse": "Gutenbergstraße 12",
    "plz": "87781",
    "ort": "Ungerhausen",
    "email": "info@alois-mueller.com",
    "telefon": "+49 8393 9467-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Spreitzer Trockenbau": {
    "strasse": "Walder Straße 19",
    "plz": "93192",
    "ort": "Wald / Wutzldorf",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "HCO Ausbau GmbH": {
    "strasse": "Friedrich-Koenig-Str. 12",
    "plz": "97297",
    "ort": "Waldbüttelbrunn",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Ecker / Heiz- und Kühlflächensysteme": {
    "strasse": "Oberpöringer Straße 4",
    "plz": "94574",
    "ort": "Wallerfing",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Ecker Heiz- und Kühlflächensysteme": {
    "strasse": "Oberpöringer Straße 4",
    "plz": "94574",
    "ort": "Wallerfing",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Danhauser Bauzentrum": {
    "strasse": "Dr.-von-Fromme-Straße 8",
    "plz": "92637",
    "ort": "Weiden",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "KE KELIT Klimasysteme Deutschland GmbH": {
    "strasse": "Pfaffenpfad 3",
    "plz": "97440",
    "ort": "Werneck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Weber Schraubautomaten GmbH z.Hnd. Hr. Freilinger Rudolf": {
    "strasse": "Hans-Urmiller-Ring 56",
    "plz": "82515",
    "ort": "Wolfratshausen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Bachhuber Contract GmbH & Co KG": {
    "strasse": "hORMARK 6",
    "plz": "84364",
    "ort": "bAD bIMBACG",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Ruck Günther, Malergeschäft, Trockenbau WDVS, z.Hd.Hrn. Rainer Ruck": {
    "strasse": "Mittlere Stämmig 22",
    "plz": "97292",
    "ort": "Üttingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Bayern",
    "prioritaet": "B"
  },
  "Elcometer Instruments GmbH": {
    "strasse": "Ulmer Stra0e 68",
    "plz": "73431",
    "ort": "Aalen",
    "email": "de_info@elcometer.de",
    "telefon": "+49 7361 528 06 0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Haustechnik",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "inStyle raumerneuerung GmbH": {
    "strasse": "Renchtalstr. 78",
    "plz": "77855",
    "ort": "Achern",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Renz Solutions GmbH": {
    "strasse": "Forchenweg 37",
    "plz": "71134",
    "ort": "Aidlingen",
    "email": "",
    "telefon": "+49 7034 729684-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Manfred Lück GmbH": {
    "strasse": "Ungeheuerhof 9-9a",
    "plz": "71522",
    "ort": "Backnang",
    "email": "info@trockenbau-lueck.de",
    "telefon": "+49 (0) 7191 / 53808",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "ARKU Maschinenbau GmbH": {
    "strasse": "Siemensstraße 11",
    "plz": "76532",
    "ort": "Baden-Baden",
    "email": "info@akru.de",
    "telefon": "+49 7221 5009 800",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "GA-Tec Gebäude- und Anlagentechnik GmbH; Herr Schäfer": {
    "strasse": "Im Metzenacker 5",
    "plz": "76532",
    "ort": "Baden-Baden",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Ingenieurbüro Weingärtner VDI techn. Gebäudeausrüstung": {
    "strasse": "Marienburger Str. 22",
    "plz": "72336",
    "ort": "Balingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Mayer Maschenstoffe Strickstofffabrik Rolf Mayer": {
    "strasse": "Hertenwinkelstraße 25",
    "plz": "72336",
    "ort": "Balingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "GU",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Roma-Strickstofffabrik GmbH & Co. KG": {
    "strasse": "Hertenwinkelstraße 25",
    "plz": "72336",
    "ort": "Balingen",
    "email": "info@roma-strickstoffe.de",
    "telefon": "0049-(0)7433/26029",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Gerhard Braun Unternehmensgruppe": {
    "strasse": "Prinz-Eugen-Straße 11",
    "plz": "74321",
    "ort": "Bietigheim-Bissingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Pill GmbH Möbelelemente": {
    "strasse": "Europastraße 8",
    "plz": "71576",
    "ort": "Burgstetten-Erbstetten",
    "email": "pill@pill-gmbh.de",
    "telefon": "+49 7191 900 90",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Olaf Benesch": {
    "strasse": "Heinrich -Straße 15",
    "plz": "68642",
    "ort": "Bürstadt",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Siegle + Epple; Hr. Zeitz 0049-711-8808299": {
    "strasse": "Max-Planck-Str. 8",
    "plz": "71254",
    "ort": "Ditzingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "DS-Trockenbau 0049/157-71667386": {
    "strasse": "Spitalstraße 9",
    "plz": "73479",
    "ort": "Ellwangen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Raab Karcher Esslingen": {
    "strasse": "Wolf-Hirth-Strasse 8",
    "plz": "73730",
    "ort": "Esslingen",
    "email": "",
    "telefon": "+49 711 310 585",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Sico Ausbau und Fassade": {
    "strasse": "Welfenstr. 6",
    "plz": "70736",
    "ort": "Fellbach",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "GW Bau GmbH": {
    "strasse": "Poststraße 17",
    "plz": "70794",
    "ort": "Filderstadt",
    "email": "",
    "telefon": "0711- 99702763",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Pharma Project Pilots GmbH": {
    "strasse": "Merzhauserstrasse 74",
    "plz": "79100",
    "ort": "Freiburg",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Maler Kübler": {
    "strasse": "Wasenweg 9",
    "plz": "72250",
    "ort": "Freudenstadt",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "STS Trockenbau GmbH": {
    "strasse": "Williy Brandt Straße 13",
    "plz": "76571",
    "ort": "Gaggenau",
    "email": "saitovic@ststrockenbau.de",
    "telefon": "+49(7225)9701780",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Bend and more GmbH zH Herrn Alwin Krebs": {
    "strasse": "Steinenfeldweg 7",
    "plz": "73312",
    "ort": "Geislingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Spedition Wiedmann & Winz zu Hdn. Frau Hauptmann": {
    "strasse": "Neuwiesenstraße 15-18",
    "plz": "73312",
    "ort": "Geislingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Jörg Winklbauer": {
    "strasse": "Wolfschlucht 7",
    "plz": "70839",
    "ort": "Gerlingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Kälberer": {
    "strasse": "Brückenstraße 34",
    "plz": "73037",
    "ort": "Göppingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Wiedmann + Winz": {
    "strasse": "Pfingstwasen 1",
    "plz": "73035",
    "ort": "Göppingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "UniversalProjekt Laden- und Innenausbau GmbH": {
    "strasse": "Wielandstraße 5",
    "plz": "74736",
    "ort": "Hardheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "MAXIMILIAN  MICHEL IIG Industrieisolierungen GmbH": {
    "strasse": "Industriestraße 8",
    "plz": "68542",
    "ort": "Heddesheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "E. Wertheimer GmbH": {
    "strasse": "Wachhausstrasse 1a",
    "plz": "76227",
    "ort": "Karlsruhe",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Vischer Stuckateurbetrieb": {
    "strasse": "Allmend Str. 9",
    "plz": "76199",
    "ort": "Karlsruhe",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Stukkateur Link GmbH": {
    "strasse": "Im Brühl 68/1",
    "plz": "74348",
    "ort": "Lauffen a/N.",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "W. Becker Montagebau GmbH & Co. KG Gewerbepark Ost zu Hdn. Herrn Thomas Diez": {
    "strasse": "Mauserstr. 21",
    "plz": "71640",
    "ort": "Ludwigsburg",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "DIRINGER & SCHEIDEL  BAUUNTERNEHMUNG GmbH & Co. KG": {
    "strasse": "Wilhelm-Wundt-Str.19",
    "plz": "68199",
    "ort": "Mannheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "MF-M.A.R.S. GmbH & Co. KG": {
    "strasse": "Franz-Grashof-Straße 21",
    "plz": "68199",
    "ort": "Mannheim",
    "email": "office@mf-mannheim.de",
    "telefon": "+49 (621) 8619748-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "P5 Mannheim": {
    "strasse": "Fressgasse",
    "plz": "68161",
    "ort": "Mannheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Pfeil GmbH, Frau Bianca Wörns 0049-621-7778090": {
    "strasse": "Boehringerstr. 3",
    "plz": "68307",
    "ort": "Mannheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Maric Trockenbau GmbH z.Hd. Herrn Anton Maric Tel.Nr.: 0173 / 701 32 35": {
    "strasse": "Elzstraße 10",
    "plz": "74821",
    "ort": "Mosbach",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "HEIKAUS GmbH": {
    "strasse": "Hessigheimer Straße 63",
    "plz": "74395",
    "ort": "Mundelsheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Konzernzentrale Bechtle, zur Verf. Fa. Strähle": {
    "strasse": "Bechtle Platz 1; Logistikhalle BA2",
    "plz": "74172",
    "ort": "Neckarsulm",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Decken und Wandtechnik": {
    "strasse": "Rudolf-Diesel-Straße 9",
    "plz": "71154",
    "ort": "Nufringen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Rudolf Jurincic Wand- und Deckentechnik": {
    "strasse": "Rudolf-Diesel-Str. 9",
    "plz": "71154",
    "ort": "Nufringen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Schwarzwald Akustik Decken- & Tennwandbau GmbH": {
    "strasse": "In der Aue 6a",
    "plz": "77704",
    "ort": "Oberkirch-Nußbach",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "PAN-ARMBRUSTER GmbH Wand & Raumlösungen mit System": {
    "strasse": "Raiffeisenstraße 4",
    "plz": "77704",
    "ort": "Oberkirchen",
    "email": "info@pan-armbruster.de",
    "telefon": "+49 7802 7018",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "intek GmbH": {
    "strasse": "Austraße 28",
    "plz": "71739",
    "ort": "Oberriexingen",
    "email": "info@intek.de",
    "telefon": "+49 (0)7042 948 0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "HODZIC GmbH": {
    "strasse": "Saarstrasse 28",
    "plz": "68723",
    "ort": "Oftersheim",
    "email": "info@hodzic-gmbh.de",
    "telefon": "+49 (0) 62 02 - 27 01 52",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Malerwerkstätten Heinrich Schmid GmbH & Co. KG": {
    "strasse": "Max-Eyth-Straße 17",
    "plz": "72793",
    "ort": "Pfullingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Zezelj GmbH Schreinerei / Innenausbau": {
    "strasse": "Hardtweg 12",
    "plz": "71686",
    "ort": "Remseck o. N.",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Edgar Kirn": {
    "strasse": "Armenhöfestraße 32",
    "plz": "77871",
    "ort": "Renchen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Wahl Gruppe GmbH & Co. KG z.Hd. Herr Geschäftsführer Timo Eberwein": {
    "strasse": "Bayernstraße 18-20",
    "plz": "72768",
    "ort": "Reutlingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "MCA-Raumsysteme GmbH": {
    "strasse": "Benzstraße 9/1",
    "plz": "71409",
    "ort": "Schwaikheim",
    "email": "info@mca-raumsysteme.de",
    "telefon": "+43 (7195) 95794-10",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Sysmo-tec GmbH & Co. KG": {
    "strasse": "Max-Eyth-Straße 4",
    "plz": "71409",
    "ort": "Schwaikheim",
    "email": "info@sysmo-tec.de",
    "telefon": "+49 7195 95 79 40 -0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Windmüller Technik GmbH": {
    "strasse": "Robert-Bosch-Straße 8",
    "plz": "74523",
    "ort": "Schwäbisch Hall",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Ceilinx GmbH": {
    "strasse": "Franz-Schubert-Straße 42",
    "plz": "70195",
    "ort": "Stuttgart",
    "email": "info@ceilinx.de",
    "telefon": "+49 (711) 8486180",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Engie Deutschland GmbH (Stuttgart)": {
    "strasse": "Niederlassung Stuttgart Heßbrühlstraße 51",
    "plz": "70565",
    "ort": "Stuttgart",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Fa. Wölpert": {
    "strasse": "Augsburgerstrasse 570",
    "plz": "70327",
    "ort": "Stuttgart",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "HSP Hoppe Sommer Planungs GmbH z.Hd. Frau Peterschilka": {
    "strasse": "Löwenstraße 100",
    "plz": "70597",
    "ort": "Stuttgart",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Kratschmayer GmbH": {
    "strasse": "Dreifeldstr. 50",
    "plz": "70599",
    "ort": "Stuttgart",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Memaj GmbH": {
    "strasse": "Spielbergstraße 61",
    "plz": "70435",
    "ort": "Stuttgart",
    "email": "info@memaj-trockenbau.de",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "S+E Zentrale Stuttgart": {
    "strasse": "Flachter Straße 2 / Lotterbergstraße Zufahrt",
    "plz": "70499",
    "ort": "Stuttgart",
    "email": "info@siegleundepple.de",
    "telefon": "+49 711 8808-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Wolff und Müller GmbH Bauvorhaben RHA Rosenberger Höfe": {
    "strasse": "Breitscheidstraße / Ecke Seidenstraße 21",
    "plz": "70176",
    "ort": "Stuttgart",
    "email": "",
    "telefon": "+49 173 302 9304",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Z.P.C. LDA": {
    "strasse": "Albstadtweg 3",
    "plz": "70567",
    "ort": "Stuttgart",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Züblin Stuttgart": {
    "strasse": "Albstadtweg 3",
    "plz": "70567",
    "ort": "Stuttgart",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "SIEGLE + EPPLE GmbH & Co. KG": {
    "strasse": "Flachter Straße 2",
    "plz": "70499",
    "ort": "Stuttgart - Weilimdorf",
    "email": "info@siegleundepple.de",
    "telefon": "+49 711 8808-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Firma Akustikdecken": {
    "strasse": "Talstraße 18",
    "plz": "73650",
    "ort": "Stuttgart-Winterbach",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "NWI Tübingen": {
    "strasse": "Geschwister-Scholl-Platz",
    "plz": "72074",
    "ort": "Tübingen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "B+M isol GmbH": {
    "strasse": "Wiesenstraße 82",
    "plz": "68519",
    "ort": "Viernheim",
    "email": "info@bm-isol.com",
    "telefon": "+49 6204 70195",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "AKCA Haustechnik Sanitär & Heizung": {
    "strasse": "Hintere Gasse 22",
    "plz": "71336",
    "ort": "Waiblingen",
    "email": "",
    "telefon": "+49 172 91 96 0791",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Strähle Raum-Systeme GmbH": {
    "strasse": "Gewerbestraße 6",
    "plz": "71332",
    "ort": "Waiblingen",
    "email": "info@straehle.de",
    "telefon": "+49 7151 1714-348",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Leibold, Werkstatt f. individuellen Innenausbau": {
    "strasse": "Liststraße 7",
    "plz": "71336",
    "ort": "Waiblingen - Neustadt",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Ganter Interior GmbH": {
    "strasse": "Am Kraftwerk 4",
    "plz": "79183",
    "ort": "Waldkirch",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Baden-Württemberg",
    "prioritaet": "B"
  },
  "Fischer Trockenbau": {
    "strasse": "Eisengasse 6a",
    "plz": "6850",
    "ort": "Dornbirn",
    "email": "fischer.trockenbau@vol.at",
    "telefon": "+43 5572 27 192",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Vorarlberg",
    "prioritaet": "B"
  },
  "BK Kreativ Trockenbau GmbH": {
    "strasse": "Grenzweg 10",
    "plz": "6800",
    "ort": "Feldkirch",
    "email": "info@bk-kreativ.at",
    "telefon": "+43 5522 70390",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Vorarlberg",
    "prioritaet": "B"
  },
  "HILTI + JEHLE GmbH": {
    "strasse": "Hirschgraben 20",
    "plz": "6800",
    "ort": "Feldkirch",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Vorarlberg",
    "prioritaet": "B"
  },
  "Saubermacher Graz, Hr. Reitbauer Tel.: 0664-8290785": {
    "strasse": "Grazer Hauptstrasse",
    "plz": "8073",
    "ort": "Feldkirchen bei Graz",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Vorarlberg",
    "prioritaet": "B"
  },
  "ALPLA Werke Alwin Lehner GmbH & Co KG": {
    "strasse": "Allmendstraße 81",
    "plz": "6971",
    "ort": "Hard",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Vorarlberg",
    "prioritaet": "B"
  },
  "Collini Metallveredelung GmbH": {
    "strasse": "Schweizerstrasse 59",
    "plz": "6845",
    "ort": "Hohenems",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Vorarlberg",
    "prioritaet": "B"
  },
  "Baustoff + Metall GmbH": {
    "strasse": "Ringstraße 7",
    "plz": "6923",
    "ort": "Lauterach",
    "email": "lauterach@baustoff-metall.com",
    "telefon": "+43 5574 823 30",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Vorarlberg",
    "prioritaet": "B"
  },
  "Intemann GmbH Heizung-Sanitär-Klima": {
    "strasse": "Achpark, Dammstraße 4",
    "plz": "6923",
    "ort": "Lauterach",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Vorarlberg",
    "prioritaet": "B"
  },
  "SARD Bau GmbH": {
    "strasse": "Roseggerstraße 2",
    "plz": "6890",
    "ort": "Lustenau",
    "email": "",
    "telefon": "+43 5577 87 447",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Vorarlberg",
    "prioritaet": "B"
  },
  "Fa. Schenker - Lager, zur Verf. Fa. Perchtold": {
    "strasse": "Innsbrucker Straße 11",
    "plz": "6060",
    "ort": "Hall",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Tirol",
    "prioritaet": "A"
  },
  "BV Bastion Hall Herr Kiesling Tel.: 0676 842976202": {
    "strasse": "Unterer Stadtplatz 19",
    "plz": "6060",
    "ort": "Hall in Tirol",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Haustechnik",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "ZFG Fa. Duschek, BV BTV Hakk 1. OG, Hr. Bliem 0664/6144353": {
    "strasse": "Stadtgraben 19",
    "plz": "6060",
    "ort": "Hall in Tirol",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Architekt",
    "region": "Tirol",
    "prioritaet": "C"
  },
  "BVH GHZ II Imst Danner Lüth zur Verfügung Fa. Stolz Herr Pertl Hans Jörg 0664/ 44233296": {
    "strasse": "Dr. Pfeiffenbergerstr. 22",
    "plz": "6460",
    "ort": "Imst",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "GU",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Alternativ Installationen Garber Gmbh Herr Peter Garber": {
    "strasse": "Schneeburggasse 66",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "B+M NewTec GmbH": {
    "strasse": "Etrichgasse 11",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "0512 344 900",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "BV WKO TIROL, Herr Schmidt 0664 8227440": {
    "strasse": "Wilhelm Greil Strasse",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "BV Wiener Städtische Innsbruck, zur Verfügung: Firma Sailer Herr Rauter 0676 / 611 10 94": {
    "strasse": "Südtirolerplatz 4",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "BV447 NHT Innsbruck zur Verf. Fa. TBM-Innenausbau GmbH Hr. Schulz 0662-450800182": {
    "strasse": "Reichenauer Straße 70",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "BVH Dessl Hr. Fuchs 0664/5693117": {
    "strasse": "Gumpstraße 47",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "BVH WA KOPP zur Verfügung Fa. Alternativ  Herr Kopp 0664 / 854 41 92": {
    "strasse": "Dorfgasse 15",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "GRAUP GIPS-BAU GMBH": {
    "strasse": "Höttinger Au 60",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "technik@ggb.co.at",
    "telefon": "+43 (0) 512 / 28 74 47-62",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Gnigler Ges.m.b.H. & Co. KG": {
    "strasse": "Kaufmannstraße 38a",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "+43 512 344 555",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Kältetechnik Tel.Nr.: 0512 / 546655": {
    "strasse": "Valiergasse 38 Stiege 1, Tür 1",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Med UNI Innsbruck z.Verfügung Fa. PERCHTOLD Hr. Martin Lierzer Tel.: +49 / 172 46 12 951": {
    "strasse": "Fritz-Pregl Straße 3",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Messe Innsbruck zur Verf. Fa. Gnigler": {
    "strasse": "Claudiastr.1, Ing. Etzel Strasse",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "TILAK Innsbruck Herr Weber 0664-4367726 od. Herr Geissler 0664-4367714": {
    "strasse": "Zufahrt über Fritz Pregl Straße = Haupteinfahrt Klinik",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Tirol Klinikum, z. Verf. Fa. Gnigler Hr. Weber 06664 4367726": {
    "strasse": "Fritz-Pregl-Straße 3",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "BV Sportalm": {
    "strasse": "St. Johanner Str. 13",
    "plz": "6370",
    "ort": "Kitzbühel",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Hypo Tirol Bank AG ZFG Firma Bouvier / Herr Riedl 0676 6473335": {
    "strasse": "Malserstasse 11",
    "plz": "6500",
    "ort": "Landeck",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "BTV Lienz DG Herr Dold 0664 / 530 1491": {
    "strasse": "Südtiroler Platz 2",
    "plz": "9900",
    "ort": "Lienz",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Bürogebäude Durst Herr Jeller 0664/4215093": {
    "strasse": "Julius Durst Straße 11",
    "plz": "9900",
    "ort": "Lienz",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Landesleitzentrale Lienz Rotes Kreuz-Gebäude; Hr. Schöffauer 0664-88449548 od. Hr. Urban 0664-4367725": {
    "strasse": "Emanuel von Hilber Str. 3a",
    "plz": "9900",
    "ort": "Lienz",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "V&P RIDES": {
    "strasse": "Alleestrasse 20",
    "plz": "9900",
    "ort": "Lienz",
    "email": "office@vprides.at",
    "telefon": "+43 (0) 4852 69766-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Felix GS GmbH": {
    "strasse": "Bahnhofstrasse 65",
    "plz": "6551",
    "ort": "Pians-Landeck",
    "email": "info@felix-gs.at",
    "telefon": "0043 6507041512",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Gremsl & Gruber Innenausbau GmbH": {
    "strasse": "St. Johann in der Haide 102",
    "plz": "8295",
    "ort": "St. Johann in der Haide",
    "email": "office@gremsl-gruber-innenausbau.at",
    "telefon": "03332 61712",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Gremsl + Gruber Innenausbau GmbH": {
    "strasse": "St. Johann in der Haide 102",
    "plz": "8295",
    "ort": "St. Johann in der Haide",
    "email": "office@gremsl-gruber-innenausbau.at",
    "telefon": "03332 61712",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Duschek Haustechnik Kontakt: Frau Doringa Günther, Tel.Nr.: 0664/6144355": {
    "strasse": "Bert-Köllensperger Straße 6b",
    "plz": "6065",
    "ort": "Thaur",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Spar / Tann  Wörgl z.Hd. Hr. Michael Rakautz Tel.Nr.: 0664 / 840 94 12": {
    "strasse": "Spar Straße 1",
    "plz": "6300",
    "ort": "Wörgl",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Tirol",
    "prioritaet": "B"
  },
  "Perron Sparkasse zur Verf. Fa. Perchtold Hr. Kitzberger 0664-4241534": {
    "strasse": "Rainerstrasse 4",
    "plz": "5020",
    "ort": "Salzburg",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Salzburg",
    "prioritaet": ""
  },
  "TBM-Innenausbau GmbH": {
    "strasse": "Aupoint 3",
    "plz": "5101",
    "ort": "Bergheim bei Salzburg",
    "email": "",
    "telefon": "+43 (662) 45 08 00 - 182",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Salzburg",
    "prioritaet": ""
  },
  "Truppenübungsplatz Hochfilzen zur Verf. Fa. TBM-Innenausbau": {
    "strasse": "Aupoint 3",
    "plz": "5101",
    "ort": "Bergheim bei Salzburg",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Salzburg",
    "prioritaet": ""
  },
  "FISCHER SYSTEM TECHNIK AG": {
    "strasse": "Binningerstrasse 112",
    "plz": "4123",
    "ort": "Allschwil",
    "email": "info@fischersystemtechnik.ch",
    "telefon": "+41 61 482 28 80",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Schuler Modul AG": {
    "strasse": "",
    "plz": "6460",
    "ort": "Altdorf URi",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Felix Transport AG": {
    "strasse": "Talstrasse 47",
    "plz": "4144",
    "ort": "Arlesheim",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "BIZ Basel": {
    "strasse": "Centralplatz 2",
    "plz": "4002",
    "ort": "Basel",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "UBS AG Besprechungsboxen zu Verf. Fa. Strähle": {
    "strasse": "Aeschenvorstadt 1",
    "plz": "4002",
    "ort": "Basel",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Strähle Raum-Systeme AG": {
    "strasse": "Müligässli 3",
    "plz": "8598",
    "ort": "Bottighofen TG",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "TEKO Deckensysteme AG": {
    "strasse": "Im Schörli 5",
    "plz": "8600",
    "ort": "Dübendorf",
    "email": "",
    "telefon": "+41 44 533 36 36",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Karl Bubendorfer AG": {
    "strasse": "Hirschenstraße 26 Postfach 158",
    "plz": "9201",
    "ort": "Gossau",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Karl Bubenhofer AG": {
    "strasse": "Hirschenstrasse 26",
    "plz": "9201",
    "ort": "Gossau SG",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Walther Design AG": {
    "strasse": "Dellenbodenweg 1",
    "plz": "4452",
    "ort": "Itingen",
    "email": "info@waltherdesign.ch",
    "telefon": "0041 61 463 13 30",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "LCA Küssnacht z.V. Fa. Walther Design Herr M. Schenker 0041 76 581 12 44": {
    "strasse": "Erlistrasse 3",
    "plz": "6403",
    "ort": "Küssnacht a.R.",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Centre de Rencontre et de Formation, zur Verf. Hr. Antoon Van der Burgt bzw. Hr. Fuchs 0049-151-51520311": {
    "strasse": "Au Village 13",
    "plz": "1483",
    "ort": "Les Montets",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "BLKB Liestal, zur verf. Fa. Walther Design AG": {
    "strasse": "Eichenweg 6",
    "plz": "4410",
    "ort": "Liestal",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "SUVA AG; zur Verf. Fa. Walther Design AG": {
    "strasse": "Alpenquai 28",
    "plz": "6002",
    "ort": "Luzern",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Tanner AG z.Verf. Fa. Walther Design +41 76581 1244": {
    "strasse": "Industriestrasse 2",
    "plz": "5616",
    "ort": "Meisterschwanden",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Intermune AG / Herr Dennis Barnowski 076 500 8397": {
    "strasse": "Tramstrasse 99",
    "plz": "4132",
    "ort": "Muttenz",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "One Tesa zur Verf. Fa. Barcol-Air AG Hr. Keller 0041-582194315": {
    "strasse": "Industriestrasse 8",
    "plz": "8618",
    "ort": "Oetwil",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "MFH Muhen zur Verf. Fa. Barcol Air Hr. Harlacher 0041-582194631": {
    "strasse": "Industriestrasse 8",
    "plz": "8618",
    "ort": "Oetwil am See",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Stöckli Waddesco AG": {
    "strasse": "Götzisbodenweg 2",
    "plz": "4133",
    "ort": "Pratteln",
    "email": "stoekli@stoeckliwadesco.ch",
    "telefon": "+41 61 823 00 00",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "UBS AG, zur Verf. Fa. Strähle  Hr. Wehinger +41 791711969": {
    "strasse": "Avenue des Baumettes 23",
    "plz": "1020",
    "ort": "Renens",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Novisol AG": {
    "strasse": "Weidenweg 15",
    "plz": "4310",
    "ort": "Rheinfelden",
    "email": "info@novisol.ch",
    "telefon": "+41 61 836 16 16",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Barcol-Air Group AG": {
    "strasse": "Wiesenstrasse 5",
    "plz": "8603",
    "ort": "Schwerzenbach",
    "email": "info@barcolair.com",
    "telefon": "+41 58 219 40 00",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Paul Vaucher SA Succursale du Valais": {
    "strasse": "Av. de la Gare 11 / CP 1422",
    "plz": "1951",
    "ort": "Sion",
    "email": "administratif@paul-vauch",
    "telefon": "+41 21 633 1212",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "MWH Suisse SA": {
    "strasse": "Via Gemmo 5H",
    "plz": "6924",
    "ort": "Sorengo",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Deckenbauer AG": {
    "strasse": "Schoretshuebstrasse 24",
    "plz": "9015",
    "ort": "St. Gallen",
    "email": "",
    "telefon": "+41 71 571 19 82",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "BAUSTOFFE PLUS AG": {
    "strasse": "Hauptstrasse 51",
    "plz": "9053",
    "ort": "Teufen AR",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "MWH Fabrik AG": {
    "strasse": "Industriestrasse 81",
    "plz": "6024",
    "ort": "Unwill",
    "email": "info@mwh-ch",
    "telefon": "+41 22 949 5959",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Fa. Phonex Herr Maidl": {
    "strasse": "Buchgrindelstrasse 14",
    "plz": "8620",
    "ort": "Wetzikon ZH",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Prime Tower Zürich": {
    "strasse": "Umschlagplatz Nr. 4",
    "plz": "8005",
    "ort": "Zürich",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "UBS AG - 4.OG": {
    "strasse": "Paradeplatz 6",
    "plz": "8001",
    "ort": "Zürich",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "UBS AG - Hauptsitz HGHG, zur Verf. Fa. Strähle Hr Gasztyk 0049 1735948973": {
    "strasse": "Bahnhofstrasse 45",
    "plz": "8001",
    "ort": "Zürich",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "UBS AG - Refufbishment 3.+4.OG": {
    "strasse": "Bärengasse 16",
    "plz": "8001",
    "ort": "Zürich",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Schweiz",
    "prioritaet": "B"
  },
  "Bv. Schmidhammer Hr. Lageder 0039/3487210193": {
    "strasse": "Via Macello 61",
    "plz": "39100",
    "ort": "Bozen",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Südtirol",
    "prioritaet": "B"
  },
  "Dallan Spa": {
    "strasse": "via per Salvatrondo, 50",
    "plz": "31033",
    "ort": "Castelfranco Veneto",
    "email": "",
    "telefon": "+39 0423 734111",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Südtirol",
    "prioritaet": "B"
  },
  "Hatek": {
    "strasse": "Pillhof 35",
    "plz": "39057",
    "ort": "Frangart",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Südtirol",
    "prioritaet": "B"
  },
  "Schweitzer Project Tel.Nr.: 0039 (0)473 670670": {
    "strasse": "Industriezone 7-9",
    "plz": "39025",
    "ort": "Naturns (BZ)",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Südtirol",
    "prioritaet": "B"
  },
  "Eurotek Klima SRL": {
    "strasse": "Via Cisa Sud S.N.Loc.Pratola",
    "plz": "54028",
    "ort": "Villafranca in Lunigiana (MS)",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "",
    "region": "Südtirol",
    "prioritaet": "B"
  },
  "Dualis AG": {
    "strasse": "Industriering 14",
    "plz": "9491",
    "ort": "Ruggell",
    "email": "office@dualis.li",
    "telefon": "+423 370 2270",
    "ansprechpartner": "Egon Zechmann",
    "mobil": "",
    "branche": "",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "Mohr & Hornikel": {
    "strasse": "Ortsstr. 28",
    "plz": "76228",
    "ort": "Karlsruhe",
    "email": "",
    "telefon": "0721 94541501",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "Stoeckli Wadesco AG": {
    "strasse": "Götzisbodenweg 2",
    "plz": "4133",
    "ort": "Pratteln",
    "email": "",
    "telefon": "+41 61 823 00 00",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "Innenausbau Südtirol": {
    "strasse": "Montal 44/A",
    "plz": "39030",
    "ort": "St. Lorenzen",
    "email": "",
    "telefon": "0474 404 037",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Tirol",
    "prioritaet": ""
  },
  "Metallmont GmbH": {
    "strasse": "Kaistenbergstrasse 26",
    "plz": "CH-5070",
    "ort": "Frick",
    "email": "",
    "telefon": "+41 62 871 84 71",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "Dewaisol AG": {
    "strasse": "Bottigenstrasse 217b",
    "plz": "3019",
    "ort": "Bern",
    "email": "",
    "telefon": "031 971 60 00",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "KT Ausbautechnik AG": {
    "strasse": "Paul Klee-Strasse 101",
    "plz": "3053",
    "ort": "Münchenbuchsee",
    "email": "",
    "telefon": "+41 31 868 88 88",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Bernhard Dach GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "032 665 31 31",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "R.I.D. GmbH Trockenbau": {
    "strasse": "Interpark 15",
    "plz": "76877",
    "ort": "Offenbach",
    "email": "",
    "telefon": "06348/98420",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "Dualis": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "Hillebrand Huber GmbH": {
    "strasse": "Pionierstraße 2",
    "plz": "82152",
    "ort": "Krailling",
    "email": "",
    "telefon": "+49 89 896096-0",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Roland Vasi GmbH": {
    "strasse": "St.-Benedikt-Str. 1",
    "plz": "85716",
    "ort": "Unterschleißheim",
    "email": "",
    "telefon": "+49 176 30330336",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Mueller Trockenbau": {
    "strasse": "Ziegeleistr. 4 A",
    "plz": "87772",
    "ort": "Pfaffenhausen",
    "email": "",
    "telefon": "+49 2722 6577840",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Obermeyer & Schmitz": {
    "strasse": "Gewerbering Ost 4",
    "plz": "93155",
    "ort": "Hemau",
    "email": "",
    "telefon": "+49 9491 902930",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Kurzemann Trockenbau GmbH": {
    "strasse": "Staudenweg 24",
    "plz": "6850",
    "ort": "Dornbirn",
    "email": "",
    "telefon": "+43 5572 33355",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Vorarlberg",
    "prioritaet": ""
  },
  "KR Schweiz": {
    "strasse": "Luzernerstrasse 91",
    "plz": "5630",
    "ort": "Muri AG",
    "email": "",
    "telefon": "+41 56 6645510",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "Tiroler Trockenbau": {
    "strasse": "Schützenstraße 49a",
    "plz": "6020",
    "ort": "Innsbruck",
    "email": "",
    "telefon": "+43 512 121212",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Tirol",
    "prioritaet": ""
  },
  "Kramhoeller GmbH": {
    "strasse": "Werner-von-Siemens-Str. 20",
    "plz": "94447",
    "ort": "Plattling",
    "email": "",
    "telefon": "+49 9931 98080",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Bayern",
    "prioritaet": ""
  },
  "RIES Akustik-Innenausbau GmbH": {
    "strasse": "Raiffeisenstraße 2a",
    "plz": "86733",
    "ort": "Alerheim",
    "email": "",
    "telefon": "+49 09085 96940",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Bayern",
    "prioritaet": ""
  },
  "MDS Bauunternehmen": {
    "strasse": "Höchster Straße 30",
    "plz": "65835",
    "ort": "Liederbach",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Trockenbau Celik e.K.": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "+49 8265 730673",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Bayern",
    "prioritaet": ""
  },
  "KST AG": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "+41 55 418 70 50",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "Bayazid Innenausbau GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Asen Akustik-und Trockenbau GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Brändle Installationen": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Vorarlberg",
    "prioritaet": ""
  },
  "Reinisch Bau GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "Pagitsch": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "Intermass Innenausbau": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "Pfau GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "weischedel & binder": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "Trockenbauteam GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Tirol",
    "prioritaet": ""
  },
  "ILP Trockenbau GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Tirol",
    "prioritaet": ""
  },
  "Pi Innenausbau": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Tirol",
    "prioritaet": ""
  },
  "trockenbau-ms.at": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "stuck-michl.at": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Tirol",
    "prioritaet": ""
  },
  "BHW Bauhandwerk": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Salzburg",
    "prioritaet": ""
  },
  "Kälin Deckenbau": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "Silent Deckensysteme": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "Isolag AG": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "IDL Deckenbau": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "Tschanz Deckenverkleidungen AG": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "RE-DECKEN": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "x-akustik.ch": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "Systemdecken": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "x-metall": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Tirol",
    "prioritaet": ""
  },
  "KATMETAL": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Tirol",
    "prioritaet": ""
  },
  "MetallDesign GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Tirol",
    "prioritaet": ""
  },
  "ellecosta": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Südtirol",
    "prioritaet": ""
  },
  "PICHLER projects": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Tirol",
    "prioritaet": ""
  },
  "Steinfeld GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Tirol",
    "prioritaet": ""
  },
  "Wiedenhofer GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Tirol",
    "prioritaet": ""
  },
  "Idea Casa Plan": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Südtirol",
    "prioritaet": ""
  },
  "Isodomus GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Tirol",
    "prioritaet": ""
  },
  "Kager HSI GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Südtirol",
    "prioritaet": ""
  },
  "Climant": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Tirol",
    "prioritaet": ""
  },
  "Singer Akustik und Architektur": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Bayern",
    "prioritaet": ""
  },
  "projekt:m³": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Phoneon": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Raumakustik-Team München": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Auri Akustik": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Lech Büroplanung": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Bayern",
    "prioritaet": ""
  },
  "Möhler + Partner": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Bayern",
    "prioritaet": ""
  },
  "SEF Ingenieurbüro": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "IBE GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Architekt",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "Planungsgesellschaft SCHAAF": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "ibheimsch GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "dieBauingenieure": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "WIRTH-Ingenieure": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "engineering_consult": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "EGS-plan": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Baden-Württemberg",
    "prioritaet": ""
  },
  "Heinrich Schmid": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "JA-ARCHITEKTUR": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Architekt",
    "region": "Tirol",
    "prioritaet": ""
  },
  "UNISONO ARCHITEKTEN": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Architekt",
    "region": "Tirol",
    "prioritaet": ""
  },
  "ATP architekten ingenieure": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Tirol",
    "prioritaet": ""
  },
  "SNOW ARCHITEKTUR": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Architekt",
    "region": "Tirol",
    "prioritaet": ""
  },
  "Stöger+Zelger Architekten": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Architekt",
    "region": "Tirol",
    "prioritaet": ""
  },
  "ROECK Architekten": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Tirol",
    "prioritaet": ""
  },
  "Bauphysik Team": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Salzburg",
    "prioritaet": ""
  },
  "ROHDE ACOUSTICS": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Salzburg",
    "prioritaet": ""
  },
  "Ziegler Schallschutz": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Salzburg",
    "prioritaet": ""
  },
  "Akustik-Design": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Salzburg",
    "prioritaet": ""
  },
  "Dr. Harald Graf-Müller": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Salzburg",
    "prioritaet": ""
  },
  "Akustik Buch GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Salzburg",
    "prioritaet": ""
  },
  "Bürodesign Bliem": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Salzburg",
    "prioritaet": ""
  },
  "MC-Engineering GmbH": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Südtirol",
    "prioritaet": ""
  },
  "Isifer Metallbau": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Tirol",
    "prioritaet": ""
  },
  "Lindner Group": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "BER Deckensysteme": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "NOVISOL AG": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Schweiz",
    "prioritaet": ""
  },
  "Estrics": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "SAS International": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "Trikustik": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "HOFA-Akustik": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "freiraum Akustik": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Bauplanung",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "raum-akustiks.de": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Sonstige",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "Fural": {
    "strasse": "",
    "plz": "",
    "ort": "",
    "email": "",
    "telefon": "",
    "ansprechpartner": "",
    "mobil": "",
    "branche": "Metallmontage",
    "region": "Sonstige",
    "prioritaet": ""
  },
  "Büroumbau Hälg / Hälg & Co. AG": {
    "strasse": "Neumattstraße 30",
    "plz": "5000",
    "ort": "Aarau",
    "email": "",
    "telefon": "",
    "ansprechpartner": "Hr. Malveda",
    "mobil": "",
    "branche": "Trockenbau",
    "region": "Schweiz",
    "prioritaet": ""
  }
}

KUNDENLISTE = sorted(KUNDEN_DB.keys())

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_file(uploaded_file):
    ext = uploaded_file.name.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    filepath = os.path.join(UPLOADS_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return {"name": uploaded_file.name, "path": filepath}

st.set_page_config(page_title="MCI Metalldecken – Besuchsberichte", page_icon="🏗️", layout="wide")

st.markdown("""
<style>
    .top-header {
        background: linear-gradient(135deg, #0d2137 0%, #1a4a7a 60%, #2980b9 100%);
        padding: 28px 36px; border-radius: 16px; color: white;
        margin-bottom: 28px; box-shadow: 0 4px 20px rgba(0,0,0,0.18);
    }
    .top-header h1 { margin: 0; font-size: 2em; font-weight: 700; }
    .top-header p { margin: 6px 0 0 0; opacity: 0.85; }
    .stat-card { background: white; border-radius: 12px; padding: 20px; text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.07); border-top: 4px solid #2980b9; }
    .stat-card h2 { font-size: 2.2em; color: #1a4a7a; margin: 0; }
    .stat-card p { color: #666; margin: 4px 0 0 0; font-size: 0.9em; }
    .section-title { color: #1a4a7a; font-size: 1.05em; font-weight: 700;
        border-bottom: 2px solid #2980b9; padding-bottom: 6px; margin: 18px 0 12px 0; }
    div[data-testid="stSidebar"] { background: linear-gradient(180deg, #0d2137 0%, #1a4a7a 100%); }
    div[data-testid="stSidebar"] * { color: white !important; }
    .stButton > button { background: linear-gradient(90deg, #1a4a7a, #2980b9);
        color: white; border: none; border-radius: 8px; padding: 10px 24px; font-weight: 600; }
    .auto-filled { background-color: #e8f4fd !important; border: 1.5px solid #2980b9 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="top-header">
    <h1>🏗️ MCI Metalldecken – Besuchsberichte</h1>
    <p>Außendienst-Dokumentation | Berichte erfassen, suchen und filtern</p>
</div>
""", unsafe_allow_html=True)

data_all = load_data()
st.sidebar.markdown("## 📂 Navigation")
menu = st.sidebar.radio("", ["📝 Neuer Bericht", "📋 Alle Berichte", "🔍 Kundenübersicht"])
st.sidebar.markdown("---")
st.sidebar.markdown(f"📊 **{len(data_all)}** Berichte gesamt")
st.sidebar.markdown(f"🏢 **{len(set(r['kunde'] for r in data_all))}** Kunden besucht")
st.sidebar.markdown(f"📋 **{len(KUNDENLISTE)}** Kunden in Datenbank")
st.sidebar.markdown("---")
st.sidebar.markdown("**MCI Metalldecken GmbH**")
st.sidebar.markdown("Außendienst-Tool v3.0")

# ── NEUER BERICHT ────────────────────────────────────────────
if menu == "📝 Neuer Bericht":
    st.markdown("## 📝 Neuen Besuchsbericht erfassen")

    st.markdown('<div class="section-title">🏢 Kunde auswählen</div>', unsafe_allow_html=True)
    col_sel1, col_sel2 = st.columns([3,1])
    with col_sel1:
        kunde_auswahl = st.selectbox("Kundenname aus Liste wählen", ["-- Neuen Kunden eingeben --"] + KUNDENLISTE)
    with col_sel2:
        st.markdown("<br>", unsafe_allow_html=True)
        neuer_kunde = kunde_auswahl == "-- Neuen Kunden eingeben --"

    # Auto-fill from DB
    if neuer_kunde:
        kd = {}
    else:
        kd = KUNDEN_DB.get(kunde_auswahl, {})

    with st.form("bericht_form", clear_on_submit=True):
        st.markdown('<div class="section-title">👤 Kundendaten</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if neuer_kunde:
                kunde = st.text_input("Kundenname / Firma *")
            else:
                kunde = st.text_input("Kundenname / Firma", value=kunde_auswahl, disabled=True)
            ansprechpartner = st.text_input("Ansprechpartner", value=kd.get("ansprechpartner",""))
            telefon = st.text_input("Telefon", value=kd.get("telefon",""))
            email_kunde = st.text_input("E-Mail", value=kd.get("email",""))
        with col2:
            strasse = st.text_input("Straße", value=kd.get("strasse",""))
            plz_ort_val = f"{kd.get('plz','')} {kd.get('ort','')}".strip()
            plz_ort = st.text_input("PLZ / Ort", value=plz_ort_val)
            region_options = ["Bayern","Baden-Württemberg","Schweiz","Südtirol","Vorarlberg","Tirol","Salzburg","Sonstige"]
            reg_val = kd.get("region","Bayern")
            reg_idx = region_options.index(reg_val) if reg_val in region_options else 0
            region = st.selectbox("Region", region_options, index=reg_idx)
            branche_options = ["","Architekt","Bauplanung","Trockenbau","Metallmontage","Facility Management","GU","Haustechnik","Sonstige"]
            br_val = kd.get("branche","")
            br_idx = branche_options.index(br_val) if br_val in branche_options else 0
            branche = st.selectbox("Branche", branche_options, index=br_idx)

        if not neuer_kunde:
            st.info("✅ Kundendaten automatisch aus der Datenbank übernommen – bitte prüfen und ggf. anpassen.")

        st.markdown('<div class="section-title">📅 Besuchsdetails</div>', unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3:
            besuchsdatum = st.date_input("Besuchsdatum *", value=date.today())
            besuchsart = st.selectbox("Besuchsart", ["Erstbesuch","Folgebesuch","Servicebesuch","Akquise","Reklamation","Sonstiges"])
            prioritaet = st.selectbox("Priorität", ["Hoch","Mittel","Niedrig"])
        with col4:
            naechster_termin = st.date_input("Nächster Termin", value=date.today() + timedelta(days=30))
            erfasst_von = st.text_input("Erfasst von (Name)")
            umsatzpotenzial = st.selectbox("Umsatzpotenzial", ["Hoch","Mittel","Niedrig","Unbekannt"])

        st.markdown('<div class="section-title">📝 Bericht</div>', unsafe_allow_html=True)
        ziele = st.text_area("Besuchsziele", height=80)
        ergebnisse = st.text_area("Ergebnisse / Gesprächsinhalt", height=120)
        massnahmen = st.text_area("Maßnahmen / To-Dos", height=80)
        notizen = st.text_area("Weitere Notizen", height=80)

        st.markdown('<div class="section-title">📎 Dateien & Bilder</div>', unsafe_allow_html=True)
        uploads = st.file_uploader("Bilder, PDFs oder Dokumente", accept_multiple_files=True)

        col_b1, col_b2, col_b3 = st.columns([2,1,2])
        with col_b2:
            submitted = st.form_submit_button("💾 Speichern", use_container_width=True)

        if submitted:
            k_name = kunde if neuer_kunde else kunde_auswahl
            if not k_name or k_name == "-- Neuen Kunden eingeben --":
                st.error("⚠️ Bitte Kundenname angeben.")
            else:
                saved_files = [save_file(uf) for uf in uploads]
                data = load_data()
                data.append({
                    "id": str(uuid.uuid4()),
                    "datum": str(besuchsdatum),
                    "kunde": k_name,
                    "ansprechpartner": ansprechpartner,
                    "telefon": telefon,
                    "email_kunde": email_kunde,
                    "strasse": strasse,
                    "plz_ort": plz_ort,
                    "region": region,
                    "branche": branche,
                    "besuchsart": besuchsart,
                    "prioritaet": prioritaet,
                    "naechster_termin": str(naechster_termin),
                    "erfasst_von": erfasst_von,
                    "umsatzpotenzial": umsatzpotenzial,
                    "ziele": ziele,
                    "ergebnisse": ergebnisse,
                    "massnahmen": massnahmen,
                    "notizen": notizen,
                    "dateien": saved_files,
                    "erstellt_am": datetime.now().strftime("%Y-%m-%d %H:%M"),
                })
                save_data(data)
                st.success(f"✅ Bericht für **{k_name}** gespeichert!")
                st.balloons()

# ── ALLE BERICHTE ────────────────────────────────────────────
elif menu == "📋 Alle Berichte":
    st.markdown("## 📋 Alle Besuchsberichte")
    data = load_data()
    if not data:
        st.info("Noch keine Berichte vorhanden.")
    else:
        col1, col2, col3, col4 = st.columns(4)
        heute = date.today()
        with col1:
            st.markdown(f'<div class="stat-card"><h2>{len(data)}</h2><p>Berichte gesamt</p></div>', unsafe_allow_html=True)
        with col2:
            hoch = sum(1 for r in data if r.get("prioritaet") == "Hoch")
            st.markdown(f'<div class="stat-card"><h2 style="color:#c0392b">{hoch}</h2><p>Priorität Hoch</p></div>', unsafe_allow_html=True)
        with col3:
            dm = sum(1 for r in data if r.get("datum","")[:7] == str(heute)[:7])
            st.markdown(f'<div class="stat-card"><h2>{dm}</h2><p>Diesen Monat</p></div>', unsafe_allow_html=True)
        with col4:
            kc = len(set(r["kunde"] for r in data))
            st.markdown(f'<div class="stat-card"><h2>{kc}</h2><p>Kunden besucht</p></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            f_kunde = st.text_input("🔍 Kundenname")
        with col2:
            f_region = st.selectbox("Region", ["Alle","Bayern","Baden-Württemberg","Schweiz","Südtirol","Vorarlberg","Tirol","Salzburg","Sonstige"])
        with col3:
            f_prio = st.selectbox("Priorität", ["Alle","Hoch","Mittel","Niedrig"])
        with col4:
            f_zeitraum = st.selectbox("Zeitraum", ["Alle","Diese Woche","Dieser Monat","Letzter Monat","Dieses Jahr"])

        filtered = data
        if f_kunde:
            filtered = [r for r in filtered if f_kunde.lower() in r["kunde"].lower()]
        if f_region != "Alle":
            filtered = [r for r in filtered if r.get("region") == f_region]
        if f_prio != "Alle":
            filtered = [r for r in filtered if r.get("prioritaet") == f_prio]
        if f_zeitraum != "Alle":
            if f_zeitraum == "Diese Woche":
                start = heute - timedelta(days=heute.weekday())
            elif f_zeitraum == "Dieser Monat":
                start = heute.replace(day=1)
            elif f_zeitraum == "Letzter Monat":
                start = (heute.replace(day=1) - timedelta(days=1)).replace(day=1)
            else:
                start = heute.replace(month=1, day=1)
            filtered = [r for r in filtered if r.get("datum","") >= str(start)]

        st.markdown(f"**{len(filtered)} Bericht(e) gefunden**")
        for r in reversed(filtered):
            with st.expander(f"📅 {r['datum']}  |  🏢 {r['kunde']}  |  📍 {r.get('region','')}  |  👤 {r.get('erfasst_von','')}  |  ⚡ {r.get('prioritaet','')}"):
                col1,col2,col3 = st.columns(3)
                with col1:
                    st.markdown("**📞 Kontakt**")
                    st.write(f"Ansprechpartner: {r.get('ansprechpartner','–')}")
                    st.write(f"Telefon: {r.get('telefon','–')}")
                    st.write(f"E-Mail: {r.get('email_kunde','–')}")
                    st.write(f"Adresse: {r.get('strasse','')} {r.get('plz_ort','')}")
                with col2:
                    st.markdown("**📋 Besuch**")
                    st.write(f"Besuchsart: {r.get('besuchsart','–')}")
                    st.write(f"Priorität: {r.get('prioritaet','–')}")
                    st.write(f"Nächster Termin: {r.get('naechster_termin','–')}")
                    st.write(f"Umsatzpotenzial: {r.get('umsatzpotenzial','–')}")
                with col3:
                    st.markdown("**📝 Inhalt**")
                    st.write(f"Ziele: {r.get('ziele','–')}")
                    st.write(f"Ergebnisse: {r.get('ergebnisse','–')}")
                    st.write(f"Maßnahmen: {r.get('massnahmen','–')}")
                if r.get("notizen"):
                    st.info(f"📌 {r['notizen']}")
                if r.get("dateien"):
                    st.markdown("**📎 Dateien:**")
                    for df in r["dateien"]:
                        if os.path.exists(df["path"]):
                            with open(df["path"], "rb") as file:
                                st.download_button(f"⬇️ {df['name']}", data=file, file_name=df["name"], key=df["path"])
                st.markdown("---")
                if st.button(f"🗑️ Bericht löschen", key=f"del_{r['id']}"):
                    data_neu = [x for x in data if x["id"] != r["id"]]
                    save_data(data_neu)
                    st.success("Bericht gelöscht!")
                    st.rerun()

# ── KUNDENÜBERSICHT ──────────────────────────────────────────
elif menu == "🔍 Kundenübersicht":
    st.markdown("## 🔍 Kundenübersicht – Letzter Besuch")
    data = load_data()
    if not data:
        st.info("Noch keine Berichte vorhanden.")
    else:
        kunden = {}
        for r in data:
            k = r["kunde"]
            if k not in kunden or r["datum"] > kunden[k]["datum"]:
                kunden[k] = r
        suche = st.text_input("🔍 Kunde suchen")
        kunden_liste = sorted(kunden.values(), key=lambda x: x["datum"], reverse=True)
        if suche:
            kunden_liste = [k for k in kunden_liste if suche.lower() in k["kunde"].lower()]
        st.markdown(f"**{len(kunden_liste)} Kunden**")
        for r in kunden_liste:
            tage = (date.today() - date.fromisoformat(r["datum"])).days
            farbe = "🔴" if tage > 90 else "🟡" if tage > 30 else "🟢"
            alle = [x for x in data if x["kunde"] == r["kunde"]]
            with st.expander(f"{farbe} {r['kunde']}  |  Letzter Besuch: {r['datum']} ({tage} Tage)  |  {len(alle)} Besuche"):
                col1,col2 = st.columns(2)
                with col1:
                    st.write(f"**Ansprechpartner:** {r.get('ansprechpartner','–')}")
                    st.write(f"**Telefon:** {r.get('telefon','–')}")
                    st.write(f"**Adresse:** {r.get('strasse','')} {r.get('plz_ort','')}")
                with col2:
                    st.write(f"**Nächster Termin:** {r.get('naechster_termin','–')}")
                    st.write(f"**Letzter Bericht von:** {r.get('erfasst_von','–')}")
                    st.write(f"**Ergebnisse:** {r.get('ergebnisse','–')}")

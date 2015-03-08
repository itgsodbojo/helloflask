En enkel flask app för att demonstrera hur man deployar en applikation.

Det är inte komplett men det fungerar.


Ni kan skapa en distribution genom att ange följande i en terminal, i samma katalog som setup.py finns.,

 `python setup.py sdist --formats=gztar`
 
 Fungerar det ska ni ha en katolog dist med en komprimerad uppsättning av projektet.
 
 Den går att installera med 
 
    pip install helloflask-0.0.1.dev0.tar.gz

Om ni ska göra en egen  behöver ni åtminstone ändra i

- setup.py
    
- MANIFEST.in

Läs filerna i exemplet och byt ut till egna värden.

En manual hittar ni här. [docs.python.org](https://docs.python.org/2/distutils/setupscript.html)
    

En beskrivning och lite hjälp av hur man deployar detta till en server finne i de här projektet. 
flask-development
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:57:59 2019

@author: Tine
"""

authors = ["Darwin", "Lovelace", "Hawking", "Noether"]

output_fh = open("list.html", "w")

scaffold_start = """<!DOCTYPE html>
<html>
<head>
<title>Titel dieser wunderbaren Seite</title>
</head>
<body>

<h1>Eine grandiose Überschrift</h1>

<p>Ein nicht weniger toller Abschnitt.</p>

<ul>
"""

output_fh.write(scaffold_start)

scaffold_middle = ""

for author in authors:
    scaffold_middle = scaffold_middle + "<li>" + author + "</li>\n"
        
print(scaffold_middle)

output_fh.write(scaffold_middle)

scaffold_end = """
</ul>
</body>

</html>"""

output_fh.write(scaffold_end)

output_fh.close()
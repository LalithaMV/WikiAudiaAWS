# -*- coding: utf-8 -*-
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
#pdf.add_font('Kedage-b', '', 'Kedage-b.ttf', uni=True) 
#pdf.set_font('Kedage-b', '', 14)
pdf.add_font('Meera_04', '', 'Meera_04.ttf', uni=True) 
pdf.set_font('Meera_04', '', 14)
linestring = open('Input.txt', 'r').read()
pdf.write(20,linestring)
pdf.ln(20)
pdf.output("Output.pdf", 'F')

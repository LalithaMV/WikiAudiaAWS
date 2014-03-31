# -*- coding: utf-8 -*-
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.add_font('Meera_04', '', 'Meera_04.ttf', uni=True) 
pdf.set_font('Meera_04', '', 14)
#pdf.add_font('MalFont', '', 'Kinnari.ttf', uni=True) 
#pdf.set_font('MalFont', '', 30)
linestring = open('Input.txt', 'r').read()
pdf.write(20,linestring)
pdf.ln(20)
pdf.output("Output.pdf", 'F')

'''
from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.add_font('Garuda', '', 'Garuda.ttf', uni=True) 
pdf.set_font('Garuda', '', 14)
#pdf.set_font('Arial','B',16)
pdf.cell(40,10,'मोरा')
pdf.output('Output.pdf','F')
'''
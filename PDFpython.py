# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 04:49:22 2020

@author: Tarun
"""

import PyPDF2 as p2


pdf = open("DVWA_v1.3.pdf","rb")

pdfread = p2.PdfFileReader(pdf)

#spage = pdfread.getPage(1)

#print(spage.extractText())
#print(pdfread.getIsEncrypted())
#print(pdfread.getDocumentInfo())
#print(pdfread.getNumPages())



i =0 
while i<pdfread.getNumPages():
    pageinfo = pdfread.getPage(i)
    print(pageinfo.extractText())
    i = i + 1
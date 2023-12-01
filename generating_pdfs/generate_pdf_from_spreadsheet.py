import pandas
from fpdf import FPDF

df = pandas.read_excel('data.xlsx')


for index, row in df.iterrows():
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=50, txt=row['name'], align="C", border=1, ln=1)

    for column in df.columns[1:]:
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt=f'{column.title()} :')

        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=row[column], ln=1)

    # pdf.set_font(family='Times', style='B', size=14)
    # pdf.cell(w=100, h=25, txt="Phylum: ")
    #
    # pdf.set_font(family='Times', size=14)
    # pdf.cell(w=100, h=25, txt=row['phylum'], ln=1)
    #
    # pdf.set_font(family='Times', style='B', size=14)
    # pdf.cell(w=100, h=25, txt="Class: ")
    #
    # pdf.set_font(family='Times', size=14)
    # pdf.cell(w=100, h=25, txt=row['class'], ln=1)
    #
    # pdf.set_font(family='Times', style='B', size=14)
    # pdf.cell(w=100, h=25, txt="Order: ")
    #
    # pdf.set_font(family='Times', size=14)
    # pdf.cell(w=100, h=25, txt=row['order'], ln=1)
    #
    # pdf.set_font(family='Times', style='B', size=14)
    # pdf.cell(w=100, h=25, txt="Suborder: ")
    #
    # pdf.set_font(family='Times', size=14)
    # pdf.cell(w=100, h=25, txt=row['suborder'], ln=1)

    pdf.output(f'animals/{row["name"]}.pdf')


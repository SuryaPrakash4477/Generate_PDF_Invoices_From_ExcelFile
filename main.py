import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation = "P", unit = "mm", format = "A4")
    pdf.add_page()

    # Extracting the Number form the file name
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    # Setting the font
    pdf.set_font(family = "Times", size = 16, style = "B")

    # Adding the Page
    pdf.cell(w = 50, h = 8, txt = f"Invoice nr.{invoice_nr}", ln = 1)

    # Setting the font
    pdf.set_font(family = "Times", size = 16, style = "B")

    # Adding the Page
    pdf.cell(w = 50, h = 8, txt = f"Date.{date}", ln = 1)

    df = pd.read_excel(filepath, sheet_name = "Sheet 1")

    # Adding Header
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family = "Times", size = 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w = 30, h = 8, txt = columns[0], border = 1)
    pdf.cell(w = 70, h = 8, txt = columns[1], border = 1)
    pdf.cell(w = 30, h = 8, txt = columns[2], border = 1)
    pdf.cell(w = 30, h = 8, txt = columns[3], border = 1)
    pdf.cell(w = 30, h = 8, txt = columns[4], border = 1, ln = 1)

    # Adding Rows to the table
    for iindex, row in df.iterrows():
        pdf.set_font(family = "Times", size = 10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w = 30, h = 8, txt = str(row["product_id"]), border = 1)
        pdf.cell(w = 70, h = 8, txt = str(row["product_name"]), border = 1)
        pdf.cell(w = 30, h = 8, txt = str(row["amount_purchased"]), border = 1)
        pdf.cell(w = 30, h = 8, txt = str(row["price_per_unit"]), border = 1)
        pdf.cell(w = 30, h = 8, txt = str(row["total_price"]), border = 1, ln = 1)

    pdf.output(f"PDFs/{filename}.pdf")


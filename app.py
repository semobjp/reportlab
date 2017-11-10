"""
Main Application (Report Database STT)
"""
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from data_interface import get_report_data
from report_as_pdf import parse_line_format, list_to_table_format



# Reportlab Simple Doc Template
pdf_elements_array = []


if __name__ == "__main__":
    doc = SimpleDocTemplate("report.pdf", pagesize=A4)
    db_data = get_report_data()
    parsed_list = list_to_table_format(db_data)

    table = Table(parsed_list)
    pdf_elements_array.append(table)
    doc.build(pdf_elements_array)

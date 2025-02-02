from fpdf import FPDF
import os


def create_pdf_from_folder(folder_path, output_pdf):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=10)

    # Traverse the folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(
                (".py", ".txt", ".md")
            ):  # Add more extensions if needed
                pdf.add_page()
                pdf.cell(200, 10, txt=file_path, ln=True, align="C")
                with open(file_path, "r") as f:
                    for line in f:
                        pdf.cell(200, 10, txt=line.strip(), ln=True)

    pdf.output(output_pdf)


# Usage
folder_path = "."
output_pdf = "output.pdf"
create_pdf_from_folder(folder_path, output_pdf)

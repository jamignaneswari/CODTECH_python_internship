from fpdf import FPDF

# Read data from file
with open("data.txt", "r") as file:
    content = file.readlines()

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Internship Task 2 Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)

# Add file content to PDF
for line in content:
    pdf.multi_cell(0, 10, line)

# Save PDF
pdf.output("Task_2_Report.pdf")

print("PDF report generated successfully!")
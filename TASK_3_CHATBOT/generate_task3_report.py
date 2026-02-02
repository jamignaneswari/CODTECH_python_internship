# Task 3: Automated PDF Report Generation
# CODTECH Python Internship
# Intern Name: Jami Gnaneswari

from fpdf import FPDF

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "TASK 3 REPORT - AI CHATBOT WITH NLP", ln=True, align="C")
pdf.ln(10)

# Read data from text file
with open("task3_data.txt", "r") as file:
    content = file.readlines()

# Add content to PDF
pdf.set_font("Arial", size=12)
for line in content:
    pdf.multi_cell(0, 8, line)

# Save PDF
pdf.output("Task_3_Report.pdf")

print("✅ Task 3 PDF Report Generated Successfully!")
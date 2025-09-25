from fpdf import FPDF

text = """
SERVICE AGREEMENT

This Service Agreement (“Agreement”) is made and entered into as of January 1, 2025, by and between ABC Solutions, Inc. (“Provider”) and XYZ Enterprises LLC (“Client”). The parties agree as follows:

1. Scope of Services. Provider agrees to perform software development, maintenance, and support services (“Services”) as requested by Client during the term of this Agreement.

2. Term. The initial term of this Agreement shall be one (1) year from the effective date and may be renewed upon mutual written agreement.

3. Payment. Client shall pay Provider a total fee of $50,000, payable in quarterly installments. Late payments shall incur a 2% interest per month on overdue amounts.

4. Confidentiality. Both parties agree to keep all proprietary information confidential and not disclose it to any third party without prior written consent, except as required by law.

5. Termination. Either party may terminate this Agreement upon thirty (30) days’ written notice. Upon termination, Client shall pay for all Services performed up to the termination date.

6. Liability. Provider’s liability shall be limited to direct damages not exceeding the total fees paid by Client under this Agreement. Neither party shall be liable for indirect, incidental, or consequential damages.

7. Governing Law. This Agreement shall be governed by and construed in accordance with the laws of the State of California, without regard to its conflict of law principles.

IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first written above.

ABC Solutions, Inc.                    XYZ Enterprises LLC
By: ____________________               By: ____________________
Name: John Doe                         Name: Jane Smith
Title: CEO                             Title: COO
"""


pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

for line in text.split("\n"):
    pdf.multi_cell(0, 7, line)

pdf.output("sample_contract.pdf")
print("✅ PDF Created: sample_contract.pdf")

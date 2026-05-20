import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
 # Create a dummy sales_data.csv file for demonstration
sample_data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Sales': [150, 200, 100, 250]
}
sample_df = pd.DataFrame(sample_data)
sample_df.to_csv('sales_data.csv', index=False)
 # Read CSV data
file_path = 'sales_data.csv'
data = pd.read_csv(file_path)
 # Display data
print("Sales Data:")
print(data)
   # Calculate total sales
total_sales = data['Sales'].sum()
print("\nTotal Sales:", total_sales)
    # Create bar chart
plt.figure(figsize=(6, 4))
plt.bar(data['Product'], data['Sales'])
plt.xlabel('Products')
plt.ylabel('Sales Amount')
plt.title('Sales Report')
plt.savefig('sales_chart.png')
plt.close()
     # Create PDF report
pdf = SimpleDocTemplate("Automated_Report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
content = []
     # Add title
content.append(Paragraph("Automated Report Generation Using Python", styles['Title']))
content.append(Spacer(1, 12))
      # Add report information
report_text = f"Total Sales Amount: {total_sales}"
content.append(Paragraph(report_text, styles['BodyText']))
content.append(Spacer(1, 12))
# Add chart image
content.append(Image('sales_chart.png', width=400, height=250))
       # Build PDF
pdf.build(content)
print("\nPDF Report Generated Successfully")

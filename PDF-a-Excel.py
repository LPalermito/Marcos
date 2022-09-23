# Import the required Module
import tabula
# Read a PDF File
df = tabula.read_pdf("F:\ProyectosVS\Marcos\SIX.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("SIX.pdf", "iplmatch.csv", output_format="csv", pages='all')
print(df)


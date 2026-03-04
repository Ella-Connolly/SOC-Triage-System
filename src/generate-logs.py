import csv
import pprint
from socfaker import SocFaker

sc = SocFaker()

header = ['Summary', 'Signature', 'Timestamp', 'Type', 'Status', 'Direction', 'Location']

alert_data = []
for _ in range(10):
    row = [
         sc.alert.summary, 
         sc.alert.signature_name, 
         sc.timestamp.current,
         sc.alert.type,
         sc.alert.status,
         sc.alert.direction,
         sc.alert.location
    ]
    alert_data.append(row)

#pprint(alert)

with open("alert.csv", "w", encoding="UTF-8", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
    csv_writer.writerows(alert_data)

print("alert.csv generated successfully.")

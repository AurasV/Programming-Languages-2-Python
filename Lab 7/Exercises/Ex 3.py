name = ["Alex", "Emma", "Kate", "Ryan", "Lily"]
age = [21, 25, 36, 31, 27]

with open("Table.html", "w") as f:
    f.write("<html><body><table><tr><th>Name</th><th>Age</th></tr>")

    for i in range(len(name)):
        f.write("<tr><td>{}</td><td>{}</td></tr>".format(name[i], age[i]))

    f.write("</table></body></html>")

"""
Module of parser database to reportlab format.
"""

def parse_line_format(line):
    """
    Transform a database line to table line as our requeriment output
    """
    def parse_date(datetime):
        return datetime.strftime("%d/%m/%Y")

    def parse_value(value):
        return "R$ {:0.2f}".format(value)

    return [line[0], parse_date(line[1]), parse_date(line[2]), line[3], line[4], parse_value(line[5])]


def list_to_table_format(dblist):
    """
    This function receive a list as parameter and output it as a table format
    with lines parsed as our requirements.
    """
    parsed_table = [
                    ["Placa", "Data", "Data", "Código", "Desb", "Valor",
                     "Placa", "Data", "Data", "Código", "Desb", "Valor"]
                   ]

    for index in range(0, len(dblist), 2):
        # we loop in range length of our data with pass as 2

        try:
            # Merges two index of our big list in one line
            composite = parse_line_format(dblist[index]) + parse_line_format(dblist[index + 1])
        except IndexError:
            composite = final_data[index]

        # composite is our big line
        parsed_table.append(composite)

    return parsed_table

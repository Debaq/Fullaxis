from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def create_answer_sheet_pdf(filename, title, num_questions, num_alternatives, columns=2):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []

    # Calcular el número de filas necesarias
    rows = -(-num_questions // columns)  # División entera redondeada hacia arriba

    # Crear tabla de alternativas
    data = [[""] * (columns * (num_alternatives + ) - 1) for _ in range(rows)]
    print(data)

    for r in range(num_questions):
        row = r % rows
        column = r // rows
        question_number = row + (rows * column) + 1 #numero de la pregunta
        data[row][column * (num_alternatives + 2)] = f"{question_number}."
        for c in range(num_alternatives):
            data[row][(column * (num_alternatives + 2)) + c + 1] = chr(ord("A") + c)

    # Crear tabla
    table = Table(data)
    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )
    )

    # Marcas guías en los bordes
    table.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 1, colors.black),
                ("LINEABOVE", (0, 0), (-1, -1), 1, colors.black),
                ("LINEBEFORE", (0, 0), (-1, -1), 1, colors.black),
                ("LINEAFTER", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
    )

    # Encabezado
    header_data = [
        [title, ""],
        ["RUT: ____________-_", ""],
    ]

    header = Table(header_data, colWidths=[doc.width / 2] * 2)
    header.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )
    )

    elements.append(header)
    elements.append(table)
    doc.build(elements)

if __name__ == "__main__":
    create_answer_sheet_pdf("hoja_de_respuestas.pdf", "Evaluación I, ETMP162", num_questions=55, num_alternatives=5)

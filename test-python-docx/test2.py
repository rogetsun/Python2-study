# coding:utf-8
__author__ = 'uv2sun'


style_footer = "DarkList"
style_red = "ColorfulList"
style_yellow = "LightShading"
style_green = "MediumShading2-Accent6"
style_transperent = "TableNormal"



for a,rec in enumerate(data):
    #V headinh se piše prvo polje iz table heada
    document.add_heading(rec['tableHead'][0][0], level=1)
    image_path = imageFolder + "\\" + slike[a]
    document.add_picture(image_path, height=Inches(3.5))

    #y += 28
    #worksheet.insert_image( y, 1,imageFolder + "/" + slike[a])


    for i, head in enumerate(rec['tableHead']):
        table = document.add_table(rows=1, cols = len(head))
        hdr_cells = table.rows[0].cells
        for a in range(0,len(head)):
            hdr_cells[a].text = head[a]


    for a,body in enumerate(rec['tableData']):
        row_cells = table.add_row().cells

        for a in range(0,len(body)):
            if body[a]['style'] == 'footer':
                stil = style_footer
            elif body[a]['style'] == 'red':
                stil = style_red

            elif body[a]['style'] == 'yellow':
                stil = style_yellow
            elif body[a]['style'] == 'green':
                stil = style_green

            else:
                stil = style_transperent

            row_cells[a].add_paragraph(body[a]['value'], stil)

document.save(wordDoc)
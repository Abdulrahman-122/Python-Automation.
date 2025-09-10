# Writing Word Documents:
import docx

doc = docx.Document()
doc.add_paragraph("Hello man!")
para2 = doc.add_paragraph("This is a second paragraph.")
para3 = doc.add_paragraph("This is the third paragraph.")
para3.add_run("This text will be added to the end of third paragraph")
para3.add_run("This new text will be added to the third text")
doc.save("Hello.docx")

# save() save the additional text you added to the docx file


import docx

doc = docx.Document()
doc.add_paragraph("Hello man!")
para2 = doc.add_paragraph("This is a second paragraph.")
para3 = doc.add_paragraph("This is the third paragraph.")
para3.add_run("This text will be added to the end of third paragraph")
para3.add_run("This new text will be added to the third text")
doc.add_paragraph(
    "Hello world", "Title"
)  # using Title for add this text as title section

doc.save("Hello.docx")

# use add_paragraph to make a title by text in it : doc.paragraph(text,'Title')


# Add Heading;
# add_heading() used to add heading to your docx
# this method take: text + integer(level of heading)
#
#
import docx

doc = docx.Document()
doc.add_heading("Header 0", level=0)
doc.add_heading("Header1", level=1)
doc.add_heading("Header 2", level=2)
doc.add_heading("Heading3", level=3)
doc.add_heading("Header4", level=4)

doc.save("Heading.docx")


# the most big heading who with level 0
# the least small heading who with level 4


# Adding line and Page Breaks:
import docx
from docx.text.run import WD_BREAK
doc=docx.Document()
para1=doc.add_paragraph('This is the first paragraph.')
run1=para1.add_run('this is tends to the first paragraph.')
run1.add_break(WD_BREAK.LINE)
para1.add_run('This is belongs to the para1.')

para2=doc.add_paragraph('This is the second Paragraph in this page')

# doc.paragraphs[1].runs[-1].add_break(WD_BREAK.PAGE)
para2.add_run('The last run in this page').add_break(WD_BREAK.PAGE)

doc.add_paragraph('the first paragraph in the second page.')

doc.save('Break(line&page).docx')
#Adding Pictures:
import docx
from docx.text.run import WD_BREAK
doc=docx.Document()
doc.add_picture('download(4).png', width=docx.shared.Inches(10),height=docx.shared.Inches(10))
doc.save('Image.docx')

#
#using add_picture(filename,height,width) to add anypicture to the docx
#using with 
#height=docx.shared.Inches(value)
#width=docx.shared.Cm(value)


# Practice Questions;
# 1.I passed to it the file object
# 2.for PdfFileREader -> I use 'rb' read binary
# with PdfFileWriter -> I use 'wb' write binary
# 3. reader=PdfReader(filename)
# reader.pages[4]
# 4.(.pages store the nums of pages) 
# 5. I should make decrypt for it by using : reader.decrypt(user_password)
# 6. .rotate(degree(90 or 180 or 270 or -90))
# 7.Document
# 8 paragraph obj contain on list of paragraphs in the doc
# while run obj contain on list of runs in each paragraph
# paragraph=docx.Document(filename)
# 9.two types of objects can hold these (paragraph,run)
# 10. if you put bold: true -> enable this style to the object
# if bold:False => disable this style to the object
# if bold:None -> save  the default style to the object no change
# 11.doc=docx.document()
# doc.save(newfile.docx)
# 12.doc.add_paragraph('Hello there !')
# 14. integers in word from 0 to 4 to represent level of heading in word documents



# Creating Word Documents with NOndefault styles:
# to create a new styles
# go to word -> newstyles
# make your style
# name it
# open the word docs on vSC  and use the name of it

# Run Attributes:
# to use Run attributes you need to give eachone a value
# 1.True -> the attribute is enabled
# 2.False -> the attribute is disabled
# 3.None -> Defaults to whatever the run's style is set to.
# :it's attributes:
# bold -> make text bold
# italic -> make the text italic
# underline -> the text is underlined
# strike -> the text has a strike through
# double_strike -> text appears with double strike through
# all_caps -> text appear all in capital letters
# small_caps -> text has capital letters and small letters
# shadow -> text has a shadow through him
# outline -> text appears  outlined rather than solid
# rtl -> text is written right to left
# imprint -> text appears pressed into the page
# emboss -> text appears raised off the page in relief.
#

# import docx

# doc = docx.Document("demo.docx")
# print(doc.paragraphs)  # as you see return list of paragraph objects
# print(doc.paragraphs[1])  # return the first paragraph object
# print(doc.paragraphs[0].text)
# print(doc.paragraphs[0].style.name)  # return the name of style in paragraph zero
# doc.paragraphs[0].style = "Normal"
# print(doc.paragraphs[0].style.name)
# print(doc.paragraphs[0].text)

# runs = doc.paragraphs[1].runs
# #print(runs)  # show you the list of runs object
# print(runs[0].text,runs[1].text,runs[2].text,runs[3].text,runs[4].tex t)
# runs[0].style='QuoteChar'
# runs[1].underline=True
# runs[2].underline=True
# runs[3].underline=True
# runs[4].underline=True
# doc.save('restyled.docx')

# let's see How to add new text into a word with these attributes:
# import docx

# doc = docx.Document()
# doc.add_heading("Add attributes to the Word", level=0)
# para = doc.add_paragraph("")
# run1 = para.add_run("Bold\n")
# run1.bold = True
# run2 = para.add_run("italic \n")
# run2.italic = True
# run3 = para.add_run("underline\n")
# run3.strike = True
# run4 = para.add_run("DoubleStrike\n")
# run4.double_strike = True
# run5 = para.add_run("All Caps\n")
# run5.all_caps = True
# run6 = para.add_run("small_caps\n")
# run6.small_caps = True
# r8 = para.add_run("Shadow\n ")
# r8.shadow = True

# r9 = para.add_run("Outline\n")
# r9.outline = True

# r10 = para.add_run("Right-to-Left \n")
# r10.rtl = True  # works best with Arabic/Hebrew text

# r11 = para.add_run("Imprint \n")
# r11.imprint = True

# r12 = para.add_run("Emboss\n")
# r12.emboss = True
# doc.save("Stayled.docx")
# print("File created successfully")


# import docx

# doc = docx.Document()
# doc.add_heading("Add attributes to the Word", level=0)
# para = doc.add_paragraph("")

# run1 = para.add_run("Bold\n")
# run1.bold = True

# run2 = para.add_run("Italic\n")
# run2.italic = True

# run3 = para.add_run("Underline\n")
# run3.underline = True


# run5 = para.add_run("Double Strike\n")
# run5.double_strike = True

# run6 = para.add_run("All Caps\n")
# run6.all_caps = True

# run7 = para.add_run("Small Caps\n")
# run7.small_caps = True

# run8 = para.add_run("Shadow\n")
# run8.shadow = True

# run9 = para.add_run("Outline\n")
# run9.outline = True

# run10 = para.add_run("Right-to-Left\n")
# run10.rtl = True  # works best with Arabic/Hebrew text

# run11 = para.add_run("Imprint\n")
# run11.imprint = True

# run12 = para.add_run("Emboss\n")
# run12.emboss = True

# doc.save("Styled3.docx")
# print("File created successfully")


# you change the style of paragraph from Title (which is bold and centered , big) to Normal(which is plain text(like default text))
#
import docx

doc = docx.Document("Stayled.docx")
runs = doc.paragraphs[1].runs
print(runs[1].text)
runs[1].bold=True
doc.save('StyledUpdate.docx')
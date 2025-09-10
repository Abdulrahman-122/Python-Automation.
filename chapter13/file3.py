# Word Documents:
# python uses: python-docx as module with word  and you import docx not python-docx
# import docx

#
# word files: anyfiles that ends with .docx
# it has alot of structures:
# Document object rperesent the entire document
# Documnet object contains a list of paragraph objects for the paragraphs in the document
#
# New paragraph begins when the user press Enter or Return when typing in a word document
#
# Each of these paragraph objects contains a list of one or more Run objects.
#
# ex:
# Aplain paragraph with some bold and some italic.(this sentence contain on four runs)
# the list of run objects here
# 1.Aplain paragraph with some
# 2.bold
# 3.and some
# 4.italic
# note:
# text in word document has more than one style (it has font,size,color,...)
# style in word:is a collection of these attributes(fonts,size,color,.....)
#
# Run object: is a contiguous(connected) run of text with the same style
#
# New Run object is needed when the text style changed
#


# Reading Word Documens
# import docx
# doc=docx.Document('demo.docx')
# print(len(doc.paragraphs))   # return the num of paragraphs
# #see the text in the docx
# print(doc.paragraphs[0].text)
# print(doc.paragraphs[1].text)
# print(doc.paragraphs[2].text)
# print(doc.paragraphs[3].text)
# print(doc.paragraphs[4].text)
# print(doc.paragraphs[5].text)
# print(doc.paragraphs[6].text)
# #see the Run object in the second text
# print(len(doc.paragraphs[1].runs))
# print(doc.paragraphs[1].runs[0].text)
# print(doc.paragraphs[1].runs[1].text)
# print(doc.paragraphs[1].runs[2].text)
# print(doc.paragraphs[1].runs[3].text)
# print(doc.paragraphs[1].runs[4].text)


#
# paragraphs -> contain on the list of paragraph objects
# it has a text attribute which contain on the string of that paragraph
# also paragraph has a run attribute which tell us the number of run objects in that text
# this run object change as the style change at the text
# we have 5 runs in the second text
# A plain text with (the first style with)
# some (second style)
# bold(third)
# and some(fourth)
# italic(fifth)

# Getting the full Text from a .docx file
# import docx


# def get_text(filename):
#     doc = docx.Document(filename)
#     fullText = []
#     for par in doc.paragraphs:
#         fullText.append(par.text)
#     return "\n".join(fullText)

#Styling paragraph and Run objects:
#in word there are three types of styles:
#paragraph styles can be applied to paragraph objects
#character styles can be applited to run objects
#linked styles can be applied to both types of objects
# 
# to give paragraph and run objects a style:
# setting their style object to a string
# the string should be the name of the style 
# if name is none -> this means no style applied with paragraph or Run objects
# 
# 
#to set a style name;
# don't put a spaces in it  as the word may misread it 
# 
# when using a linked style for a run object -> you all add a char at the end of it's name
# 
# ex: to add a Quote  to linked style -> with paragraph -> paragrphObj.style='Quote'
# for Run object -> runObj.style='QuoteChar'


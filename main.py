import PyPDF2
import gtts

# The PDF you want to convert to audio should be in the same directory

# Enter name of file with the extension (file.pdf)
file_name = input("Enter the name of the file you want to read: ")

# Open the PDF
with open(file=file_name, mode="rb") as file, open(file="book.txt", mode="w") as book_txt:
    # Read the file
    pdf_reader = PyPDF2.PdfReader(file)
    # Get the text from every page
    for i in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[i]
        page_text = page.extract_text()
        # Write the text into the new text file
        book_txt.write(page_text)

# Read from the new text file and convert to speech
with open(file="book.txt", mode="r") as book_txt:
    audio = gtts.gTTS(text=book_txt.read())
    audio.save(f"{file_name.split('.')[0]}.mp3")

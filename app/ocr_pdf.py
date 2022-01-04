import os
import sys
from pdf2image import convert_from_path
import glob
import cv2
import pytesseract
import shutil

INPUT_DIR_ARG = "--input-dir="
OUTPUT_DIR_ARG = "--output-dir="


def readArguments(INPUT_DIR_ARG, OUTPUT_DIR_ARG):
    input_dir = "./"
    output_dir = "./"
    if(len(sys.argv) > 1):
        for i in range(1, len(sys.argv)):
            arg = sys.argv[i]
            if(arg.startswith(INPUT_DIR_ARG) == True):
                input_dir = arg[len(INPUT_DIR_ARG):]
            elif(arg.startswith(OUTPUT_DIR_ARG) == True):
                output_dir = arg[len(OUTPUT_DIR_ARG):]

    file_names = glob.glob(input_dir + "/*.pdf")
    return input_dir, output_dir, file_names


def processFile(input_dir, output_dir, pdf_source_file):
    pdf_name = pdf_source_file[len(input_dir)+1:-4]
    print(pdf_name)
    output_file_dir = output_dir + "/" + pdf_name
    if os.path.isdir(output_file_dir) == False:
        os.mkdir(output_file_dir)

    pages = convert_from_path(pdf_source_file, 300)

    num_pages = pagesToImages(output_file_dir, pages)

    output_file = open(os.path.join(output_file_dir, pdf_name + ".txt"), "a")
    appendTextFromImagePagesToTxtFile(output_file_dir, num_pages, output_file)
    output_file.close()
    shutil.move(pdf_source_file, output_file_dir + "/" + pdf_name + ".pdf")


def appendTextFromImagePagesToTxtFile(output_file_dir, num_pages, output_file):
    for page_num in range(0, num_pages):
        img_file = os.path.join(output_file_dir, "p"+str(page_num)+".png")
        temp_name = img_file.replace("/", ".")
        text_filename = temp_name.split(".")[1]
        img = cv2.imread(img_file)
        converted_text = pytesseract.image_to_string(img)
        output_file.write(converted_text)
        output_file.write("\n<-- pag {} -->\n".format(page_num + 1))
        os.remove(img_file)


def pagesToImages(output_file_dir, pages):
    last_page = 0
    for page_num, page in enumerate(pages):
        filename = os.path.join(output_file_dir, "p"+str(page_num)+".png")
        page.save(filename, 'PNG')
        last_page += 1
    return last_page


input_dir, output_dir, file_names = readArguments(
    INPUT_DIR_ARG, OUTPUT_DIR_ARG)

for pdf_source_file in file_names:
    processFile(input_dir, output_dir, pdf_source_file)

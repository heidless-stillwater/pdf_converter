from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os
from constants import *
#
#
# PDF_FILES = './pdf_files'
# PDF_IMG_DIR = './pdf_files/pdf_images'

NOTHING_SELECTED = 'NOTHING_SELECTED'


class PdfToolbox:

    def __init__(self):
        self.dir_listing = self.list_pdf_dir()
        # print(f'in PdfToolbox dir_listing: {self.dir_listing}')

    def list_pdf_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir('pdf_files') if os.path.isfile(os.path.join('pdf_files', f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'listing: {listing}')
        return listing

    def list_pages_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(PAGES_DIR) if os.path.isfile(os.path.join(PAGES_DIR, f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'listing: {listing}')
        return listing

    def list_images_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(PDF_IMG_DIR) if os.path.isfile(os.path.join(PDF_IMG_DIR, f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        print(f'images listing: {listing}')
        return listing

    def list_combo_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(COMBO_DIR) if os.path.isfile(os.path.join(COMBO_DIR, f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'listing: {listing}')
        return listing

    def split_combo_pdf_into_pages(self, pdf_file, name_of_split):
        print(f'split_pdf_into_pages:pdf_file: {pdf_file}')
        pdf_path = f'{COMBO_DIR}/{pdf_file}'
        print(f'pdf_path: {pdf_path}')
        with open(pdf_path, 'rb') as f:
            print(f'0: opening file')
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
            print(f'x: number_of_pages: {number_of_pages}')

            for page in range(number_of_pages):
                print(f'1:processing page: {page}')
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf.getPage(page))

                output = f'{COMBO_PAGES_DIR}/{name_of_split}{page}.pdf'
                print(f'split_pdf_into_pages:output: {output}')

                with open(output, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)

    def split_pdf_into_pages(self, in_dir, pdf_file, name_of_split):
        print(f'split_pdf_into_pages:pdf_path: {pdf_file}')
        pdf_path = f'{in_dir}/{pdf_file}'
        print(f'pdf_path: {pdf_path}')
        with open(pdf_path, 'rb') as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()

            for page in range(number_of_pages):
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf.getPage(page))

                output = f'{PAGES_DIR}/{name_of_split}{page}.pdf'
                print(f'output: {output}')
                print(f'split_pdf_into_pages:output: {output}')

                with open(output, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)

    def extract_information(self, pdf_file):
        # print(f'pdf_t:extract_information')
        pdf_path = f'{PDF_FILES}/{pdf_file}'
        # print(f'extract_information:pdf_path: {pdf_path}')
        if pdf_path == NOTHING_SELECTED:
            information = pdf_path
        else:
            with open(pdf_path, 'rb') as f:
                pdf = PdfFileReader(f)
                information = pdf.getDocumentInfo()
                number_of_pages = pdf.getNumPages()

            txt = f"""
            Information about {pdf_path}:
    
            Author: {information.author}
            Creator: {information.creator}
            Producer: {information.producer}
            Subject: {information.subject}
            Title: {information.title}
            Number of pages: {number_of_pages}
            """
            information = txt
            # print(txt)
        return information

    def merge_files(self, m_lst, o_file):

        merger = PdfFileMerger()
        listing = m_lst

        for pdf in listing:
            pdf = f'{PAGES_DIR}/{pdf}'
            merger.append(pdf)

        merger.write(f"{COMBO_DIR}/{o_file}")
        merger.close()

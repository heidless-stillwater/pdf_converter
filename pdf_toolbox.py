from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os

PDF_FILES = './pdf_files'
PDF_PAGES = './pdf_files/pdf_pages'
PDF_COMBO = './pdf_files/pdf_combo'

NOTHING_SELECTED = 'NOTHING_SELECTED'


class PdfToolbox:

    def __init__(self):
        self.dir_listing = self.list_pdf_dir()
        # print(f'in PdfToolbox dir_listing: {self.dir_listing}')

    def split_pdf_into_pages(self, pdf_file, name_of_split):
        # print(f'split_pdf_into_pages:pdf_path: {pdf_file}')
        pdf_path = f'{PDF_FILES}/{pdf_file}'
        with open(pdf_path, 'rb') as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()

            for page in range(number_of_pages):
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf.getPage(page))

                output = f'{PDF_PAGES}/{name_of_split}{page}.pdf'
                print(f'split_pdf_into_pages:output: {output}')

                with open(output, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)

    def merge_files(self, m_lst, o_file):

        merger = PdfFileMerger()
        listing = m_lst

        for pdf in listing:
            pdf = f'{PDF_PAGES}/{pdf}'
            merger.append(pdf)

        merger.write(f"{PDF_COMBO}/{o_file}")
        merger.close()

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
        dir_contents = [f for f in os.listdir(PDF_PAGES) if os.path.isfile(os.path.join(PDF_PAGES, f))]
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

    def list_combo_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(PDF_COMBO) if os.path.isfile(os.path.join(PDF_COMBO, f))]
        print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

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

import os
import pdfplumber


def extract_text_with_pdfplumber(folder_path, output_file):

    if not os.path.exists(folder_path):
        print(f"Ошибка: Папка {folder_path} не существует!")
        return

    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("В указанной папке не найдено PDF-файлов!")
        return

    print(f"Найдено PDF-файлов: {len(pdf_files)}")

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for pdf_file in pdf_files:
            pdf_path = os.path.join(folder_path, pdf_file)

            try:
                print(f"Обрабатывается файл: {pdf_file}")

                with pdfplumber.open(pdf_path) as pdf:
                    out_file.write(f"=== Файл: {pdf_file} ===\n")

                    for page_num, page in enumerate(pdf.pages):
                        text = page.extract_text()

                        if text:
                            out_file.write(f"\n--- Страница {page_num + 1} ---\n")
                            out_file.write(text)
                            out_file.write("\n")

                    out_file.write("\n" + "=" * 50 + "\n\n")

                print(f"Файл {pdf_file} успешно обработан!")

            except Exception as e:
                print(f"Ошибка при обработке файла {pdf_file}: {str(e)}")
                out_file.write(f"!!! Ошибка при обработке файла {pdf_file}: {str(e)} !!!\n\n")

    print(f"Готово! Текст сохранен в файл: {output_file}")

folder_path = r"C:\Users\Strelitzia2810\Downloads"
output_file = os.path.join(folder_path, "textfromPDF.txt")
extract_text_with_pdfplumber(folder_path, output_file)
import os

# loon funktsiooni, mis kontrollib kas fail on .jpeg, lugedes headerist 2 esimest bitti
def picture(file_path):
    with open(file_path, 'rb') as file:
        header = file.read(2)
        return header == b'\xFF\xD8'

# määran directory, kus asuvad failid aka random_files
directory = 'C:\\Users\\TarvoHeinroos\\PycharmProjects\\scriptinglanguages\\searching-for-jpeg-files-TarvoH\\random_files'

# kontrollin igat faili directory's ning kui on .JPEG siis prindin välja, vastasel juhul kustutan
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path):
        if picture(file_path):
            print(f'{file} is picture')
        else:
            os.remove(file_path)
            print(f'{file} not picture aka deleted')

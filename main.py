import difflib
import random
import os
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Mengecek Quotes
def delete_similar_quotes(file_path):
    with open(file_path, 'r') as f:
        quotes = f.readlines()
        
    deleted_count = 0
        
    for i in range(len(quotes)):
        for j in range(i+1, len(quotes)):
            seq = difflib.SequenceMatcher(None, quotes[i], quotes[j])
            ratio = seq.ratio()
            
            if ratio > 0.7 and ratio < 0.99:
                if len(quotes[i]) > len(quotes[j]):
                    del quotes[i]
                else:
                    del quotes[j]
                deleted_count += 1
                break
                
    with open(file_path, 'w') as f:
        f.writelines(quotes)
        
    if deleted_count > 0:
        print(f"{deleted_count} quotes yang mirip telah dihapus.")
    else:
        print("Tidak ada quotes yang mirip dihapus.")

delete_similar_quotes('quotes/sedih.txt')

time.sleep(2)

# Memilih 1 Quote
def move_random_quote(source_file_path, target_file_path):
    # Read quotes from source file
    with open(source_file_path, 'r') as f:
        quotes = f.readlines()

    # Choose a random quote
    random_index = random.randrange(len(quotes))
    random_quote = quotes[random_index]

    # Write the random quote to the target file
    with open(target_file_path, 'a') as f:
        f.write(random_quote)

    # Remove the random quote from the source file
    with open(source_file_path, 'w') as f:
        quotes.pop(random_index)
        f.writelines(quotes)

    print(f"Quote acak telah dipindahkan ke {target_file_path} dan dihapus dari {source_file_path}.")

move_random_quote('quotes/sedih.txt', 'quotes/edit.txt')

time.sleep(2)

# Memberikan Random New Line "\n"
def add_random_newline(file_path, n=2):
    # Read the content of the file
    with open(file_path, 'r') as f:
        content = f.read()

    # Add random newline characters to a random sentence
    sentences = content.split('. ')
    random_sentence_index = random.randrange(len(sentences))
    sentence = sentences[random_sentence_index].strip()

    # Split the sentence into words
    words = sentence.split(' ')

    # Add newline characters randomly to the sentence
    new_sentence = ''
    for i, word in enumerate(words):
        new_sentence += word
        if i < len(words) - 3 and random.random() < 0.4:
            new_sentence += '\n'
        else:
            new_sentence += ' '
    
    # Print the original and modified sentences
    print(f'Original sentence: {sentence}')
    print(f'Modified sentence: {new_sentence}\n')

    # Write the modified content to the file
    with open(file_path, 'w') as f:
        content = content.replace(sentence, new_sentence, 1)
        f.write(content)

add_random_newline('quotes/edit.txt')

time.sleep(2)

#Mengedit Gambar

# Membuka file gambar base.jpg
img = Image.open('images/base.jpg')

# Membuat objek ImageDraw untuk menggambar pada gambar
draw = ImageDraw.Draw(img)

# Mendapatkan ukuran gambar
width, height = img.size

# Membuat objek font Helvetica dengan ukuran 50
font = ImageFont.truetype("font/Helvetica.ttf", 40)

# Membuka file /quotes/edit.txt dan membaca teks dari file
with open('quotes/edit.txt', 'r') as f:
    text = f.read() #.replace('\n', '')  # Menghapus karakter newline jika ada

# Mendapatkan ukuran teks
text_width, text_height = draw.textsize(text, font)

# Menghitung posisi X dan Y untuk menempatkan teks di tengah gambar
x = (width - text_width) / 2
y = (height - text_height) / 2

# Menambahkan teks ke dalam gambar pada posisi yang telah dihitung dan dengan warna hitam
draw.text((x, y), text, font=font, fill=(0,0,0))

# Menyimpan gambar
img.save('images/hasil.jpg')
print("Foto Berhasil Diedit!")

time.sleep(2)

#Menghapus Quote
with open('quotes/edit.txt', 'w') as f:
    f.write('')

print("Semua Proses Telah Selesai!")
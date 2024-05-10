import exifread

with open('Fujifilm_FinePix_E500.jpg', 'rb') as f:
    tags = exifread.process_file(f)

print(tags)
from simple_image_download import simple_image_download as sim

my_downloader = sim.Downloader()

my_downloader.directory = 'my_dir/'
# Change File extension type
my_downloader.extensions = '.jpeg'
print(my_downloader.extensions)

my_downloader.download('parrot', limit=100)
my_downloader.download('pigeon', limit=100)
#my_downloader.download('bananas', limit=100)
#my_downloader.download('mangoes', limit=100)
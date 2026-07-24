import sys

from .youtube_to_csv import YoutubeToCSV

def main():
    config_file_yml = 'config.yml'
    if len(sys.argv) > 1:
        config_file_yml = sys.argv[1]
    YoutubeToCSV(config_file_yml).run()

main()

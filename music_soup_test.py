import requests
import os
from bs4 import BeautifulSoup

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class MusicDownload:
    def __init__(self, url, folder_name):
        self.url = url
        self.name_list = []
        self.id_list = []
        self.url_name_class = "Q5txwe"
        self.url_name_attribute = "aria-label"
        self.url_id_class = "WYuW0e"
        self.url_id_attribute = "data-id"
        self.music_id = {folder_name: self.id_list}
        self.music_name = {folder_name: self.name_list}

    def get_music_name_id(self):
        URL = self.url
        page = requests.get(URL)
        # print(page.text)
        soup = BeautifulSoup(page.content, "html.parser")
        # print(soup)
        results = soup.find(id="drive_main_page")
        # print(results.prettify())
        job_elements_name = results.find_all("div", class_=self.url_name_class)
        for job_elements_name in job_elements_name:
            # title_music = results["div aria-label"]
            # print(job_elements, end="\n"*2)
            music_name = job_elements_name[self.url_name_attribute]
            self.name_list .append(music_name)
        job_elements_id = results.find_all("div", class_=self.url_id_class)
        for job_elements_id in job_elements_id:
            music_id = job_elements_id[self.url_id_attribute]
            self.id_list.append(music_id)

    def download_file_from_google_drive(self, id, destination):
        URL = "https://docs.google.com/uc?export=download"

        session = requests.Session()

        response = session.get(URL, params={'id': id}, stream=True)
        token = MusicDownload.get_confirm_token(self, response)

        if token:
            params = {'id': id, 'confirm': token}
            response = session.get(URL, params=params, stream=True)

        MusicDownload.save_response_content(self, response, destination)

    def get_confirm_token(self, response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(self, response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

    def download_music(self):

        for key, value in self.music_id.items():
            for x in range(0, len(value)):
                # print(x)
                folder = key
                file_id = value[x]
                song_name = self.music_name[key][x]
                print(folder, file_id, song_name)
                destination = CURR_DIR_PATH + "\\music" + folder + "\\" + song_name
                MusicDownload.download_file_from_google_drive(self, file_id, destination)


chapter_1 = MusicDownload("https://drive.google.com/drive/folders/1fIoMFPg_ZDl70WhZNahfi4T8x77OWZ_D", "\\chapter_1")
chapter_1.get_music_name_id()
chapter_1.download_music()

battle = MusicDownload("https://drive.google.com/drive/folders/192XFTaoDi-_J3JEuwUQo2Gn7h1Oi6Ndp", "\\battle")
battle.get_music_name_id()
battle.download_music()

for_all = MusicDownload("https://drive.google.com/drive/folders/1HxmHwk7k9eke-d3I7z8Z9L5eUsojPVk8", "\\For all")
for_all.get_music_name_id()
for_all.download_music()

main_intro = MusicDownload("https://drive.google.com/drive/folders/1ks6SIeVvzogLqqvTDARckj0pgQORDVHH", "\\main_intro")
main_intro.get_music_name_id()
main_intro.download_music()







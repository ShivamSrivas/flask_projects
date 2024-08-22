import os
import requests
from bs4 import BeautifulSoup as bs
from utilis.logger import logger
from urllib.request import urlopen as uReq

class Scrappy:
    def __init__(self, image_to_be_downloaded, number_of_images_to_be_downloaded):
        self.image_to_be_downloaded = image_to_be_downloaded
        self.number_of_images_to_be_downloaded = number_of_images_to_be_downloaded
        self.log_path = "logs/scrappy.log"
        logger(self.logs_path, 'info', 'Object initialized with Scrappy class')

    def download_images(self):
        logger(self.logs_path, 'info', 'download_images method called')
        image_downloaded_count = 0
        page_number = 1
        images_links = set()
        save_folder = 'static\images'
        os.makedirs(save_folder, exist_ok=True)

        try:
            while image_downloaded_count < self.number_of_images_to_be_downloaded:
                search_url = f"https://www.bing.com/images/search?q={self.image_to_be_downloaded}&form=HDRSC3&first={page_number}"
                uClient = uReq(search_url)
                uClient_html = bs(uClient.read(), "html.parser")
                uClient.close()
                images_link_tags = uClient_html.find_all("img", {'class': ('cimg', 'mimg', 'rms_img')})

                for img_tag in images_link_tags:
                    if image_downloaded_count >= self.number_of_images_to_be_downloaded:
                        break

                    img_url = img_tag.get('src') or img_tag.get('data-src')

                    if img_url and img_url.startswith('https') and img_url not in images_links:
                        images_links.add(img_url)
                        image_name = f"{self.image_to_be_downloaded}_{image_downloaded_count}.jpg"
                        image_path = os.path.join(save_folder, image_name)

                        try:
                            image = requests.get(img_url)
                            with open(image_path, 'wb') as file:
                                file.write(image.content)

                            image_downloaded_count += 1
                            print(f"Downloaded: {image_name}")
                        except Exception as e:
                            print(f"Error downloading {img_url}: {e}")

                page_number += 1
            logger(self.logs_path, 'info', 'download_images method ran successfully')
            return list(images_links)

        except Exception as error:
            logger(self.logs_path, 'error', f'download_images end up with an error saying {error}')
            return {"error": str(error)}

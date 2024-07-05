
from requests import post,get,delete
from loguru import logger
from env import BASEURL
import streamlit as st
import random
import string

def generate_boundary(length=16):
    characters = string.ascii_letters + string.digits + "-_"
    boundary = "".join(random.choice(characters) for _ in range(length))
    return boundary
class _HTTP:
    def __init__(self,baseurl=BASEURL):
        self.headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36 Edg/126.0.0.0"}
        self.base = baseurl
    def update_baseurl(self,baseurl):
        logger.info(f"Updating base url to {baseurl}")
        self.base = baseurl
    def json_post(self,url,data):
        try:
            logger.info(f"Posting to {url} with data: {data}")
            p = post(self.base+url,json=data,headers=self.headers)
            logger.info(f"Posting to {url} with data: {data} RAW:{p.request.body}")
            logger.info(f"Posting response: {p.text}")
            return p
        except Exception as e:
            logger.error(f"Error posting to {url} with data: {data}")
            st.toast(f"Error posting to {url} with data: {data} {e}")
    def data_post(self,url,data):
        try:
            logger.info(f"Posting to {url} with data: {data}")
            p = post(self.base+url,data=data,headers=self.headers)
            logger.info(f"Posting response: {p.text}")
            return p
        except Exception as e:
            logger.error(f"Error posting to {url} with data: {data}")
            st.toast(f"Error posting to {url} with data: {data} {e}")
    def get(self,url):
        try:
            logger.info(f"Getting from {url}")
            p = get(self.base + url,headers=self.headers)
            logger.debug(f"Getting response {p.text}")
            return p
        except Exception as e:
            logger.error(f"Error getting from {url}")
            st.toast(f"Error getting from {url} {e}")
    def update_headers(self,headers:dict):
        logger.info(f"Updating headers to {headers}")
        self.headers.update(headers)
    def api_delete(self,url):
        r = delete(self.base+url,headers=self.headers)
        return r
    def upload_file(self,url:str,file:bytes,filename:str):

        r = post(self.base+url,files={"file":(filename, file)},headers=self.headers,allow_redirects=False)
        logger.info(f"status_code = {r.status_code}")
        if r.status_code == 301:
            new_url = r.headers['Location']
            r = post(new_url,files={"file":(filename, file)},headers=self.headers,allow_redirects=False)
        logger.info(f"Uploading file to {url} with data: {r.text}, headers={self.headers}")
        return r
    def upload_image_file(self,url,body:bytes,file_ext:str):
        file_type = "image/png"
        if file_ext not in ["png","jpg"]:
            raise Exception("Only png and jpg files are supported")
        if file_ext == "png":
            file_type = "image/png"
        elif file_ext == "jpg":
            file_type = "image/jpeg"
        elif file_ext == "jpeg":
            file_type = "image/jpeg"
        elif file_ext == "gif":
            file_type = "image/gif"
        elif file_ext == "webp":
            file_type = "image/webp"
        elif file_ext == "svg":
            file_type = "image/svg+xml"
        else:
            raise Exception("Unsupported file type")
        boundary = generate_boundary()
        header = {
            "Content-Type": f"multipart/form-data; boundary={boundary}"
        }
        data = f"--{boundary}\r\n"
        data += f'Content-Disposition: form-data; name="file"; filename="file.{file_ext}"\r\n'
        data += f"Content-Type: image/{file_type}\r\n\r\n"
        import base64
        data += base64.b64encode(body).decode()
        data += f"\r\n--{boundary}--\r\n"
        header.update(self.headers)
        r = post(self.base+url,data=data,headers=header)
        return r
def _reverse_dict(original_dict):
    reversed_dict = {value: key for key, value in original_dict.items()}
    return reversed_dict

HTTP = _HTTP()
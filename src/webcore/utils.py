

from tortoise.models import Model
from pydantic import BaseModel
from conf import config
import pytz
from datetime import datetime,timezone
import socket
import struct
import aiohttp
import jwt
from os import path,walk


async def async_get(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        
def decrypt_jwt(token: str, key: str, algorithm: str):
    return jwt.decode(token, key, algorithms=algorithm)



def hex_to_ipv4(hex_ip:str)->str:
    # 确保输入为不带前缀的十六进制字符串
    hex_ip = hex_ip.replace('0x', '').replace('0X', '')
    # 将十六进制字符串转换为32位二进制打包格式
    packed_ip = struct.pack('!L', int(hex_ip, 16))
    # 将打包的二进制格式转换为点分十进制的IPv4地址
    ipv4_address = socket.inet_ntoa(packed_ip)
    return ipv4_address

def ipv4_to_hex(ip:str)->str:
    # 将点分十进制的IPv4地址转换为32位打包的二进制格式
    packed_ip = socket.inet_aton(ip)
    # 将打包的二进制格式转换为一个长整数
    unpacked_ip = struct.unpack("!L", packed_ip)[0]
    # 将长整数转换为十六进制字符串
    hex_ip = hex(unpacked_ip)[2:].zfill(8)  # 移除"0x"前缀并补足为8位
    return hex_ip.upper()


def get_current_time():
    try:
        timezone = pytz.timezone(config.GLOBAL_TIMEZONE)
        current_time = datetime.now(timezone)
        return current_time
    except pytz.UnknownTimeZoneError:
        return datetime.now()
    
def get_timezone():
    return pytz.timezone(config.GLOBAL_TIMEZONE)

def get_ip()->str:
    if config.APP_DEBUG:
        return "127.0.0.1"
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return str(ip_address)


def port_to_hex(port):
    # 确保端口号是一个有效的整数
    if 0 <= port <= 65535:
        # 将整数转换为十六进制字符串，并移除"0x"前缀
        hex_port = hex(port)[2:].upper()
        # 为了表示清晰，确保输出为4位十六进制数（即2个字节）
        hex_port = hex_port.zfill(4)
        return hex_port
    else:
        return "Invalid port number"
def hex_to_port(hex_port):
    try:
        # 将十六进制字符串转换为十进制整数
        port = int(hex_port, 16)
        return port
    except ValueError:
        return "Invalid hexadecimal port number"


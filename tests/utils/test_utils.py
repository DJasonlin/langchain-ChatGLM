import os
import datetime
import time

DEFAULT_PAGESIZE = 5


def list_docs_from_folder_by_page(page: int):
    doc_path = '/Users/jason/Downloads/done'
    # 获取目录下的所有文件
    files = os.listdir(doc_path)
    # 将文件按时间倒序排序
    files.sort(key=lambda x: datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(doc_path, x))),reverse=True)
    return files[DEFAULT_PAGESIZE * (page - 1):DEFAULT_PAGESIZE * page]

def list_docs_from_folder(kb_name: str):
    doc_path = '/Users/jason/Downloads/done'
    return [file for file in os.listdir(doc_path)
            if os.path.isfile(os.path.join(doc_path, file))][0:10]


if __name__ == '__main__':
    # print(list_docs_from_folder_by_page(1))
    starttime = datetime.datetime.now().timestamp()
    list = [1,2,3]
    time.sleep(3)
    i=1
    print("[{}]Processing completed-{}, waitting-{}, time cost-{} s".format(datetime.datetime.now(), i, (len(list) - i), int(datetime.datetime.now().timestamp() - starttime)))

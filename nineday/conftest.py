import json
import pytest


@pytest.fixture(scope="module")
def author_file_json(tmpdir_factory):
    python_data = {
        'linda': {'city': 'beijing'},
        'seven': {'city': 'nanji'},
        'nine': {'city': 'paris'}
    }
    # 创建一个临时目录data及下面author_file.json文件
    file = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file:{}'.format(str(file)))
    # 将 数据写入文件中
    with open(file, 'w') as f:
        json.dump(python_data, f)
    return file


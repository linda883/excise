

def test_tmpdir(tmpdir):
    # tmpdir是已经有的临时路径，通过join加上文件名，这是个临时文件。
    a_file = tmpdir.join("test_data.txt")
#     建立一个临时文件 夹
    a_sub_dir = tmpdir.mkdir("testdatafp")
#     可以在这个文件夹下建立一个文件
    another = a_sub_dir.join("file.txt")
    a_file.write("这是文件内容第一个")
    another.write("this is file contents second")
    assert a_file.read() == "这是文件内容第一个"
    assert another.read() == "this is file contents second"
    print(tmpdir.realpath)

# tmpdir_factory的作用范围是会话级别的。tmpdir是函数级别的。
def test_tmpdir_factory(tmpdir_factory):
    a_dir =tmpdir_factory.mktemp("mydir")
    print(tmpdir_factory.getbasetemp())


    # 可以使用pytest  -basetemp=mydir 指定自己的根目录


import wx

def printhelp(content_text):
    content_text.AppendText("usage:[help][daily][shot NAME]\n")
    content_text.AppendText("[help]--输出帮助\n")
    content_text.AppendText("[daily]--做每日（待做）\n")
    content_text.AppendText("[shot NAME]--截图，NAME为文件名称（无后缀）默认为png格式,存储位置程序文件夹\n")
    content_text.AppendText("[genshin resin]--去风本无脑清体力\n")
    content_text.AppendText("不同命令可以使用&分隔，会按照顺序执行\n")
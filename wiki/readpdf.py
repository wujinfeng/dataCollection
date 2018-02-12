from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter


# 获取文档对象. rb二进制模式
fp = open('naacl06-shinyama.pdf', 'rb')
# 创建解析器
parser = PDFParser(fp)
# PDF文档对象.
doc = PDFDocument()
# 连接解析器和文档对象.
parser.set_document(doc)
doc.set_parser(parser)
# Supply the password for initialization.
# (If no password is set, give an empty string.)
# 文档初始化
doc.initialize('')

# 创建资源管理器.
resource = PDFResourceManager()
# 创建参数分析器.
laparam = LAParams()
# 创建一个聚合器
device = PDFPageAggregator(resource, laparams=laparam)
# 创建页面解释器.
interpreter = PDFPageInterpreter(resource, device)
# Process each page contained in the document.
for page in doc.get_pages():
    # 页面解释器来读取
    interpreter.process_page(page)

    # 使用聚合器来获得内容
    layout = device.get_result()
    for out in layout:
        if hasattr(out, "get_text"):
            print(out.get_text())

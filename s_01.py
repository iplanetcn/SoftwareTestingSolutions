# 一、抓取百度首页全部链接，链接文字、链接URL地址，回填到Excel文件中
# 1. 抓取百度首页内容
# 2. 分析内部的链接文字、链接url
# 3. 操作excel-csv文件，并写入上一步骤2中，所得到的文字和url
import chardet
import requests
import csv
from bs4 import BeautifulSoup
import xlsxwriter

if __name__ == '__main__':
    # 1. 抓取百度首页内容
    url = "https://www.baidu.com"
    resp = requests.get(url)
    # 以下这两行以便python正确识别网页编码，以防乱码
    encoding = chardet.detect(resp.content)["encoding"]
    resp.encoding = encoding

    resp_text = resp.text
    print(resp_text)

    # 2. 分析内部的链接文字、链接url
    soup = BeautifulSoup(resp_text, 'html.parser')
    print("------soup.prettify()-----")
    all_links = soup.find_all('a')
    for a in all_links:
        print(a.attrs['href'])
        print(a.text)

    titles = ["链接文字", "链接URL"]

    # 3.操作excel-csv文件，并写入上一步骤2中，所得到的文字和url
    with open("s_01_result.csv", 'w') as f:
        write = csv.writer(f)
        # write.writerow(titles)
        for a in all_links:
            write.writerow([a.text, a.attrs['href']])

    # 4.（可选）写入Excel-xlsx文件
    workbook = xlsxwriter.Workbook('s_01_result.xlsx')
    worksheet = workbook.add_worksheet()
    # 操作行列
    col = 1
    for a in all_links:
        worksheet.write("A{}".format(col), a.text)
        worksheet.write("B{}".format(col), a.attrs['href'])
        col += 1
    workbook.close()

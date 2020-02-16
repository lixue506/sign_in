import datetime
import pymysql
import base64
import request
import openpyxl
import xlrd
import os


class Operator_Mysql():

    def Check_pwd(self,name,pwd):
        con = pymysql.connect("localhost", "root", "lixue123", "qiandao")
        cur = con.cursor()
        sql = "select * from user where name={} and pwd={}".format(name,pwd)
        cur.execute(sql)
        con.commit()
        con.close()

    def Read_file(self, path):
        # 打开excel文件,获取工作簿对象
        wb = openpyxl.load_workbook(path)
        # 从工作薄中获取一个表单(sheet)对象
        sheets = wb.sheetnames
        sheet0 = sheets[0]
        for i in sheets0:
            self.Save_data(i[0],[1],i[2])
 
    def Save_data(self,name,day,hour):
        con = pymysql.connect("localhost", "root", "lixue123", "qiandao")
        cur = con.cursor()
        sql = "insert into qiandao values ({},{},{})".format(name,day,hour)
        cur.execute(sql)
        con.commit()
        con.close()  

    def Query_data(self,start_time,end_time):
        con = pymysql.connect("localhost", "root", "lixue123", "test")
        cur = con.cursor()
        # 待更新
        sql = "select * from qiandao where ".format(start_time, end_time)
        cur.execute(sql)
        con.commit()
        cols = cur.fetchall() 
        con.close()
        return self.format_data(cols)

    def format_data(self, cols):
        query_dict = []
        for i in cols:
            d = {}
            d['name'] = i[0]
            d['time'] = i[1]
            d['hour'] = i[2]
            query_dict.append(d)
        return query_dict


import sys
import pymysql.cursors


class TransferMoney(object):
    def __init__(self):
        self.conn = conn

    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where accid=%s" % acctid
            cursor.execute(sql)
            print("check_acct_available:" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账户%s不存在" % acctid)
        finally:
            cursor.close()

    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where accid=%s and money>%s" % (acctid, money)
            cursor.execute(sql)
            print("has_enough_money:"+sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账户%s没有足够钱" % acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):
        pass

    def add_money(self, acctid, money):
        pass


if __name__ == "__main__":
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]

    conn = pymysql.connect(
        host="localhost",
        user="root",
        db="test",
        password="1234"
    )
    tr_money = TransferMoney()
    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print('出现问题：' + str(e))
    finally:
        conn.close()

import streamlit as st
from beem.steem import Steem
from beem.account import Account
#节点地址，这是我的节点
nodes = 'https://cn.steems.top'

def trans(nodes,password,player,toplayer,number,Token,memo):
    #加载密码和节点
    s = Steem(keys=[password],node=nodes)
    #加载账户
    account = Account(player,steem_instance=s)
    # 转账
    tx=account.transfer(toplayer,number, Token,memo)
    return tx




st.title("一个钱包")
player=st.text_input("请输入账号")
password=st.text_input("请输入密码",type="password")

toplayer = st.text_input('转到to')

Token=st.text_input('转账币种Token')
Token=Token.upper()

number=st.text_input('数量Number')
memo = st.text_input('备忘memo')

button_trans=st.button('提交')

if button_trans:
    tx = trans(nodes,password,player,toplayer,number,Token,memo)
    st.write(tx)







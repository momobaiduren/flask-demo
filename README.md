使用flask-sqlacodegen代码生成
    1.pip3 install flask-sqlacodegen
    2.cd 当前model保存的目录
    2.flask-sqlacodegen 'mysql+cymysql://root:zl12345@127.0.0.1/csx_b2b_settle' --tables statement_statement_account --outfile "Models.py"  --flask
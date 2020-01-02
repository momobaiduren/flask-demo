# # coding: utf-8
# from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.schema import FetchedValue
#
# Base = declarative_base()
# metadata = Base.metadata
#
#
# class StatementStatementAccount(Base):
#     __tablename__ = 'statement_statement_account'
#
#     id = Column(BigInteger, primary_key=True, info='主键')
#     statement_no = Column(String(32), nullable=False, info='对账单号')
#     check_ticket_no = Column(String(32), info='勾票单号')
#     statement_time = Column(DateTime, info='对账时间')
#     company_code = Column(String(32), nullable=False, server_default=FetchedValue(), info='公司编码')
#     company_name = Column(String(32), nullable=False, server_default=FetchedValue(), info='公司名称')
#     supplier_code = Column(String(32), nullable=False, server_default=FetchedValue(), info='供应商编码')
#     supplier_name = Column(String(32), nullable=False, server_default=FetchedValue(), info='供应商名称')
#     in_warehouse_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='入库金额')
#     out_warehouse_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='退货金额')
#     rebate_delivery_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='返利配送')
#     promotion_deduct_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                      info='促销扣款')
#     compensation = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='补差')
#     account_passageway_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                        info='账扣通道费')
#     withhold_passageway_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                         info='代扣通道费')
#     account_passageway_total = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                       info='账扣费用合计')
#     statement_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='对账金额')
#     uncollected_account_passageway = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                             info='期末累计未收账扣费用')
#     suggesti_nvoice_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                     info='建议开票总金额')
#     blue_j0_tax00 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝0点金额')
#     blue_ji_tax13 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝13点金额')
#     blue_jf_tax09 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝9点金额')
#     blue_jj_tax09574 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝9.574点金额')
#     blue_jh_tax0989 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝9.89点金额')
#     blue_j2_tax13 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝13点金额')
#     blue_j3_tax14942 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝14.942点金额')
#     red_j0_tax00 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红0点金额')
#     red_ji_tax13 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红13点金额')
#     red_jf_tax09 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红9点金额')
#     red_jj_tax09574 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红9.574点金额')
#     red_jh_tax0989 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红9.89点金额')
#     red_j2_tax13 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红13点金额')
#     red_j3_tax14942 = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红14.942点金额')
#     statement_status = Column(Integer, nullable=False, server_default=FetchedValue(),
#                               info='对账状态0.生成对账单；1.财务确认；2.通道服务对账单')
#     finance_statement_time = Column(DateTime, info='财务对账日期')
#     payment_no = Column(String(32), info='实际付款单号')
#     not_satisfy_payment_no = Column(String(650), info='未满足付款单号')
#     check_ticket_status = Column(Integer, nullable=False, server_default=FetchedValue(),
#                                  info='票核状态 0-发票未录入 1-发票已录入未审核 2-票核通过 3-票核拒绝')
#     tax_total = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='总税额')
#     audit_date = Column(DateTime, info='票核时间')
#     account_period = Column(DateTime, info='账期时间')
#     signature_url = Column(String(100), info='签章凭证')
#     contract_id = Column(String(32), info='合同编号')
#     sign_date = Column(DateTime, info='签章日期')
#     sign_flag = Column(Integer, nullable=False, server_default=FetchedValue(), info='签章状态 0：未签章 1：自动签章 2:手动签章')
#     credit_control_payment_no = Column(String(650), info='信控扣下的白单')
#     create_time = Column(DateTime, nullable=False, server_default=FetchedValue())
#     create_by = Column(String(64))
#     update_time = Column(DateTime, server_default=FetchedValue())
#     update_by = Column(String(20), server_default=FetchedValue())
#     merge_account_no = Column(String(32), info='合并单号')
#     in_warehouse_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                      info='入库税额')
#     out_warehouse_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                       info='退货税额')
#     rebate_delivery_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                         info='返利配送税额')
#     promotion_deduct_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                          info='促销扣款税额')
#     compensation_tax = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='补差税额')
#     account_passageway_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                            info='账扣通道费税额')
#     withhold_passageway_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                             info='代扣通道费税额')
#     suggesti_nvoice_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                         info='建议开票总金额税额')
#     uncollected_account_passageway_tax = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                                 info='期末累计未收账扣费用税额')
#     account_passageway_total_tax = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                           info='账扣费用合计税额')
#     blue_j0_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝0点税额')
#     blue_ji_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝13点税额')
#     blue_jf_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝9点税额')
#     blue_jj_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                 info='蓝9.574点税额')
#     blue_jh_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝9.89点税额')
#     blue_j2_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='蓝13点税额')
#     blue_j3_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                 info='蓝14.942点税额')
#     red_j0_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红0点税额')
#     red_ji_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红13点税额')
#     red_jf_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红9点税额')
#     red_jj_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红9.574点税额')
#     red_jh_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红9.89点税额')
#     red_j2_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(), info='红13点税额')
#     red_j3_tax_amount = Column(Numeric(15, 5), nullable=False, server_default=FetchedValue(),
#                                info='红14.942点税额')
#     account_operator = Column(String(64), info='对账人')

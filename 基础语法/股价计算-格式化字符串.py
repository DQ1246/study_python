name="梦白愿"
price="当前股价"
code="股票代码"
price_daily_growth_factor="每日增长系数"
growth_day="增长天数"
print(f"公司：{name}，{code}：003032，{price}：19.99")
print(f"{price_daily_growth_factor}是：1.2，{growth_day}：7，股价：%.2f"%(19.99*(1.2**7)))

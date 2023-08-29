from exchanges.bitget import BitgetExchange
# 数量限制
def amount_limit(ex: BitgetExchange, df, symbol, amount, amount_max_limit):
    side = None
    # 获取最后一个数据
    last = df.iloc[-1]
    last_date = df.index[-1]
    # 获取当前仓位
    position = ex.fetch_position(symbol)

    side = 'buy' if last['buy'] == 1 else 'sell' if last['sell'] == 1 else None
    if side is None:
        return side

    print(f"strategy [{side}] signal: {last_date} {last['close']}")
    # 如果有新的信号，先取消所有订单
    ex.cancel_orders(symbol)

    # 判断是否有买入信号
    if side == 'buy':
        # 判断是否有空仓
        if position['short']['qty'] > 0:
            # 平空
            print(f"close short: {last['close']}")
            # ex.close_position(symbol, 'buy', position['short']['qty'])
            ex.close_position(symbol, 'buy', amount)
        else:
            if position['long']['qty'] < amount_max_limit:
                # 开多
                print(f"open long: {last['close']}")
                ex.create_order_limit(symbol, 'buy', amount, last['close'])
            else:
                # 超出最大仓位
                print(f"long position is max: {position['long']['qty']}")

    elif side == 'sell':
        # 判断是否有多仓
        if position['long']['qty'] > 0:
            # 平多
            print(f"close long: {last['close']}")
            # ex.close_position(symbol, 'sell', position['long']['qty'])
            ex.close_position(symbol, 'sell', amount)
        else:
            if position['short']['qty'] < amount_max_limit:
                # 开空
                print(f"open short: {last['close']}")
                ex.create_order_limit(symbol, 'sell', amount, last['close'])
            else:
                # 超出最大仓位
                print(f"short position is max: {position['short']['qty']}")
    return side

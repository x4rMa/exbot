pub mod kline;

pub enum Spot {
    Ping,
    Time,
    ExchangeInfo,
    Depth,
    Trades,
    HistoricalTrades,
    AggTrades,
    Klines,
    AvgPrice,
    UiKlines,
    Ticker24hr,
    TickerPrice,
    TickerBookTicker,
    Ticker,
    OrderTest,
    Order,
    OpenOrders,
    OrderCancelReplace,
    AllOrders,
    OrderOco,
    OrderList,
    AllOrderList,
    OpenOrderList,
    Account,
    MyTrades,
    RateLimitOrder,
    UserDataStream,
}

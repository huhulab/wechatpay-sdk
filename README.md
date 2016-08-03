WechatPay
=============

WechatPay is a sdk for wechat pay, Before using this, you need to set up the configuration of wechat pay.

About pay, please read the [wechat pay document](https://pay.weixin.qq.com/wiki/doc/api/index.html)

### how to install

```
    git clone git@github.com:fanhan/wechatpay.git

    cd wechatpay
    python setup.py install
```

or

```
    pip install wechat_pay
```


[How to get openid](https://pay.weixin.qq.com/wiki/doc/api/app.php?chapter=4_4)

### how to use?

``` python

    from wechatpay_sdk import WechatPay

    client = WechatPay(
        appid = 'your_appid',
        mch_id='your_mch_id',
        appSecret = 'your_appSecret',
        partnerKey = 'your_partnerKey',
        notify_url = 'your_notify_url',
        cert = '/path/your_cert.pem'
    )

    # For app sdk pay
    params = {
        'body': 'XX pay test',
        'out_trade_no': 'xxx-xxx-xxx',
        'total_fee': 1,
        'spbill_create_ip': '127.0.0.1'
    }
    ret = client.app_pay(params)

    # Order query
    ret = client.order_query(transaction_id='xxxxx') or client.order_query(out_trade_no='xxxx')

    # Refund order query
    params = {
        'out_order_no': 'xxxx',
    }
    ret = client.refund_order_query(params)

```

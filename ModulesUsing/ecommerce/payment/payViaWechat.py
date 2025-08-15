print("WechatPayment initialized, name:", __name__)


def pullPayRequest():
    print("PayRequest established.")


if __name__ == "__main__":
    print("payViaWechat started as independent script")
    pullPayRequest()
# This will only run when directly use this module. When imported it will not be executed.
# payViaWechat started as independent script
# PayRequest established.

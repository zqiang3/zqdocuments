ASYNC_EVT_NEW   = 0     # 新连接：wp=hid, lp=-1(连出),0(监听),>0(连入)
ASYNC_EVT_LEAVE = 1     # 连接断开：wp=hid, lp=tag 主动被动断开都会收到
ASYNC_EVT_ESTAB = 2     # 连接建立：wp=hid, lp=tag 仅用于连出去的连接
ASYNC_EVT_DATA  = 3     # 收到数据：wp=hid, lp=tag
ASYNC_EVT_PROGRESS = 4  # 待发送数据已经全部发送完成：wp=hid, lp=tag



# 等待事件，seconds为等待的时间，0表示不等待
# 一般要先调用 wait，然后持续调用 read取得消息，直到没有消息了
def wait (self, seconds = 0):
    if self.obj:
        _qnet_async_file:/E:/work/platform/lib/QuickNet.pywait(self.obj, long(seconds * 1000))
        return True
    return False


# 建立一个新的监听连接，返回 hid，错误返回 <0, reuse为是否启用 REUSEADDR
def new_listen (self, ip, port, head = 0, reuse = False):
    if not self.obj:
        self.obj = _qnet_async_new()
        _qnet_async_limit(self.obj, -1, 0x200000)
    if not ip:
        ip = '0.0.0.0'
    if reuse: head |= 0x200
    return _qnet_async_new_listen(self.obj, ip, port, head)
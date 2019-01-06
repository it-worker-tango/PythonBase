class TVshow:
    def __init__(self, show):
        self.__show = show
    @property
    def show(self):
        return self.__show

tvshow = TVshow("正在播放<<海贼王>>")
print("默认:", tvshow.show)

tvshow.show = "这在播放<<火影>>" # 修改属性 这里会报错
print("修改后:", tvshow.show) # 获取属性值
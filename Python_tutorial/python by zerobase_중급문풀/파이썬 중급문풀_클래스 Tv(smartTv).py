import smartTv as st

my4KTv = st.Tv4K('65', 'silver', '4k')
my4KTv.setSmartTv('on')
my4KTv.turnOn()
my4KTv.printTvInfo()
my4KTv.turnOff()

my8KTv = st.Tv8k('75', 'black', '8k')
my8KTv.setSmartTv('on')
my8KTv.setAiTv('on')
my8KTv.turnOn()
my8KTv.printTvInfo()
my8KTv.turnOff()
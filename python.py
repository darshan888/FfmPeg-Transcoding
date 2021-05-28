from mininet.net import Mininet

from mininet.node import  Controller, RemoteController, OVSKernelSwitch

from mininet.cli import CLI

from mininet.log import setLogLevel

from mininet.link import TCLink

 

def topology():

    "Create a network."

    net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )

 

    print "*** Creating nodes"

    h1 = net.addHost( 'h1', ip="192.168.10.1/24", mac='00:00:00:00:00:01')  #video sender

    h2 = net.addHost( 'h2', ip="192.168.10.2/24", mac='00:00:00:00:00:02')  #video receiver

    h3 = net.addHost( 'h3', ip="192.168.10.3/24", mac='00:00:00:00:00:03')  #video transcoder. not used in this case

    s1 = net.addSwitch( 's1', listenPort=6673, mac='00:00:00:00:00:03')

    c0 = net.addController('c0', controller=Controller, ip='127.0.0.1', port=6633 )

 

    print "*** Adding Link"

    net.addLink(h1, s1)

    net.addLink(s1, h2, bw=1, max_queue_size=100)

    net.addLink(s1, h3)

 

    print "*** Starting network"

    net.build()

    c0.start()

    s1.start( [c0] )

    print "*** Running CLI"

    CLI( net )

    print "*** Stopping network"

    net.stop()

 

if __name__ == '__main__':

    setLogLevel( 'info' )

    topology()

from mininet.topo import Topo


class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        hostA = self.addHost( 'A' , mac='00:00:00:00:00:01')
        hostB = self.addHost( 'B' , mac='00:00:00:00:00:02')
        hostC = self.addHost( 'C' , mac='00:00:00:00:00:03')
        hostD = self.addHost( 'D' , mac='00:00:00:00:00:04')
        hostE = self.addHost( 'E' , mac='00:00:00:00:00:05')
        hostF = self.addHost( 'F' , mac='00:00:00:00:00:06')
        

        # Add switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )

        # Add links in s1
        self.addLink(hostA, s1, 1, 2)
        self.addLink(hostB, s1, 3, 4)

        # Add links in s2
        self.addLink(hostC, s2, 5, 6)     
        self.addLink(hostD, s2, 7, 8)        

        # Add links in s5
        self.addLink(hostE, s5, 80, 10)
        self.addLink(hostF, s5, 80, 12)
        
        

        # Add links between switch
        self.addLink(s1, s2, 13, 14)
        self.addLink(s2, s4, 15, 16)
        self.addLink(s4, s3, 17, 18)
        self.addLink(s3, s1, 19, 20)
        self.addLink(s3, s5, 21, 22)
        self.addLink(s1, s5, 23, 24)
        

topos = { 'mytopo': ( lambda: MyTopo() ) }
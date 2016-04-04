# marcos
RIP_MULTICAST_ADDR      = '224.0.0.9'
RIP_UDP_PORT            = 520

RIP_COMMAND_REQUEST     = 1
RIP_COMMAND_RESPONSE    = 2

RIP_METRIC_INFINITY     = 16

RIP_DEFAULT_UPDATE      = 30
RIP_DEFAULT_TIMEOUT     = 180
RIP_DEFAULT_GARBAGE     = 120

RIP_HEADER_SIZE         = 4
RIP_HEADER_PACK_FORMAT  = '!BBH'
RIP_ENTRY_SIZE          = 20
RIP_ENTRY_PACK_FORMAT   = '!HHIIII'

RIP_MAX_ROUTE_ENTRY     = 25
RIP_RECV_BUF_SIZE       = 41600

# it's very unlikely to change in future
RIP_ADDRESS_FAMILY      = 2 

def Mask2PrefixLen(mask): 
    prefix = bin(mask).count('1')
    return prefix

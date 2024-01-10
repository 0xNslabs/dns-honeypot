import os
import argparse
from twisted.internet import reactor, protocol
from twisted.names import dns, server
from twisted.python import log

script_dir = os.path.dirname(os.path.abspath(__file__))

class SimpleDNSProtocol(protocol.DatagramProtocol):
    def datagramReceived(self, datagram, address):
        message = dns.Message()
        try:
            message.fromStr(datagram)
        except (EOFError, dns.UnknownOpcode):
            return

        for query in message.queries:
            self.logQuery(query, address)
            response = self.createResponse(message, query)
            self.transport.write(response.toStr(), address)

    def logQuery(self, query, address):
        log.msg(f"DNS Query Received - Query Name: {query.name.name}, Type: {dns.QUERY_TYPES.get(query.type, 'UNKNOWN')}, Class: {dns.QUERY_CLASSES.get(query.cls, 'UNKNOWN')}, From: {address}")

    def createResponse(self, message, query):
        response = dns.Message(id=message.id, answer=1)
        response.queries = [query]
        query_name_str = query.name.name.decode() if isinstance(query.name.name, bytes) else query.name.name
        
        if query.type == dns.A:
            answer = dns.RRHeader(name=query_name_str, type=dns.A, cls=query.cls, ttl=60, payload=dns.Record_A(address='127.0.0.1'))
            response.answers.append(answer)
        elif query.type == dns.AAAA:
            answer = dns.RRHeader(name=query_name_str, type=dns.AAAA, cls=query.cls, ttl=60, payload=dns.Record_AAAA(address='::1'))
            response.answers.append(answer)
        elif query.type == dns.TXT:
            answer = dns.RRHeader(name=query_name_str, type=dns.TXT, cls=query.cls, ttl=60, payload=dns.Record_TXT(data=['dummy response']))
            response.answers.append(answer)
        elif query.type == dns.MX:
            answer = dns.RRHeader(name=query_name_str, type=dns.MX, cls=query.cls, ttl=60, payload=dns.Record_MX(preference=10, exchange='mail.example.com'))
            response.answers.append(answer)
        elif query.type == dns.CNAME:
            answer = dns.RRHeader(name=query_name_str, type=dns.CNAME, cls=query.cls, ttl=60, payload=dns.Record_CNAME(name='cname.example.com'))
            response.answers.append(answer)
        elif query.type == dns.NS:
            answer = dns.RRHeader(name=query_name_str, type=dns.NS, cls=query.cls, ttl=60, payload=dns.Record_NS(name='ns.example.com'))
            response.answers.append(answer)
        elif query.type == dns.SOA:
            answer = dns.RRHeader(name=query_name_str, type=dns.SOA, cls=query.cls, ttl=60, payload=dns.Record_SOA(mname='ns.example.com', rname='hostmaster.example.com', serial=12345, refresh=3600, retry=600, expire=86400, minimum=3600))
            response.answers.append(answer)
        elif query.type == dns.PTR:
            answer = dns.RRHeader(name=query_name_str, type=dns.PTR, cls=query.cls, ttl=60, payload=dns.Record_PTR(name='ptr.example.com'))
            response.answers.append(answer)
        else:
            log.msg(f"Received unsupported DNS query type: {query.type}")

        return response

class SimpleDNSServerFactory(server.DNSServerFactory):
    def __init__(self):
        clients = [SimpleDNSProtocol()]
        super(SimpleDNSServerFactory, self).__init__(clients=clients)

def main():
    LOG_FILE_PATH = os.path.join(script_dir, "dns_honeypot.log")
    parser = argparse.ArgumentParser(description='Run a DNS honeypot server.')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to bind the server to.')
    parser.add_argument('--port', type=int, default=5353, help='Port to bind the server to.')
    args = parser.parse_args()

    print(f"DNS HONEYPOT ACTIVE ON HOST: {args.host}, PORT: {args.port}")
    print(f"ALL DNS queries will be logged in: {LOG_FILE_PATH}")

    log_observer = log.FileLogObserver(open(LOG_FILE_PATH, 'a'))
    log.startLoggingWithObserver(log_observer.emit, setStdout=False)

    dns_factory = SimpleDNSServerFactory()

    reactor.listenUDP(args.port, SimpleDNSProtocol(), interface=args.host)
    reactor.listenTCP(args.port, dns_factory, interface=args.host)
    reactor.run()

if __name__ == "__main__":
    main()

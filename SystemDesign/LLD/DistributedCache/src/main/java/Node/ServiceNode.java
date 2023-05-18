package Node;

/**
 * Service Node or server node, it is the physical server node
 */
public class ServiceNode implements Node {
    private final String name;
    private final String ip;
    private final String port;

    /**
     *
     * @param name name identifier of the server
     * @param ip ip address of the server
     * @param port port of the server
     */
    public ServiceNode(String name, String ip, String port) {
        this.name = name;
        this.ip = ip;
        this.port = port;
    }

    @Override
    public String getKey() {
        return name + "-" + ip + ":" + port;
    }

    @Override
    public String toString() {
        return getKey();
    }
}

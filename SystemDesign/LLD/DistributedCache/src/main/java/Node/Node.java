package Node;

/**
 * Node is a thing that can be mapped to the hash ring, for ex. server, virtual nodes, key-value pair
 */
public interface Node {
    /**
     *
     * @return key string
     */
    String getKey();
}

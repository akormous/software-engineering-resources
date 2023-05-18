package HashFunction;

/**
 * Hash Function: used for generating hash value for a given string
 * it is an interface, so that custome Hash functions can be implemented
 */
public interface HashFunction {
    long hash(String key);
}

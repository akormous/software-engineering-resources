package HashFunction;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * MD5 Hash Function: a class that uses MD5 algorithm to generate hash values
 */
public class MD5HashFunction implements HashFunction {
    MessageDigest instance;

    public MD5HashFunction() {
        try {
            instance = MessageDigest.getInstance("MD5");
        }
        catch (NoSuchAlgorithmException e) {

        }
    }

    @Override
    public long hash(String key) {
        instance.reset();
        instance.update(key.getBytes());
        byte[] digest = instance.digest();

        long h = 0;
        for(int i = 0; i < 4; i++) {
            h = h << 8;
            h = h | ((int) digest[i]) & 0xFF;
        }
        return h;
    }
}

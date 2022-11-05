# JSON Web Token
- JWT is an open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object.
- This information can be verified and trusted because it is digitally signed.
- JWTs can be signed using a secret (HMAC algorithm) or a public/private key pair using RSA or ECDSA.
- **Signed** tokens can verify the integrity of the claims contained within it.
- **Encrypted** tokens hide those claims from other parties.
- When tokens are signed using public/private key pairs, the signature also certifies that only the part holding the private key is the one that signed it.

## When to use JWT?

### Authorization
This is the most common scenario, once the user is logged in, each subsequent request will include the JWT, allowing the user to access routes, services, and resources that are permitted with that token.
Ex. Single-sign on

### Information Exchange
Securely transmitting information between parties, because JWTs can be signed using public/private key pairs - you can be sure the senders are who they say they are. Additionally, as the signature is calculated using the header and the payload, you can also verify that the content hasn't been tampered with.

## JWT Structure
It consists of 3 parts separated by dots (`.`):
- Header
- Payload
- Signature

Therefore, a JWT typically looks like the following.

`xxxxx.yyyyy.zzzzz`

## Header
It consists of 2 parts - 

- type of the token, which is JWT
- signing algorithm being used (HMAC SHA256 or RSA)

For example,
```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```

Then, this JSON is Base64Url encoded to form the first part of the JWT

## Payload
It contains the claims. Claims are statements about an entity (typically, the user) and additional data. There are 3 types of claims: *registered, public,* and *private* claims. For more details, read [here](https://jwt.io/introduction).

For example,
```json
{
    "sub": "1234567890",
    "name": "Ben Dover",
    "admin": true,
}
```
Then, this JSON is Base64Url encoded to form the second part of the JWT

## Signature
To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that.
For example, if you use HMAC SHA256 algorithm:

```py
HMACSHA256(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
    secret
)
```

## Putting all together
The output is 3 Base64-URL strings separated by dots that can be easily passed in HTML and HTTP environments, while being more compact when compare to XML-based standards such as SAML.

For example,
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkJlbiBEb3ZlciIsImFkbWluIjp0cnVlfQ.nNM50laahYfPPnkvvWwM_9lGFaFS9il0qaiX6WLQyOM
```

# How JWTs are propagated?

```mermaid

flowchart LR
    id1[Application Client]
    id2[Authorization Server AuthO]
    id3[Your API Resource Server]

    id1 -->|1| id2
    id2 -->|2| id1
    id1 -->|3| id3

```

1. The client request authorization to the authorization server.
2. The authorization server returns an access token to the application.
3. The application uses the access token to access a protected resource (like an API)
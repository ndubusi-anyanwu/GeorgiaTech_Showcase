#!/usr/bin/env python3

from typing import Tuple
import oracle
import crypto

def main(message: bytes, injection: bytes) -> Tuple[bytes, str]:
    """ Your goal is to bypass the oracle's integrity check.

    This will break UF-CMA security of the scheme and demonstrate a length
    extension attack on the underlying SHA1 hash function, which relies on the
    Merkle-Damgard construction internally.

    Specifically, you must somehow craft a message that includes the given
    parameter WITHIN the default message AND find a valid tag for it WITHOUT
    querying the oracle.

    Your attack should be able to inject any message you want, but we want you
    to include your GT username (as bytes) specifically.
    """

    

    
    if not isinstance(message, bytes) or not isinstance(injection, bytes):
        raise TypeError(f"expected bytes as args, got {type(message)} and {type(injection)}")
    
    # The original message and its SHA-1 hash.
    reg_message = message

    tag = oracle.query(reg_message)
    
    # length extension attack.
    
    for secret_length in range(1, 100):
    
    #  padding

        padding = crypto.Sha1.create_padding(reg_message, secret_length)
    
    # New  forge message
        forged_message = reg_message + padding + injection
    
    # Start to construct the forged SHA-1 hash.
        hasher = crypto.Sha1()
    
   
    # Convert the original tag (hex) to bytes.

        a, b, c, d, e = (int(tag[i:i+8], 16) for i in range(0, 40, 8))

        initial_state = (a, b, c, d, e)
    
    # Update  hasher
        hasher.update(injection)
    
    # forged tag

        forged_tag = hasher.hexdigest(extra_length=secret_length + len(reg_message) + len(padding),
                                   initial_state=initial_state)
    
        if oracle.check(forged_message, forged_tag):
                return forged_message, forged_tag
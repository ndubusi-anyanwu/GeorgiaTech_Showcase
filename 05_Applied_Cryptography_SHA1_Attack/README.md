# SHA-1 Length Extension Attack Implementation

**Subject Area:** Applied Cryptography · Hash Function Security · Exploit Implementation · Cryptographic Attacks

---

## What It Does

This project implements a **SHA-1 length extension attack** from scratch in Python — a classical cryptographic attack that allows an attacker to append arbitrary data to a MAC-protected message and forge a valid authentication tag, without knowing the secret key. The implementation reconstructs the internal hash state from an intercepted digest, manually re-initializes the SHA-1 compression function from that state, and produces a valid forged MAC for the extended message.

## Problem Addressed

Hash-based message authentication codes (HMACs) built using vulnerable constructions — specifically `H(secret || message)` rather than the proper HMAC standard — are susceptible to length extension. This attack exploits a fundamental property of Merkle-Damgård hash functions (MD5, SHA-1, SHA-256) where the output digest directly encodes the internal state, allowing state reconstruction and continued hashing. Understanding this vulnerability is essential for evaluating legacy authentication implementations and recommending secure alternatives.

## Practical Relevance

Length extension vulnerabilities have appeared in real-world systems: the Flickr API authentication flaw (2009), early Amazon Web Services signature schemes, and several open-source web frameworks. Any system that protects integrity with a naive `hash(secret + data)` construction instead of `HMAC(key, data)` is potentially vulnerable. This implementation demonstrates exactly how such an attack works, which is critical for:

- Security code review: identifying improper MAC constructions
- Penetration testing: exploiting vulnerable API authentication schemes
- Cryptographic education: building intuition for why HMAC is the correct construction

## Tools, Languages, and Libraries

Python · SHA-1 internals · Merkle-Damgård structure · struct (binary packing) · bitwise operations

## Skills Demonstrated

- Cryptographic attack implementation: translating a theoretical attack into working code
- Low-level binary manipulation: manually reconstructing hash state from raw digest bytes
- Understanding of hash function internals: SHA-1 padding, block structure, compression function
- Security analysis: connecting the attack to real-world vulnerable implementations
- Communicating cryptographic concepts clearly in code and comments

## Extension Ideas

- Extend the attack to SHA-256 and benchmark against SHA-1
- Build a demonstration web application with a vulnerable MAC endpoint and a corresponding attack client
- Implement the fix alongside the attack: show how switching to HMAC-SHA1 defeats the length extension
- Analyze which modern hash functions (SHA-3 / Keccak) are structurally immune to this attack and explain why

---

*Georgia Institute of Technology — MS Cybersecurity · CS 6260: Applied Cryptography*

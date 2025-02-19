# hm-dive
A Basic Encryption/Decryption Terminal Tool
Made for CS3090: Ethics in Computing

Symmetric encryption/decryption of a text file using a randomly-generated key.
Overwrites existing file for both encryption and decryption.

This basic script uses the [Fernet library](https://cryptography.io/en/latest/fernet/) from Python cryptography; installation of cryptography is required to run this code.
Use `python hm-dive.py -h` for help.

### Notes/Warnings about use:
Current implementation requires that you `cd` into the project directory to run the script.
This tool overwrites the targets file, and creates a new binary file containing the key. 
The key file will also be overwritten if you try to encrypt something multiple times.
In other words, **if you encrypt something twice, the data is lost unless you made a copy of the first generated key.**
Be very careful to automate this for encrypting multiple files as this is untested behavior. Be absolutely sure you know what you're doing.

### Ethical considerations, responsible use
A tool similar to this or that references this could be used for a ransomware attack.
If something would be able to call other terminal commands, it could theoretically use this code to lock your files behind encryption and then move the keys elsewhere.
As always, be very careful which cryptography software you trust.
**This is an educational tool. There are much better and safer implementations of CLI encryption elsewhere**

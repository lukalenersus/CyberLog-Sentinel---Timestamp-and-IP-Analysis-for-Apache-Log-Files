https://github.com/gracenolan/Notes/blob/master/interview-study-notes-for-security-engineering.md#threat-modeling

—Parse timestamp and IP from apache log files

—Correlate data from 2 separate logs, parse and store them using hashmap of lists so you can look it up in O(1) time later

—Count frequency of words that appear in a text

—Make API calls using requests and write tests for your methods

—Write a caesar cipher

—Leetcode easy string manipulation questions

—Leetcode medium string problems involving a stack
These security engineering challenges focus on text parsing and manipulation, basic data structures, and simple logic flows. Give the challenges a go, no need to finish them to completion because all practice helps.

Cyphers / encryption algorithms
Implement a cypher which converts text to emoji or something.
Be able to implement basic cyphers.
Parse arbitrary logs
Collect logs (of any kind) and write a parser which pulls out specific details (domains, executable names, timestamps etc.)
Web scrapers
Write a script to scrape information from a website.
Port scanners
Write a port scanner or detect port scanning.
Botnets
How would you build ssh botnet?
Password bruteforcer
Generate credentials and store successful logins.
Scrape metadata from PDFs
Write a mini forensics tool to collect identifying information from PDF metadata.
Recover deleted items
Most software will keep deleted items for ~30 days for recovery. Find out where these are stored.
Write a script to pull these items from local databases.
Malware signatures
A program that looks for malware signatures in binaries and code samples.
Look at Yara rules for examples.
Put your work-in-progress scripts on GitHub and link to them on your resume/CV. Resist the urge to make your scripts perfect or complete before doing this.
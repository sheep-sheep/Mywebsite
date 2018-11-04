1. what would happen when you visit a website?
* The first place your computer looks for the corresponding IP address is its local DNS cache
* your computer queries (contacts) the recursive DNS servers (resolvers) from your internet service provider (ISP)
* If the recursive servers don’t have the answer, they query the root name servers
* The root name servers will look at the first part of our request, reading from right to left — www.yangzhang.us — and in our case, direct our query to the top-level domain (TLD) name servers for .us
* TLD name servers review the next part of our request and direct to authoritative name servers. (address record (A record)) and stores the record in its local cache. All records have a time-to-live value
* Recursive server returns the A record back to your computer. Your computer stores the record in its cache, reads the IP address from the record, then passes this information to your browser. The browser then opens a connection to the webserver and receives the website.


2. What's the difference between clone() and fork()?

3. What's a file descriptor?

4. What's an inNode?

5. What will happen if a command line is too long?

6. fork，virtual memory, file system, inode

7. process 和 thread 
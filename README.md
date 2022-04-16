# UGC (Unturned Gas Calculator)

UGC is a tool made specifically for Unturned Role-play servers.


### Using UGC

1. Enter your Gas Price.
2. Enter the amout of percent the tank is on.


### Example

Current Gas Price: 0.63

Tank Level: 30

Output:

<pre><code> Total Price: 44.1
</code></pre>

### How it works

Firstly when a user inputs his "Gas Price" it gets converted into a float, because gas prices usually have comma values. UGC then finds out the percent it has to fill by taking 100 (total) and deducting their "Tank Level" which then gets multiplied by the "Gas Price".

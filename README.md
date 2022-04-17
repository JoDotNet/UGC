# UGC (Unturned Gas Calculator)

UGC is a tool made specifically for Unturned role-play servers.


### Using UGC

1. Enter your Gas Price.
2. Enter the amount of percent the tank is on.


### Example

Current Gas Price: 0.63

Tank Level: 30

Output:

<pre><code> Total Price: 44.1
</code></pre>

### How it works

Firstly when a user inputs his "Gas Price" it gets converted into a float value, because gas prices usually have comma values. UGC then finds out the percent it has to fill by taking 100 (total) and deducting their "Tank Level" which then gets multiplied by the "Gas Price".


### Upcomming Features

- Graphical UI
- Config File (default gas price etc.)

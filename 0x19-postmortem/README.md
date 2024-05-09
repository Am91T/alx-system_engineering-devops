# Postmortem: E-commerce Website Slowdown (April 10th, 2024)

## Issue Summary

On Thursday, April 10th, 2024, our e-commerce website experienced a significant slowdown between 14:30 PST and 15:45 PST. During this outage, users encountered extended loading times and difficulty completing transactions. We estimate that this impacted approximately 30% of our website traffic, potentially leading to lost sales.

## Timeline

* `14:30 PST`: Monitoring alerts indicated a surge in response times for product page loads.
* `14:32 PST`: An engineer on call identified the slowdown and began investigating. Initial suspicion fell on a recent product data update that had just been deployed.
* `14:40 PST`: The product data update was rolled back, but response times remained slow.
* `14:50 PST`: The investigation shifted towards database performance. Database queries were taking longer than usual, causing bottlenecks.
* `15:00 PST`: The incident was escalated to the database administration team.
* `15:15 PST`: The database team identified a failing disk on one of the database servers.
* `15:30 PST`: The failing disk was replaced, and the database server was restarted.
* `15:45 PST`: Website performance returned to normal.

## Root Cause and Resolution

The root cause of the slowdown was a failing disk on a database server. This disk malfunction led to slow read/write times, impacting database query performance. Replacing the faulty disk and restarting the server resolved the issue.

## Corrective and Preventative Measures

`**Improve Database Monitoring**`: We will implement more granular monitoring of individual database servers, including disk health checks. This will allow for faster detection of potential hardware failures.

`**Redundancy Measures**`: We will explore implementing redundancy for critical database components, such as a RAID configuration for storage. This will ensure continued operation in case of future hardware failures.

`**Automated Failover**`: Investigate and implement automated failover mechanisms for database servers. This would automatically switch to a secondary server in case of a primary server failure, minimizing downtime.

`**Scheduled Maintenance**`: Implement scheduled maintenance windows for database servers to proactively identify and address potential issues.

This postmortem serves as a learning experience. By implementing the corrective and preventative measures outlined above, we can minimize the risk of similar outages in the future and ensure a smoother user experience on our e-commerce platform.
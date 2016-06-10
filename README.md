## Description

Simple script to check if some endpoints are working (200) and returning the context you expect.

Ideal to run on a CI server like Jenkins periodically; so you will get email
with errors on failures.

## Configuration

Check `config.cfg.sample`

## Sample output

```python run.py

Running checkHealth script at 2016/06/10 21:06:54

Checking google-works
* Request took 0 seconds
* OK
Checking unexisting-retry
* Request took 0 seconds
* Service unexisting-retry check FAILED at 2016/06/10 21:06:54: 'http://unexisting.domain.com/' doesn't contain 'Missing content'
```

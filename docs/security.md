# Lab 5.7 — OWASP Juice Shop

## Completed Challenges

### 1. DOM XSS

**OWASP Top 10:** A03:2021 — Injection

The DOM XSS challenge demonstrates how malicious JavaScript can be executed in the browser through unsafe DOM manipulation. The payload used was:

`<iframe src="javascript:alert(`xss`)">`

**How Patuvaj would prevent it:**
Patuvaj should avoid inserting untrusted user input into the DOM as HTML, use safe DOM APIs and apply proper output encoding.

### 2. Bonus Payload

**OWASP Top 10:** A03:2021 — Injection

The Bonus Payload challenge demonstrates that DOM XSS can also be used to inject an iframe containing external content. I completed it using the provided SoundCloud iframe payload.

**How Patuvaj would prevent it:**
Patuvaj should sanitize untrusted HTML, restrict allowed iframe sources with Content Security Policy (CSP), and avoid rendering user-provided HTML without validation.

## Additional Challenge

### Score Board

Found the hidden Score Board page in OWASP Juice Shop.
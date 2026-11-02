## Question 14

The AGPL matters because it includes a network-use requirement. If a company modifies AGPL-licensed software and makes that modified version available to users over a network, it must offer those users the corresponding source code.

The GPL generally requires source-code availability when the software is distributed. Since Patuvaj only provides its platform over the internet and does not distribute the software, the GPL's distribution requirement would generally not be triggered. The AGPL closes this network-use gap.


## Dependency Licence Analysis

These three dependencies are taken from my SquidFlag project (`apps/api/package.json`).

| Dependency | Licence | Could Patuvaj use it in its closed product? |
| ---------- | ------- | ------------------------------------------- |
| `@nestjs/common` | MIT | Yes. MIT permits use in closed-source commercial products, provided the copyright and licence notice are preserved. |
| `fastify` | MIT | Yes. MIT permits commercial and closed-source use, provided the copyright and licence notice are preserved. |
| `zod` | MIT | Yes. MIT permits use in closed-source products, provided the copyright and licence notice are preserved. |
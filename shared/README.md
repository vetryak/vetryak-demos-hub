# shared/

Código compartilhado entre demos. Só crie um pacote aqui quando **duas ou mais demos**
precisarem do mesmo código (regra da vertical slice: duplicar um pouco é melhor do que
acoplar cedo).

Cada pacote é um projeto moon (`shared/<pacote>/moon.yml`) e a demo que usa declara
`dependsOn: ["<pacote>"]`.

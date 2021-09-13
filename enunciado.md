# DEIParty
Para inaugurar os novos laboratórios da RNL, o departamento fará o primeiro churrasco do ano. Para tal, todas as bebidas serão catalogadas pela nova aplicação DEIParty. Já foi implementada toda a lógica de armazenamento de stocks e encomendas automáticas das bebidas que estão perto de acabar, com as mais recentes técnicas de inteligência artificial, na API *Partystore*.

O objectivo deste exercício é desenvolver a aplicação **DEIParty** usando a framework **Django**[2][3] (versão 3.1.x).

A aplicação DEIParty vai interagir com a API *Partystore*[1]. Deve testar os exemplos dados para cada operação de modo a perceber as características dos pedidos à API.

A aplicação DEIParty deve implementar as seguintes funcionalidades:
- Uma página que lista todas as *bebidas* devolvidos pela API numa tabela. A cada entrada da tabela está associada uma *bebida* e as colunas devem corresponder ao id, designação, quantidade disponível e imagem devolvida pela *Partystore*.
- A página pessoal de cada *bebida* que deve conter o id, designação, quantidade disponível, fornecedor e imagem da *bebida*.
- Uma página com um formulário capaz de adicionar novas *bebidas* através da API fornecida.
- Capacidade de aumentar/diminuir a quantidade disponível de uma *bebida* através da API fornecida.
- Capacidade de remover uma *bebida* através da API fornecida.

Para *endpoints* da API *Partystore* protegidos, deverá utilizar o seu IST ID como token de acesso.

Deve realizar o exercício de forma modular: poderemos, por exemplo, querer adicionar descrições às bebidas para eventualmente expôr uma carta de vinhos aos participantes.
Serão valorizadas qualidade e estética do código e da interface web apresentada.

Deve submeter num arquivo comprimido por email a sua solução e um ficheiro README, que descreva o procedimento para iniciar um servidor local de testes.
Prazo máximo de entrega: domingo, 19 de setembro de 2021, 23:59

Recursos potencialmente úteis:
- https://tailwindcss.com/
- https://getbootstrap.com/

Boa Sorte!

Nota: Durante os testes da adição de novas *bebidas* pedimos que seja responsável nas designações, fornecedores e imagens utilizadas.

[1]: https://aduck.rnl.tecnico.ulisboa.pt/deiparty/swagger-ui/index.html
[2]: https://www.djangoproject.com/
[3]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/

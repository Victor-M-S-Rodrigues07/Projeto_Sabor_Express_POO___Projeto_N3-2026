# <h1 align = "center"> Sabor Express - Aplicativo de Restaurantes (POO) </h1>

<div align = "center">

<img src = ".\imgs\readme-capa.png" alt = "Console mostrando a lista de restaurantes pré-cadastrados" height = "230">

</div>

### Status do Projeto: Concluído ✔️ <br>

## 🗂 Sumário

- [📝 Descrição do Projeto](https://github.com/Victor-M-S-Rodrigues07/Projeto_Sabor_Express_POO___Projeto_N3-2026#-descri%C3%A7%C3%A3o-do-projeto)
- [🎯 Objetivos do Curso](https://github.com/Victor-M-S-Rodrigues07/Projeto_Sabor_Express_POO___Projeto_N3-2026#-objetivos-do-curso)
- [↩ Versão Anterior do Projeto](https://github.com/Victor-M-S-Rodrigues07/Projeto_Sabor_Express_POO___Projeto_N3-2026#-vers%C3%A3o-anterior-do-projeto)
- [💻 Tecnologias Utilizadas](https://github.com/Victor-M-S-Rodrigues07/Projeto_Sabor_Express_POO___Projeto_N3-2026#-tecnologias-utilizadas)
- [⚙ Funcionalidades do Projeto](https://github.com/Victor-M-S-Rodrigues07/Projeto_Sabor_Express_POO___Projeto_N3-2026#-funcionalidades-do-projeto)
- [📥 Acesso ao Projeto](https://github.com/Victor-M-S-Rodrigues07/Projeto_Sabor_Express_POO___Projeto_N3-2026#-acesso-ao-projeto)
- [▶️ Abrir e Rodar o Projeto](https://github.com/Victor-M-S-Rodrigues07/Projeto_Sabor_Express_POO___Projeto_N3-2026#%EF%B8%8F-abrir-e-rodar-o-projeto)
- [📂 Estrutura do Projeto](https://github.com/Victor-M-S-Rodrigues07/Projeto_Sabor_Express_POO___Projeto_N3-2026#-estrutura-do-projeto)
- [✨Autor](https://github.com/Victor-M-S-Rodrigues07/Projeto_Sabor_Express_POO___Projeto_N3-2026#autor)
- [👨🏻‍💻 Contatos & Referências](https://github.com/Victor-M-S-Rodrigues07/Projeto_Sabor_Express_POO___Projeto_N3-2026#%E2%80%8D-contatos--refer%C3%AAncias)

## 📝 Descrição do Projeto

No mundo da programação existem vários caminhos para atingir um objetivo. Na Álgebra, por exemplo, tanto *2 + 2* quanto *4 - 2*, dão o mesmo resultado. Na programação, isso também é verdade. Você pode criar o mesmo aplicativo usando duas linguagens de programação diferentes, pode percorrer listas usando métodos diferentes e até usar funções como *sum()* no lugar do laço de repetição *for* com *x = x + parâmetro*. Além desses exemplos, a forma como se desenvolve um código pode assumir outros formatos. Os dois paradigmas mais difundidos são o **Estruturado** e o **Orientado a Objetos**.

No paradigma Estruturado, o código é escrito em blocos longos, sequenciais, divididos por funções e estruturas de dados definidas pelo desenvolvedor, como o *struct*, da linguagem C. Já no paradigma Orientado a Objetos, ou Programação Orientada a Objetos (POO), a separação é realizada por classes, cada uma com seus atributos e métodos e é esse paradigma que foi usado para criar este projeto.

A **Sabor Express - POO** é a reconstituição da plataforma de cadastro de restaurantes do projeto anteiror. Nessa versão, os restaurantes e as avaliações foram modeladas em classes, na qual os métodos anteriormente concentrados em um único arquivo *app.py* foram distribuídos, aproveitando os recursos oferecidos pela Programação Orientada a Objetos. Desde **métodos da classe** até a criação de **propriedades (@property)**, o projeto retrata uma aplicação baseada em um cenário real, além de demonstrar conceitos fundamentais da Programação Orientada a Objetos, como composição entre classes, os métodos especiais e a reutilização de código.

O repositório apresenta também pequenas atividades complementares do curso, usadas para treinamento extra de conceitos aprendidos no curso.

Esse projeto foi criado a fim de aprofundar o aprendizado na linguagem de programação Python para o *Back-End*, apresentado no curso *Python: Aplicando a Orientação a Objetos* (o link do curso estará disponível no final do README). Nas próximas seções serão apresentados a estrutura do projeto, as funcionalidades implementadas, os conceitos de Programação Orientada a Objetos explorados durante o desenvolvimento, as tecnologias utilizadas e as instruções para executar a aplicação em seu ambiente local.

> [!NOTE]
> Como citado acima, os exercícios e a proposta do projeto foram criados pela ***Alura*** para o curso **Python: Aplicando a Orientação a Objetos**, enquanto o desenvolvimento, a redação e organização do README são de autoria deste desenvolvedor, compartilhados para fins de composição de portfólio profissional.

## 🎯 Objetivos do Curso

- Entenda a importância da Orientação a Objetos com Python;
- Descubra a importância de classes e atributos inspirado em um projeto real;
- Utilize métodos estáticos e encapsulamento;
- Entenda como as propriedades como elas podem conter lógica adicional além de simplesmente acessar e atribuir valores;
- Compreenda como as classes no Python podem organizar e estruturar seu código de forma eficiente;
- Aprenda a usar o construtor para inicializar objetos e definir seus estados iniciais.

## ↩ Versão Anterior do Projeto

A versão Estruturada pode ser encontrada [aqui](https://github.com/Victor-M-S-Rodrigues07/Projeto-Sabor-Express--Projeto-N2-2026). <br>

> [!IMPORTANT]
> Essa é uma série de 3 (três) projetos que constituem a formação [Aprenda a programar em Python com Orientação a Objetos](https://cursos.alura.com.br/app/learning-guide/alura/linguagem-python), da Alura. Nela, são abordados os principais temas de Orientação a Objetos no Python. Esse repositório pertence ao segundo curso da trilha.

## 💻 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-0?style=for-the-badge&logo=python&logoColor=%23FFFFFF&color=%233776AB)
![Git](https://img.shields.io/badge/Git-0?style=for-the-badge&logo=git&logoColor=%23FFFFFF&color=%23F05032)
![GitHub](https://img.shields.io/badge/GitHub-0?style=for-the-badge&logo=github&logoColor=%23FFFFFF&color=%23181717) <br>

## ⚙ Funcionalidades do Projeto

- Uso de **Classes** e **Objetos** para representar as entidades do dia a dia do ramo de cadastro de restaurantes;
- Uso dos **Construtores** para criarem as instâncias de cada classe utilizando parâmentros personalizados;
- Método ***`__str__`*** para imprimir os objetos de forma mais agradável ao usuário;
- **Métodos de Classe** próprios para listar os restaurantes cadastrados, permitindo ao usuário ver quais restaurantes foram inseridos;
- Utilização do ***decorator*** e ***@property*** a fim de permitir a criação e o manuseio de certos atributos;
- DocString para comunicação e explicação de funções entre devs. <br>

## 📥 Acesso ao Projeto

Para obter uma cópia do projeto em sua máquina, clone este repositório utilizando o Git:

```bash
git clone https://github.com/Victor-M-S-Rodrigues07/Projeto_Sabor_Express_POO___Projeto_N3-2026.git
```

Ou, se preferir, faça o download do projeto clicando em **Code** > **Download ZIP** no GitHub e extraia os arquivos para uma pasta da sua preferência. Como mostra a imagem abaixo:

<div align = "center">
    <img src = ".\imgs\ilustracao-clone.png" alt = "Imagem ilustrando um trecho do site GitHub cotnendo o botão Code e as opções de extração do arquivo">
</div>

## ▶️ Abrir e Rodar o Projeto

1. Certifique-se de possuir o **Python 3** instalado em seu computador, principalmente a versão 3.10 ou superiores.
2. Abra o projeto em uma IDE de sua preferência, como o **Visual Studio Code**, o **PyCharm** ou outra compatível com Python.
3. Navegue até a pasta do projeto pelo terminal:

```bash
cd caminho/para/o/projeto
```

4. Execute o arquivo principal da aplicação:

```bash
python main.py
```

Em alguns sistemas operacionais, pode ser necessário utilizar:

```bash
python3 main.py
```

## 📂 Estrutura do Projeto

```
/atividades_curso
    atividades-p4
        /models
            __pycache__
            biblioteca.py
            livro.py
        
        main.py
    
    atividades-p1.py
    atividades-p2-1.py
    atividades-p2-2.py
    atividades-p3.py

/imgs

/modelos
    __pycache__
    avaliacao.py
    restaurante.py

.gitignore
app.py
README.md
```

## ✨Autor

<img src = "https://avatars.githubusercontent.com/u/187053289?v=4" width = 120px> <br>
<strong> Victor </strong>

## 👨🏻‍💻 Contatos & Referências

<a href = "https://www.linkedin.com/in/victor-m-rodrigues/"><img alt="Static Badge" src="https://img.shields.io/badge/LinkedIn-0?style=for-the-badge&logoColor=%23FFFFFF&color=%230077B5&link=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fvictor-m-rodrigues%2F"></a> 
<a href = "https://github.com/Victor-M-S-Rodrigues07/"><img alt="Static Badge" src="https://img.shields.io/badge/GitHub-0?style=for-the-badge&logo=github&logoColor=%23ffffff&labelColor=%23000000&color=%2300000000"></a>
<a href = "https://cursos.alura.com.br/user/victorvicmr"><img alt="Static Badge" src="https://img.shields.io/badge/Alura-0?style=for-the-badge&color=%23100D36"></a>
<a href = "https://cursos.alura.com.br/course/python-aplicando-orientacao-objetos"> <img alt="Static Badge" src="https://img.shields.io/badge/Python%3A%20Aplicando%20a%20Orienta%C3%A7%C3%A3o%20a%20Objetos-0?style=for-the-badge&label=Curso&labelColor=646057&color=FCC34F"> </a>

🇧🇷 - 2026

# DTEM Treinamentos — Landing Page

A página institucional da DTEM é publicada no GitHub Pages com domínio personalizado.

## Endereços

- **Ementa (página principal):** https://dtemtreinamentos.com.br/ementa/
- **Raiz do domínio:** https://dtemtreinamentos.com.br/ redireciona para `/ementa/`.

## Estrutura

- `index.html`: redirecionamento da raiz para `/ementa/` (preserva parâmetros e âncoras quando JavaScript está disponível).
- `ementa/index.html`: página da formação, com conteúdo, navegação e inscrição.
- `styles.css`: estilos compartilhados pela página da ementa.
- `script.js`: interações compartilhadas da página.
- `assests/`: imagens utilizadas pela página.

Ao editar `ementa/index.html`, mantenha os caminhos relativos `../styles.css`, `../script.js` e `../assests/`.

## Publicação

O workflow `.github/workflows/pages.yml` publica a pasta `landpage/` por **GitHub Actions** após alterações nessa pasta na branch `main`, ou pela execução manual do workflow. A configuração de domínio e HTTPS fica em **Settings → Pages** no GitHub.

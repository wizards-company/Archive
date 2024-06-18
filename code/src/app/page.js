// page.js

import styles from "./page.module.css"; // Importa estilos CSS do arquivo page.module.css

/**
 * Componente principal da página inicial.
 * Renderiza um título, uma imagem, um texto de apoio e links importantes.
 */
export default function Home() {
  return (
    <main className={styles.main}>                      {/* Aplica a classe .main para o estilo principal */}
      <h1>Não pague pelo que você lê</h1>               {/* Título principal */}
      <img
        className="next-image"                          // Classe para estilização de imagem do Next.js (não aplicada pelo CSS)
        src="/Liesel-Meminger.png"                      // Caminho para a imagem de capa do livro
        alt="Capa do livro A Menina que Roubava Livros" // Descrição da imagem para acessibilidade
        unoptimized                                     // Próxima renderização otimizada (Next.js)
        width={300}                                     // Largura da imagem
        height={450}                                    // Altura da imagem
      />
      <p>                                                                                 {/* Texto de apoio */}
        Explore uma nova maneira de compartilhar histórias! <br /> 
        Troque livros ou doe para nossa comunidade acolhedora e apaixonada pela leitura.
      </p>
      <div>
        <a href="https://github.com/wizdoux/Library">Github Link</a>                      {/* Link para o GitHub */}
        {" "} | {" "}                                                                     {/* Separador */}
        <a href="https://discord.gg/BKkqutKh9s">Discord Link</a>                          {/* Link para o Discord */}
      </div>
    </main>
  );
}

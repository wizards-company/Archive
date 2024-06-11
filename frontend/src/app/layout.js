import "./globals.css";

export const metadata = {
  title: "Libs",
  description: "Ganhe livros através de doações",
};

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
